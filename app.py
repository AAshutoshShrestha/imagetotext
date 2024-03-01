import streamlit as st
from PIL import Image
import numpy as np
import easyocr as ocr

# Load OCR model asynchronously
@st.cache_data(persist=True)
def load_model(): 
    return ocr.Reader(['en'], model_storage_directory='.')

def main():
    st.title("Image Text Extractor")
    reader = load_model() # Load the OCR model

    uploaded_file = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.sidebar.image(image, caption='Uploaded Image', use_column_width=True)
        
        # Perform OCR on resized image
        text = reader.readtext(np.array(image))
        result_text = [i[1] for i in text]
        paragraph = " ".join(result_text)

        # Format extracted text
        paragraph = paragraph.replace("- ", "")
        formatted_text = paragraph.replace('. ', '. ')

        st.subheader("Extracted Text:")
        final_text=  st.text_area('final output',value=formatted_text, height=400)     
        st.code(final_text, line_numbers=False)     

if __name__ == "__main__":
    main()
