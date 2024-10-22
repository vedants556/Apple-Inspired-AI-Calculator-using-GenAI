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

filterwarnings(action='ignore')

class Calculator:

    def streamlit_config(self):
        st.set_page_config(page_title='AI Calculator', layout="wide")
        page_background_color = """
        <style>
        [data-testid="stHeader"] {
            background: rgba(0,0,0,0);
        }
        .block-container {
            padding-top: 0rem;
        }
        </style>
        """
        st.markdown(page_background_color, unsafe_allow_html=True)
        st.markdown(f'<h1 style="text-align: center; color: #ff0000;">AI Calculator</h1>',
                    unsafe_allow_html=True)
        add_vertical_space(1)

    def __init__(self):
        load_dotenv()
        if 'GOOGLE_API_KEY' not in os.environ:
            raise EnvironmentError("Please set the GOOGLE_API_KEY in your environment variables.")

    def analyze_image_with_genai(self, image):
        imgCanvas = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        imgCanvas = PIL.Image.fromarray(imgCanvas)
        genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
        model = genai.GenerativeModel(model_name='gemini-1.5-flash')

        prompt = ("Analyze the image and provide the following:\n"
                  "* The mathematical equation represented in the image.\n"
                  "* The solution to the equation.\n"
                  "* A short and sweet explanation of the steps taken to arrive at the solution.\n")

        response = model.generate_content([prompt, imgCanvas])
        return response.text

    def main(self):
        col1, _, col3 = st.columns([0.8, 0.02, 0.18])

        with col1:
            stroke_color = st.color_picker("Pick a pen color:", "#FFFFFF")
            canvas_result = st_canvas(
                fill_color="rgba(255, 255, 255, 0.3)",
                stroke_width=2,
                stroke_color=stroke_color,
                background_color="#000000",
                height=550,
                width=950,
                drawing_mode="freedraw",
                key="canvas",
            )

        with col3:
            st.markdown(f'<h5 style="text-align:center;color:green;">OUTPUT:</h5>', unsafe_allow_html=True)
            result_placeholder = st.empty()

            if st.button("Analyze Equation"):
                if canvas_result.image_data is not None:
                    result = self.analyze_image_with_genai(canvas_result.image_data)
                    result_placeholder.write(f"Result: {result}")
                else:
                    st.warning("Please draw an equation before analyzing.")

try:
    calc = Calculator()
    calc.streamlit_config()
    calc.main()
except Exception as e:
    add_vertical_space(5)
    st.markdown(f'<h5 style="text-align:center;color:orange;">{e}</h5>', unsafe_allow_html=True)
