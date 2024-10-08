import sys
import re
import os
from backend.src.parser_generic import MedicalDocParser

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)
        
    def parse(self):
        return {
            'patient_name': self.get_field('patient_name'),
            'patient_address': self.get_field('patient_address'),
            'medicines': self.get_field('medicines'),
            'directions': self.get_field('directions'),
            'refills': self.get_field('refills')
        }


    def get_field(self, field_name):
        pattern = ''
        flags = None

        pattern_dict = {
            'patient_name': {'pattern': r'Name:(.*)Date', 'flags': 0},
            'patient_address': {'pattern': r'Address:(.*)\n', 'flags': 0},
            'medicines': {'pattern': r'Address:[^\n]*(.*)Directions:', 'flags': re.DOTALL},
            'directions': {'pattern': r'Directions:\s*(.*?)\s*Refill:', 'flags': re.DOTALL},
            'refills': {'pattern': r'Refill:(.*)', 'flags': 0}
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
            if len(matches) > 0:
                return matches[0].strip()


if __name__ == '__main__':

    document_text = '''
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

K

Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mig every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times

'''



    pp = PrescriptionParser(document_text)
    print(pp.parse())
