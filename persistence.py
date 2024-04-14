""" This module provides functions to save extracted text in various formats.
It also includes some utility functions
"""
import base64
import qrcode
from fpdf import FPDF


class PDF(FPDF):
    """
    Class to create pdf file from the scratch.
    """

    def __init__(self, header_title=""):
        super().__init__('P', 'mm', 'Letter')
        self.header_title = header_title
        # Set auto page break
        self.set_auto_page_break(auto=True, margin=15)
        # Add a page
        self.add_page()
        self.used_height = 0

    def header(self):
        """# page header. This function displays header title."""
        # set font
        self.set_font('times', 'B', 20)
        # Calculate width of title and position
        title_width = self.get_string_width(self.header_title)
        document_width = self.w
        self.set_x((document_width - title_width) / 2)
        # set title
        self.cell(title_width, 10, self.header_title, ln=1, align='C')
        # set line break
        self.ln(10)

    def footer(self):
        """page footer. This function displays page number."""
        # Set position of the footer
        self.set_y(-15)
        # Set font
        self.set_font('times', 'I', 10)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')


def save_qrcode_as_pdf(input_image_file, output_file_name, file_title="", width=None):
    """
    This function saves qr-code in a pdf file.
    :param input_image_file: qr-code image file.
    :param output_file_name: name of output file.
    :param file_title: File header.
    :param width: width of the image
    """
    try:
        pdf_file = PDF(file_title)
        if width:
            pdf_file.image(input_image_file, 50, 20, width)
        else:
            pdf_file.image(input_image_file, 50, 20, pdf_file.w - 10, )
        pdf_file.output(output_file_name)
    except Exception as e:
        print(f'save_qrcode_as_pdf encountered error. {str(e)}')
        # Create a pdf file with a plain text
        text = 'Sorry, qr-code image could not be saved.'
        save_text_as_pdf(text, output_file_name, file_header=file_title)


def save_text_as_pdf(text, output_file_name, file_header=''):
    """This function saves text into a pdf document"""
    try:
        pdf = PDF(file_header)
        pdf.set_font('times', '', 12)
        pdf.multi_cell(0, 5, text)
        pdf.output(output_file_name)
    except Exception as e:
        print(f'save_qrcode_as_pdf encountered error. {str(e)}')
        pdf = PDF(file_header)
        pdf.set_font('times', '', 12)
        pdf.multi_cell(0, 5, 'Sorry, text could not be saved.')
        pdf.output(output_file_name)


def save_text(text, output_file_name):
    """
    This function saves text into a text file
    :param text: text to be saved
    :param output_file_name: destination file
    """
    with open(output_file_name, 'w') as file:
        file.write(text)


def is_pdf(file_name):
    """ This function checks if the passed is a pdf file or not
    :param file_name: file to be checked
    :return: True if file is pdf or False if otherwise
    """
    # Check if param is str
    is_str = isinstance(file_name, str)
    if not is_str:
        return False
    dot_index = file_name.rfind('.')
    if dot_index < 0:
        return False  # It is not valid file path
    file_ext = file_name[dot_index + 1:]
    if file_ext.lower() == 'pdf':
        return True
    return False


def generate_qrcode(extracted_text, output_file_name):
    """
    This function generates qr-code from the extracted_text and saves it as an image.
    :param extracted_text: text for qr-code.
    :param output_file_name: image file name.
    :return: String of decoded bytes of the image file.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(extracted_text)
    qr.make(fit=True)
    # Save QR code
    qr.make_image(fill_color="black", back_color="white").save(output_file_name)

    # Convert the QR code image to string
    with open(output_file_name, "rb") as image2string:
        qr_code_data = base64.b64encode(image2string.read()).decode()

    return qr_code_data
