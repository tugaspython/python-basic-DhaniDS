	import re
	
	def validasi_password(password):
	# Cek batas panjang karakter
	if len(password) < 8 or len(password) > 20: 
return False
	   
	# Satu pola Regex untuk mengecek huruf besar, angka, simbol, dan tanpa spasi
	pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[^ ]+$"
	return bool(re.match(pattern, password))
