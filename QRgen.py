from flask import Flask, render_template, request, jsonify
from PIL import Image
import pytesseract
import io
import os
import sys

VERSION = "0.1" # current version of the tool

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

            #Saves the File into the uploads folder 
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

            # Read the uploaded image
            img = Image.open(io.BytesIO(file.read()))

            # Use Tesseract to extract text from the image
            extracted_text = pytesseract.image_to_string(img)

            return jsonify({"extracted_text": extracted_text})

    return render_template("upload_image.html")

if __name__ == "__main__":

    if len(sys.argv) > 1:
  
        if sys.argv[1] == '-h' or sys.argv[1] == '-help' or sys.argv[1] == '--help' or sys.argv[1] == '--h' :
            # Display help message
            print("COMING SOON")
        elif sys.argv[1] == '-v' or sys.argv[1] == '-version' or sys.argv[1] == '--version' or sys.argv[1] == '--v':
            # Display version
            print(VERSION)  # Replace with your actual version
    else:
        app.run(debug=True)
