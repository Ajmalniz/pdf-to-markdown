import streamlit as st
import pdfplumber
import markdown2
from io import StringIO, BytesIO
import pytesseract
from PIL import Image
import fitz  # PyMuPDF for OCR
import base64
import os

# Function to extract text from text-based PDF
def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n\n"
    return text

# Function to extract text from scanned/image-based PDF using OCR
def extract_text_from_image_pdf(pdf_file):
    text = ""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page in doc:
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.rgb)
        page_text = pytesseract.image_to_string(img)
        text += page_text + "\n\n"
    doc.close()
    return text

# Function to convert text to Markdown
def text_to_markdown(text):
    lines = text.split("\n")
    markdown = ""
    for line in lines:
        if line.strip():
            markdown += f"{line.strip()}\n\n"
    return markdown2.markdown(markdown)

# Function to create a downloadable Markdown file
def get_markdown_download_link(markdown_text, filename="output.md"):
    buffer = BytesIO()
    buffer.write(markdown_text.encode("utf-8"))
    buffer.seek(0)
    b64 = base64.b64encode(buffer.read()).decode()
    href = f'<a href="data:text/markdown;base64,{b64}" download="{filename}">Download {filename}</a>'
    return href

# Streamlit app
st.title("PDF to Markdown Converter")
st.write("Upload a PDF file to convert it to Markdown.")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

# Option to enable OCR for scanned PDFs
use_ocr = st.checkbox("Use OCR (for scanned or image-based PDFs)")

if uploaded_file is not None:
    # Read the uploaded file
    file_name = uploaded_file.name
    st.write(f"Processing: {file_name}")

    try:
        # Extract text based on OCR selection
        if use_ocr:
            st.info("Performing OCR on the PDF. This may take a moment...")
            text = extract_text_from_image_pdf(uploaded_file)
        else:
            text = extract_text(uploaded_file)

        if text.strip():
            # Convert to Markdown
            markdown = text_to_markdown(text)

            # Display Markdown preview
            st.subheader("Markdown Preview")
            st.markdown(markdown)

            # Provide download link
            st.subheader("Download Markdown")
            output_filename = os.path.splitext(file_name)[0] + ".md"
            st.markdown(get_markdown_download_link(markdown, output_filename), unsafe_allow_html=True)
        else:
            st.error("No text could be extracted from the PDF. If it's a scanned document, try enabling OCR.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
else:
    st.info("Please upload a PDF file to begin.")