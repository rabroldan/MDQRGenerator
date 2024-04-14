"""
This module contains functions for extracting texts from images and pdf files.
"""

import os
from PIL import Image
from PyPDF2 import PdfReader
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\peace\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def _extract_text_from_image_in_pdf(pdf_page):
    """
    Utility function to extract text from images in a pdf file page.
    :param pdf_page: PyPDF2._page.PageObject
    :return: Extracted text
    """
    # Temporary file name. The file will we removed before the function returns
    image_file_name = '__extracted_pdf_image_file.png'

    # List to store texts from each page
    results = []
    try:
        # Loop over each image in pdf_page
        for image_file_object in pdf_page.images:
            with open(image_file_name, "wb") as fp:
                # Temporarily save the image. Current file overwrites the previous one
                fp.write(image_file_object.data)
                # Extract text from the image
                extracted_text = extract_text_from_image(image_file_name)
                # store extracted text
                results.append(extracted_text)
    except Exception as e:
        print(f'_extract_text_from_image_in_pdf encountered error: {str(e)}')

    # Remove temporary image file
    if os.path.exists(image_file_name):
        os.remove(image_file_name)
    return ' '.join(results).strip()


def extract_text_from_pdf(pdf_file_path):
    """
    This function extracts text from a pdf file.
    If a page contains both text and image, text will be extracted first before
    extracting text from the image.
    :param pdf_file_path: Name of pdf file from which text will be extracted.
    :return: extracted text or empty str if there is an error.
    """
    try:
        with open(pdf_file_path, 'rb') as file:
            # Create reader object
            reader = PdfReader(file)
            # List to store texts from each page
            results = []
            # Loop over each page in the pdf file
            for i in range(0, len(reader.pages)):
                # Get current page
                current_page = reader.pages[i]
                # Extract text from the page
                texts = current_page.extract_text()
                results.append(texts)
                # Extract text from the image(s) on the page
                texts = _extract_text_from_image_in_pdf(current_page)
                results.append(texts)
            return ' '.join(results).strip()
    except Exception as e:
        print(f'extract_text_from_pdf function extract_text_from_pdf encountered error: {str(e)}')
        return ''


def extract_text_from_image(file_path):
    """
    This function extracts text from an image file.
    :param file_path: image file from which texts will be extracted.
    :return: Extracted text or an empty string if the function throws an error.
    """
    try:
        img = Image.open(file_path)
        extracted_text = pytesseract.image_to_string(img)
        return extracted_text
    except Exception as e:
        print(f'extract_text_from_image function encountered error: {str(e)}')
        return ''



