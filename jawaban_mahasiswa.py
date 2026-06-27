import re

def validasi_password(password):
    # Cek batas panjang karakter (minimal 8)
    if len(password) < 8: 
        return False
        
    # Regex yang lebih dinamis:
    # (?=.*[^A-Za-z0-9 ]) memastikan ada minimal 1 simbol apa saja (termasuk @, !, _, dll)
    pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9 ])[^ ]+$"
    return bool(re.match(pattern, password))
