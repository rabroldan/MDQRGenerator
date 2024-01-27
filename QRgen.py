from flask import Flask, render_template, request, jsonify
from PIL import Image
import pytesseract
import os
import sys
import qrcode

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

VERSION = "0.1"  # current version of the tool

app = Flask(__name__)

# Define the folder where you want to save the uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        # Check if the POST request has the file part
        if "file" not in request.files:
            return jsonify({"Error": "No file is not supported"})

        file = request.files["file"]

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == "":
            return jsonify({"Error": "No selected file"})

        if file:
            # Save the File into the uploads folder
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Read the uploaded image directly from the file path
            img = Image.open(file_path)

            # Use Tesseract to extract text from the image
            extracted_text = pytesseract.image_to_string(img)

            # Generate QR code from extracted text
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(extracted_text)
            qr.make(fit=True)

            # Create a folder named "qr" if it doesn't exist within "uploads"
            qr_folder = os.path.join( 'qr')
            os.makedirs(qr_folder, exist_ok=True)

            # Save the QR code image in the "qr" folder
            qr_image_path = os.path.join(qr_folder, 'qr_code.png')
            test = qr.make_image(fill_color="black", back_color="white").save(qr_image_path)
           
            return jsonify({"extracted_text": extracted_text, "qr_image_path": qr_image_path})

    return render_template("upload_image.html")

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
