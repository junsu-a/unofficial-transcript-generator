import os
import logging
import pdfplumber

async def extract_text_from_pdf(file):
    # Save the uploaded file temporarily
    temp_filename = "temp.pdf"
    with open(temp_filename, "wb") as buffer:
        buffer.write(await file.read())

    # Extract text from the PDF using pdfplumber
    with pdfplumber.open(temp_filename) as pdf:
        pages = [page.extract_text() for page in pdf.pages]

    # Remove the temporary file
    os.remove(temp_filename)

    return pages
