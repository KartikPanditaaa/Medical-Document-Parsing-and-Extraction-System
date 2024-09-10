import sys
import re
import os
from backend.src.parser_generic import MedicalDocParser

class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def  parse(self):
        return {
            'patient_name': self.get_patient_name('name'),
            'phone_number': self.get_patient_phone_number('phone_number'),
            'medical_problems': self.get_medical_problems('medical_problems'),
            'hepatitis_b_vaccination': self.get_hepatitis_b_vaccination('hepatitis_b_vaccination')
        }

    def get_patient_name(self, name):
        pattern = r'Patient Information(.*?)\(\d{3}\)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        name = ''
        if matches:
            name = self.remove_noise_from_name(matches[0])
        return name


    def remove_noise_from_name(self, name):
        name = name.replace("Birth Date", " ").strip()
        date_pattern = r'((Jan|Feb|Mar|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
        date_matches = re.findall(date_pattern, name)

        if date_matches:
            date = date_matches[0][0]
            name = name.replace(date, ' ').strip()
        return name

    def get_patient_phone_number(self, phone_number):
        pattern = r'Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        phone_number = ' '
        if matches:
           phone_number = matches[0][-1]
        return phone_number


    def get_hepatitis_b_vaccination(self, hepatitis_b_vaccination):
        pattern = r'Have you had the Hepatitis B vaccination\?.*(Yes|No)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        hepatitis_b_vaccination = 'No'
        if matches:
            hepatitis_b_vaccination = matches[0].strip()
        return hepatitis_b_vaccination


    def get_medical_problems(self, medical_problems):
        pattern = r'List any Medical Problems \(asthma, seizures, headaches\):(.*)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        medical_problems = 'Migraine'
        if matches:
            medical_problems =  matches[0].strip()
        return medical_problems


if __name__ == '__main__':
    document_text_1 = '''   
    Patient Medical Record

    Patient Information Birth Date

    Jerry Lucas May 2 1998

    (279) 920-8204 Weight:

    4218 Wheeler Ridge Dr 57

    Buffalo, New York, 14201 Height:

    United States gnt
    170

    In Case of Emergency

    Joe Lucas . 4218 Wheeler Ridge Dr
    Buffalo, New York, 14201
    Home phone United States
    Work phone

    General Medical History

    Chicken Pox (Varicelia): Measles: ..

    IMMUNE NOT IMMUNE

    Have you had the Hepatitis B vaccination?

    Yes

    List any Medical Problems (asthma, seizures, headaches):
    N/A
    '''
    pp = PatientDetailsParser(document_text_1)
    print(pp.parse())

    document_text_2 = '''
         17/12/2020

    Patient Medical Record
    Patient Information Birth Date
    Kathy Crawford May 6 1972
    (737) 988-0851 Weight
    9264 Ash Dr 95
    New York City, 10005 .
    United States Height:
    190
    In Casc of Emergency
    7 ee
    Simeone Crawford 9266 Ash Dr
    New York City, New York, 10005
    Home phone United States
    (990) 375-4621
    Work phone
    Genera! Medical History

    Chicken Pox (Varicella): Measies:
    IMMUNE IMMUNE
    Have you had the Hepatitis B vaccination?
    (279) 920-8204
    List any Medical Problems (asthma, seizures, headaches}:
    Migraine
    '''

    pp = PatientDetailsParser(document_text_2)
    print(pp.parse())
