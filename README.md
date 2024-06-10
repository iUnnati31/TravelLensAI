# TravelVisionAI 🍽️🔍

Welcome to **TravelVisionAI**, an interactive travel guide that leverages the power of Google Gemini for image recognition and Streamlit for a user-friendly interface. This project allows users to upload photos of landmarks or tourist spots and receive detailed information and recommendations.

## Features

- Upload photos of landmarks or tourist spots
- Receive detailed information and historical facts
- Get recommendations for nearby attractions and activities
- User-friendly interface built with Streamlit
- Powered by Google Gemini for accurate image recognition

## Project Structure

The project structure is organized as follows:
```
travel-guide-app/
│
├── README.md
├── requirements.txt
├── app.py
├── output.png
├── LICENSE
```

## Getting Started

1. Clone this repository to your local machine:
```
git clone https://github.com/iUnnati31/TravelVisionAI.git
```
2. Install the Python dependencies:
```
pip install -r requirements.txt
```
3. Set up your Google API key:

- Visit the Google Cloud Console.
- Create a new project or select an existing one.
- Enable the Google Generative AI (Gemini) API.
- Create an API key and save it securely.

4. Update the `.env` file with your Google API key:
```
GOOGLE_API_KEY=your-api-key-here

```

5. Run the Streamlit app:
```
streamlit run app.py
```

6. Access the app in your browser at `http://localhost:8501`.

## License

This project is licensed under the terms of the [MIT License](LICENSE).

## Acknowledgments

- The project utilizes the Google Generative AI models for anime character chat and image recognition.
- Special thanks to the contributors of Streamlit for providing an excellent framework for building interactive web applications.