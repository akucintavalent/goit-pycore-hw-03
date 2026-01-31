import re

def normalize_phone(phone_number: str) -> str:
    '''
    Normalizes a phone number by removing all non-numeric characters
    and ensuring it starts with the country code '+38' (for Ukraine).
    '''

    digits = re.sub(r'\D', '', phone_number)
    
    if len(digits) == 10:
        return '+38' + digits
    elif len(digits) == 12 and digits.startswith('38'):
        return '+' + digits
    else:
        raise ValueError("Invalid phone number format.")
