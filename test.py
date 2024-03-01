import streamlit as st
import pytesseract
from PIL import Image
import clipboard

# Set Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def main():
    st.sidebar.title("Image Text Extractor")
    
    uploaded_file = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.sidebar.image(image, caption='Uploaded Image', use_column_width=True)

        text = pytesseract.image_to_string(image)
        st.subheader("Extracted Text:")

        # Remove leading and trailing whitespaces
        text = text.strip()
        text = ' '.join(text.split())
        text = text.replace("- ", "")
        text = text.replace('\n', '')
        formatted_text = text.replace('. ', '. ')

        final_text=st.text_area('Final formated outbut ',value=formatted_text, height=400)     
        
        # Add a "Copy Text" button
        if st.button('Copy text'):
            clipboard.copy(final_text)
            st.success('Text copied successfully!')



if __name__ == "__main__":
    main()