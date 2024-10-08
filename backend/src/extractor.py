import util
import pytesseract
from pdf2image import convert_from_path
from parser_prescription import PrescriptionParser
from parser_patient_details import PatientDetailsParser

POPPLER_PATH = 'C:/poppler-24.07.0/Library/bin'
pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'



def extract(file_path, file_format):
    #step 1: extracting text from pdf file
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''

    if len(pages) > 0:
        page = pages[0]
        processed_image = util.preprocess_image(page)  
        text = pytesseract.image_to_string(processed_image, lang = 'eng')      
        document_text = '\n' + text


    # Step 2: extract fields from text
    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse()
    elif file_format == 'patient_details':
        extracted_data = PatientDetailsParser(document_text).parse()
    else:
        raise Exception(f"Invalid Document Format: {file_format}")


    return extracted_data


        

if __name__ == "__main__":
    file_path = "../resources/patient_details/pd_1.pdf"
    data = extract(file_path, 'patient_details')
    print(data)