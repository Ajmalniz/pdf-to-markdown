# PDF to Markdown Converter

A simple web application to convert PDF files (including scanned/image-based PDFs) to Markdown format using Streamlit. Supports both text-based and image-based (OCR) PDFs.

## Features
- Upload and convert PDF files to Markdown
- Supports both text-based and scanned/image-based PDFs
- Optional OCR (Optical Character Recognition) for image-based PDFs
- Markdown preview and download link
- Easy-to-use web interface powered by Streamlit

## Demo
![Demo Screenshot](demo_screenshot.png) <!-- Add a screenshot if available -->

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/pdf-to-markdown.git
   cd pdf-to-markdown
   ```

2. **Install dependencies:**
   You can use `pip` or a tool like `uv` (if you prefer fast installs):
   ```bash
   pip install -r requirement.txt
   ```
   Or, if using `uv`:
   ```bash
   uv pip install -r requirement.txt
   ```

   Ensure you have [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system for OCR functionality.

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## Requirements
- Python 3.7+
- streamlit
- pdfplumber
- markdown2
- pytesseract
- Pillow
- PyMuPDF (fitz)

See `requirement.txt` for the full list.

## Usage
1. Open the app in your browser (Streamlit will provide a local URL).
2. Upload a PDF file using the uploader.
3. (Optional) Enable the OCR checkbox for scanned/image-based PDFs.
4. View the Markdown preview and download the result.

## Notes
- For best OCR results, ensure Tesseract is installed and available in your system PATH.
- Large or complex PDFs may take longer to process, especially with OCR enabled.

## License
MIT License

## Acknowledgements
- [Streamlit](https://streamlit.io/)
- [pdfplumber](https://github.com/jsvine/pdfplumber)
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF)
- [pytesseract](https://github.com/madmaze/pytesseract)
- [markdown2](https://github.com/trentm/python-markdown2)
- [Pillow](https://python-pillow.org/)
