# Write your code here

import re

def is_valid_password(string):

    # At least 12 characters long
    if re.fullmatch(".{,11}",string):
        return False
    
    # At least one digit
    if not re.search("[0-9]",string):
        return False
    
    # At least one lowercase letter
    if not re.search("[a-z]",string):
        return False
    
    #At least one uppercase letter
    if not re.search("[A-Z]",string):
        return False
    
    # At least one special character
    if not re.search(r"[\+\-\*/\.@]",string):
        return False
    
    # Not three characters in a row
    if re.search(r"(.)\1{2}",string):
        return False
    
    # Not four times the same character
    if re.search(r".*(.).*\1.*\1.*\1.*",string):
        return False

    return True


print(is_valid_password("Aaabcadefgahthpoyli2+"))