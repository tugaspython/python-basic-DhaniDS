import pytest
from kalkulator import tambah, kurang, kali, bagi

# ==========================================
# TEST UNTUK FUNGSI TAMBAH (5 Tes Mandiri)
# ==========================================
def test_tambah_positif():
    assert tambah(5, 3) == 8

def test_tambah_negatif():
    assert tambah(-5, -3) == -8

def test_tambah_campuran():
    assert tambah(5, -3) == 2

def test_tambah_nol():
    assert tambah(0, 7) == 7

def test_tambah_desimal():
    assert tambah(2.5, 3.1) == 5.6

# ==========================================
# TEST UNTUK FUNGSI KURANG (5 Tes Mandiri)
# ==========================================
def test_kurang_positif():
    assert kurang(10, 4) == 6

def test_kurang_negatif():
    assert kurang(-10, -4) == -6

def test_kurang_kecil_besar():
    assert kurang(5, 10) == -5

def test_kurang_nol():
    assert kurang(8, 0) == 8

def test_kurang_desimal():
    assert kurang(5.5, 2.2) == 3.3

# ==========================================
# TEST UNTUK FUNGSI KALI (5 Tes Mandiri)
# ==========================================
def test_kali_positif():
    assert kali(4, 5) == 20

def test_kali_campuran():
    assert kali(-4, 5) == -20

def test_kali_negatif():
    assert kali(-4, -5) == 20

def test_kali_nol():
    assert kali(7, 0) == 0

def test_kali_desimal():
    assert kali(2.5, 2.0) == 5.0

# ==========================================
# TEST UNTUK FUNGSI BAGI (5 Tes Mandiri)
# ==========================================
def test_bagi_habis():
    assert bagi(20, 4) == 5.0

def test_bagi_negatif():
    assert bagi(-20, 4) == -5.0

def test_bagi_nol_dibagi():
    assert bagi(0, 5) == 0.0

def test_bagi_desimal():
    assert bagi(5.5, 2.0) == 2.75

def test_bagi_dengan_nol():
    assert bagi(5, 0) == "Error: Pembagian dengan nol"
