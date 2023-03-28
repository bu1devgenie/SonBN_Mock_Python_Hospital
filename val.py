import re

def valid_phone(phone):
    if re.fullmatch('^\d{10}$', str(phone)):
        return True
    return False

def valid_email(email):
    if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
        return True
    return False

def file_open(fname):
    try:
        f = open(fname)
        f.close()
        return True
    except:
        return False

if __name__ == "__main__":
    pass