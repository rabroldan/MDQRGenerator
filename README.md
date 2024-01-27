#  MDQRConverter - STILL IN PROGRESS

## Overview

This software is designed to revolutionize the way handwritten notes, prescriptions, or important documents are handled. It converts handwritten notes, company logos, and electronic prescriptions into encrypted QR codes. Not only does it provide a secure means of storing and sharing sensitive information, but it also ensures the validity and verification of key data such as the date of issue, patient details, clinician information, drug information, and more.

## Key Features

- **Data Verification**: The software thoroughly checks and validates critical information within the uploaded document, including:
  - Date of issue
  - Patient's name and address
  - Patient's date of birth
  - Clinician name, address, DEA number
  - Drug name
  - Drug strength
  - Dosage form
  - Quantity prescribed
  - Directions for use
  - Number of refills
  - Signature of the prescriber

- **Encryption**: After successful verification, the software securely encrypts all relevant information into a QR code, ensuring the highest level of data protection.

## Advantages

- **Environmental Benefits**: By converting handwritten notes to digital QR codes, this software promotes a paperless approach, reducing paper consumption and helping the environment.

- **Security**: Handwritten notes can be easily lost or misinterpreted. The encrypted QR code offers a secure and tamper-proof method of storing and transmitting sensitive information.

- **Efficiency**: This software simplifies the process of sharing prescriptions and other handwritten documents, making it more convenient for both patients and healthcare providers.

- **Accuracy**: Handwritten prescriptions are often prone to errors due to illegible handwriting. The QR code format ensures that the information is accurately transcribed and understood by pharmacists, reducing medication errors.

- **Accessibility**: Patients can easily access their prescriptions and medical information via their smartphones or tablets, making it more accessible and convenient for tracking their healthcare.

- **Streamlined Communication**: Healthcare providers and pharmacies can streamline their communication with patients, easily sharing prescriptions and important documents digitally, which saves time and resources.

## How It Works

1. **Request from Your Doctor**: Your healthcare provider will send you a text message or email containing a link to a special QR code or token, rather than providing you with a paper prescription.

2. **Visit Your Local Pharmacy**: When you need to fill your prescription, simply show the QR code on your smartphone or tablet to your neighborhood pharmacist. If your pharmacy offers home delivery, you can also share the message with them.

3. **QR Code Scanning**: The pharmacist scans the QR code, which contains all the specifics of your prescription. They can then proceed with dispensing the medication as usual.

4. **Data Security**: The encrypted QR code ensures that your prescription and sensitive medical information remain confidential and secure.

## Difference with e-Prescriptions

- **Independence from EHRs**: Unlike traditional e-prescriptions that often rely on Electronic Health Records (EHR) systems, this software offers a standalone solution. It can work seamlessly with handwritten notes, prescriptions, and any other documents, eliminating the need for EHR integration.

- **Wider Applicability**: While e-prescriptions are primarily focused on medication orders, this software can handle various handwritten documents, including handwritten notes and company logos. It's versatile and applicable in a broader range of scenarios.

- **Increased Data Security**: The encryption of data into QR codes provides an additional layer of security beyond typical e-prescription methods, ensuring the confidentiality and integrity of patient information.
It looks like you want to create a documentation section in Markdown. Here's an improved version of your documentation with better formatting:

# Library and Dependencies

Please ensure you have installed the following Python libraries and dependencies:

- To install Pillow:
  ```
  pip install pillow
  ```

- To install Flask:
  ```
  pip install flask
  ```

- To install Pytesseract:
  ```
  pip install pytesseract
  ```

- You also need to install Tesseract. For Windows, you can find installation instructions [here](https://tesseract-ocr.github.io/tessdoc/Installation.html).
- Please Ensure that you change "pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'" to the proper path of your tesseract
# Features

For now, the application will:
- Upload a document
- Read the document
- Save it into the "uploads" folder
- Display the text on the page

## To Do

In the future, you may consider implementing the following features:
- Encryption and Decryption of the uploaded files

# Running

To run the application, execute the following command in your terminal:

```
python QRgen.py
```

Make sure you have installed the required libraries and dependencies as mentioned above before running the application.
```
