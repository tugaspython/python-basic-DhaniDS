1.	# File: test_password.py
2.	from jawaban_mahasiswa import validasi_password
3.	
4.	def test_validasi_sukses():
5.	assert validasi_password("PasswordKuat123!") == True
6.	assert validasi_password("P@ssw0rd") == True
7.	
8.	def test_validasi_gagal():
9.	assert validasi_password("lemah") == False
10.	assert validasi_password("TanpaAngka!") == False
11.	assert validasi_password("TanpaSimbol123") == False
