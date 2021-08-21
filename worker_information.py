import re

class Worker_information:
    def __init__(self, name):
        self.name = name
        self.company_name = None
        self.email = None
        self.phone_number = None

    def set_compagny_name(self, compagny_name):
        self.company_name = compagny_name

    def set_email(self, email):
        self.email = email

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_compagny_name(self):
        return self.company_name
    def get_phone_number(self):
        return self.phone_number


def isAnEmail(email):
    x = re.search("^([a-zA-Z0-9]+(([\.\-\_]?[a-zA-Z0-9]+)+)?)\@(([a-zA-Z0-9]+[\.\-\_])+[a-zA-Z]{2,4})$", email)
    if (x != None):
        return True
    return False

def isPhoneNumber(phoneNumber):
    phoneNumber = phoneNumber.replace(" ", "")
    if(len(phoneNumber) == 10):
        return True
    return False
