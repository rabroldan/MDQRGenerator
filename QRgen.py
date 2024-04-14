"""
This module contains a flask application which serves as an entry point to launch the application.
It contains functions for uploading and downloading files.
"""

from flask import Flask, render_template, request, jsonify, send_file
import os
import sys
from persistence import is_pdf, generate_qrcode, save_qrcode_as_pdf, save_text, save_text_as_pdf
from extractor import extract_text_from_pdf, extract_text_from_image

VERSION = "0.1"  # current version of the tool

app = Flask(__name__)

# Define the folder where you want to save the uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def upload_image():
    """
    This function enables user to upload an image from which text will be extracted for QR-code.
    :return: HTML template or json file.
    """
    if request.method == "POST":
        # Check if the POST request has the file part
        if "file" not in request.files:
            return jsonify({"Error": "File is not supported"})

        file = request.files["file"]

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == "":
            return jsonify({"Error": "No selected file"})

        if file:
            # Save the File into the uploads folder
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            # Read the uploaded image directly from the file path
            if is_pdf(file_path):  # Check if file_path is a pdf file
                extracted_text = extract_text_from_pdf(file_path)
            else:
                extracted_text = extract_text_from_image(file_path)

            if len(extracted_text.strip()) == 0:
                # Text content could not be extracted from the image file.
                return jsonify({"Error": "Text extraction failed", "message": f"Text could not be extracted from {file.filename}."})

            # Create a folder named "qr" if it doesn't exist within "uploads"
            qr_folder = os.path.join('qr')
            os.makedirs(qr_folder, exist_ok=True)
            # Create file path for QR code image
            qr_image_path = os.path.join(qr_folder, 'qr_code.png')
            # Generate QR code from extracted text and save QR code image in the "qr" folder
            qr_code_data = generate_qrcode(extracted_text, qr_image_path)
            # Create file path for pdf file containing qr code image
            qr_pdf_path = os.path.join(qr_folder, 'qr_code.pdf')
            # Save qr-code image as as pdf
            save_qrcode_as_pdf(qr_image_path, qr_pdf_path, 'Seneca Polytechnic - PRJ666 Project', width=110)
            # Create file path for pdf file containing extracted text
            extracted_text_pdf_path = os.path.join(qr_folder, 'extracted_text.pdf')
            save_text_as_pdf(extracted_text, extracted_text_pdf_path)
            # Create file path for pdf file containing extracted text
            extracted_text_txt_path = os.path.join(qr_folder, 'extracted_text.txt')
            save_text(extracted_text, extracted_text_txt_path)

            return jsonify({"extracted_text": extracted_text, "qr_code_data": qr_code_data})
 
    return render_template("upload_image.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    # Render the about.html template
    return render_template('about.html')

@app.route("/difference", methods=["GET", "POST"])
def difference():
    # Render the difference.html template
    return render_template('difference.html')
@app.route("/howto", methods=["GET", "POST"])
def howto():
    # Render the howto.html template
    return render_template('howto.html')
@app.route("/download_pdf")
def download_pdf():
    """This function contains an app route for downloading qr-code image as pdf file."""
    qr_image_path = os.path.join("qr", 'qr_code.pdf')
    return send_file(qr_image_path, as_attachment=True)


@app.route("/download_image")
def download_image():
    """This function contains an app route for downloading qr-code image."""
    qr_image_path = os.path.join("qr", 'qr_code.png')
    return send_file(qr_image_path, as_attachment=True)


@app.route("/download_text")
def download_text():
    """This function contains an app route for downloading extracted text as text file"""
    qr_image_path = os.path.join("qr", 'extracted_text.txt')
    return send_file(qr_image_path, as_attachment=True)


@app.route("/download_text_pdf")
def download_text_pdf():
    """This function contains an app route for downloading extracted text as pdf file"""
    qr_image_path = os.path.join("qr", 'extracted_text.pdf')
    return send_file(qr_image_path, as_attachment=True)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-h', '-help', '--help', '--h']:
            # Display help message
            print("COMING SOON")
        elif sys.argv[1] in ['-v', '-version', '--version', '--v']:
            # Display version
            print(VERSION)  # Replace with your actual version
    else:
        app.run(debug=True)
