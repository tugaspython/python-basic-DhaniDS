import re

def validasi_password(password):
  if len(password) < 8 or len(password) > 20: 
    return False
    
pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[^ ]+$"
return bool(re.match(pattern, password))
