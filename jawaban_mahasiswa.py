def validasi_password(password):
    if len(password) < 8:
        return False
    
    # Pendekatan O(N): Hanya butuh 1 kali perulangan (Single Pass)
    if ' ' in password: # in pada string adalah O(N)
        return False

    ada_angka = False
    ada_simbol = False
    ada_huruf_besar = False

    for char in password:
        if char.isdigit(): ada_angka = True
        elif char.isupper(): ada_huruf_besar = True
        elif not char.isalnum(): ada_simbol = True

    return ada_angka and ada_simbol and ada_huruf_besar
