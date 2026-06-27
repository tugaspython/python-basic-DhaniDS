# File: test_password.py
from jawaban_mahasiswa import validasi_password

def test_validasi_sukses():
    assert validasi_password("PasswordKuat123!") == True
    assert validasi_password("P@ssw0rd") == True

def test_validasi_gagal():
    assert validasi_password("lemah") == False # Kependekan
    assert validasi_password("TanpaAngka!") == False
    assert validasi_password("TanpaSimbol123") == False
    assert validasi_password("Ada Spasi123!") == False
