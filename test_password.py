from jawaban_mahasiswa import validasi_password

def test_validasi_sukses():
    assert validasi_password("PasswordKuat123!") == True
    assert validasi_password("P@ssw0rd") == True

def test_validasi_gagal():
    assert validasi_password("lemah") == False 
    assert validasi_password("TanpaAngka!") == False
    assert validasi_password("TanpaSimbol123") == False
    assert validasi_password("Ada Spasi123!") == False

def test_validasi_big_o():
    # Membuat password valid dengan panjang 50.000 karakter
    # Contoh: "AAAAA..." (sebanyak 49.997 kali) + "1!b"
    password_panjang = "A" * 49997 + "1!b"
    assert validasi_password(password_panjang) == True
