def validasi_password(password):
    if len(password) < 8:
        return False

    # Kesalahan fatal: Menggunakan nested loop O(N^2)
    # Mengecek apakah ada spasi dengan membandingkan semua karakter satu per satu
    for i in range(len(password)):
        for j in range(len(password)):
            if password[j] == ' ':
                return False

    ada_angka = False
    ada_simbol = False
    ada_huruf_besar = False

    for char in password:
        if char.isdigit(): ada_angka = True
        elif char.isupper(): ada_huruf_besar = True
        elif not char.isalnum(): ada_simbol = True

    return ada_angka and ada_simbol and ada_huruf_besar
