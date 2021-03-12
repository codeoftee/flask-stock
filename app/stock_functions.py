import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def is_valid_email(email):
    if re.search(regex, email):
        return True
    else:
        return False

# https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
