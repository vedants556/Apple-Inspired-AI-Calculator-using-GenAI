# 🧮 AI Calculator Web Application

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](#)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat&label=Contributions&colorA=red&colorB=black)](#)

This project is a web application that allows users to draw mathematical equations on a whiteboard and analyze them using AI. The application utilizes Google’s Generative AI to interpret the drawn equations and provide solutions along with explanations.

## 🌟 Features

- Draw equations on a user-friendly whiteboard interface
- Analyze drawn equations using Google’s Generative AI
- Display results including the equation, solution, and explanation
- Clear the canvas for new drawings
- Responsive design for various screen sizes

## 🛠️ Technologies Used

- Python
- Streamlit
- OpenCV
- PIL (Pillow)
- NumPy
- Google Generative AI
- dotenv (for environment variable management)

## 🚀 Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/vedants556/Apple-Inspired-AI-Calculator-using-GenAI.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the project root directory and add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

4. Run the Streamlit application:
   ```
   streamlit run app.py
   ```

5. Open a web browser and navigate to `http://localhost:8501` to use the application.

## 📊 How It Works

1. Users draw mathematical equations on the whiteboard.
2. Upon clicking the "Analyze Equation" button, the application sends the drawn image to Google’s Generative AI.
3. The application displays the predicted equation, solution, and a brief explanation.
4. Users can clear the canvas to start a new drawing.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/vedants556/ai_calculator_app/issues) if you want to contribute.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Vedant Shelar
- GitHub: [@vedants556](https://github.com/vedants556)
- LinkedIn: [your-linkedin-profile](https://www.linkedin.com/in/your-linkedin-profile)

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [OpenCV](https://opencv.org/)
- [Pillow](https://python-pillow.org/)
- [Google Generative AI](https://cloud.google.com/generative-ai)

---

If you find this project useful, please consider giving it a star ⭐️ to show your support!
