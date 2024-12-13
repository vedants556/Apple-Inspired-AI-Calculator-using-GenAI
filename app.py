import os
import cv2
import PIL
import numpy as np
import google.generativeai as genai
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from streamlit_extras.add_vertical_space import add_vertical_space
from dotenv import load_dotenv
from warnings import filterwarnings

# Suppress warnings for cleaner output
filterwarnings(action='ignore')

class Calculator:
    def streamlit_config(self):
        # Set Streamlit page config
        st.set_page_config(
            page_title="AI Math Solver",
            page_icon=":robot:",
            layout="wide"
        )

        # Custom page background and header styling
        page_background_color = """
        <style>
        [data-testid="stHeader"] {
            background: rgba(0,0,0,0.1);
            color: #FFFF;
            padding-top: 0rem;
        }
        .block-container {
            padding-top: 3rem;
            padding-bottom: 1rem;
        }
        .rainbow-text {
            font-size: 3rem;
            font-weight: bold;
            animation: rainbow 15s linear infinite;
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent;
        }
        @keyframes rainbow {
            0% { color: red; }
            14% { color: orange; }
            28% { color: yellow; }
            42% { color: green; }
            57% { color: blue; }
            71% { color: indigo; }
            85% { color: violet; }
            100% { color: red; }
        }
        </style>
        """
        st.markdown(page_background_color, unsafe_allow_html=True)

        # Add rainbow text as the header
        st.markdown('<h1 class="rainbow-text" style="text-align: center;">AI Calculator</h1>', unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>Draw an equation on the canvas, and let AI solve it for you!</h5>", unsafe_allow_html=True)

        # Add some vertical space for better alignment
        add_vertical_space(2)

    def __init__(self):
        load_dotenv()
        if 'GOOGLE_API_KEY' not in os.environ:
            raise EnvironmentError("Please set the GOOGLE_API_KEY in your environment variables.")

    def analyze_image_with_genai(self, image):
        """Analyze the drawn image using the AI model."""
        # Convert the image to RGB format and prepare it for AI analysis
        imgCanvas = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        imgCanvas = PIL.Image.fromarray(imgCanvas)

        # Configure the AI model with API key
        genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
        model = genai.GenerativeModel(model_name='gemini-1.5-flash')

        # Define the prompt to send to the model
        prompt = ("Analyze the image and provide the following:\n"
                  "* The mathematical equation represented in the image.\n"
                  "* The solution to the equation.\n"
                  "* A short and sweet explanation of the steps taken to arrive at the solution.\n")

        # Request the model to generate content based on the prompt
        response = model.generate_content([prompt, imgCanvas])
        return response.text

    def main(self):
        """Main method to render UI and handle interactions."""
        # Layout with two columns
        col1, col2 = st.columns([3, 1])

        with col1:
            # Draw equation on the canvas
            #st.markdown("### Draw your equation here:")
            stroke_color = st.color_picker("Pick a pen color:", "#FFFFFF")
            canvas_result = st_canvas(
                fill_color="rgba(255, 255, 255, 0.3)",
                stroke_width=4,
                stroke_color=stroke_color,
                background_color="#333333",
                height=500,
                width=1000,
                drawing_mode="freedraw",
                key="canvas",
                display_toolbar=True  # Set to True to show the toolbar, or False to hide it
            )

        with col2:
            # Output section
            st.markdown("### Output:")
            result_placeholder = st.empty()
            
            # Button to trigger analysis
            if st.button("Analyze Equation"):
                if canvas_result.image_data is not None:
                    with st.spinner("Analyzing your equation..."):
                        result = self.analyze_image_with_genai(canvas_result.image_data)
                        result_placeholder.write(f"### Result:\n\n{result}")
                else:
                    st.warning("Please draw an equation on the canvas before analyzing.")
            
# Initialize and run the calculator
try:
    calc = Calculator()
    calc.streamlit_config()
    calc.main()
except Exception as e:
    add_vertical_space(5)
    st.markdown(f'<h5 style="text-align:center;color:orange;">{e}</h5>', unsafe_allow_html=True)
