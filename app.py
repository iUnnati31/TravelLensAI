## travel guide that allows users to upload photos of landmarks or tourist spots and receive detailed information and recommendations.
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Pro Vision API And get response

def get_gemini_repsonse(image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app

st.set_page_config(page_title="INTERACTIVE TRAVEL GUIDE")

st.header("INTERACTIVE TRAVEL GUIDE")

uploaded_file = st.file_uploader("Upload a photo of a landmark or tourist spot...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("IDENTIFY LANDMARK")


input_prompt="""
### Landmark Information

You are a tour guide who specializes in this landmark or tourist spot. Describe its:

- # **History**: The historical background of the landmark.
- # **Significance**: Why is this landmark important or famous?
- # **Interesting Facts**: Any fascinating or unique aspects of the landmark.
- # **Recommendations**: Suggestions for visitors, such as best times to visit, nearby attractions, etc.
- # **Food suggestions**: Suggestions for visitors, such as best food to have, best places to have food, etc.
"""

## If submit button is clicked

if submit:
    if image is None:
        st.warning("Please upload an image.")
    else:
        try:
            image_data = input_image_setup(uploaded_file)
            response = get_gemini_repsonse(image_data, input_prompt)
            st.subheader("Landmark Information")
            st.write(response)
        except FileNotFoundError as e:
            st.error(str(e))
