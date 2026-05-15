import os
import requests
import json

# ==============================================================================
# BAGIAN KONFIGURASI - MOHON ISI BAGIAN INI DENGAN DATA ANDA
# ==============================================================================

# 1. URL Moodle, ID Kursus, dan ID Tugas
MOODLE_URL = "http://3.27.152.91/moodle"
COURSE_ID = 2
ASSIGNMENT_ID = 2

# 2. Pemetaan Manual dari Username GitHub ke Email yang Terdaftar di Moodle
GITHUB_TO_EMAIL_MAP = {
    "DhaniDS": "fastgoole@gmail.com",
    "dhanidds": "localhouse2402@gmail.com",
    "dhans24": "dhanidwinawans12@gmail.com",
    "iccanfly": "iccanfly@gmail.com",
    "mahasiswa4": "ican88030@gmail.com",
    "mahasiswa5": "icann1400@gmail.com",
}

# ==============================================================================
# FUNGSI TAMBAHAN: ANALISIS KOMPLEKSITAS (RADON)
# ==============================================================================

def get_complexity_feedback(filepath="complexity.json"):
    """Membaca file JSON dari Radon dan mengembalikan string umpan balik."""
    if not os.path.exists(filepath):
        return "\n⚠️ Catatan: Analisis kualitas kode (Radon) tidak tersedia."

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            
        feedback_lines = ["\n--- Analisis Kualitas Kode (Cyclomatic Complexity) ---"]
        
        for filename, blocks in data.items():
            if not isinstance(blocks, list): 
                continue
                
            for block in blocks:
                tipe = block.get('type', 'block')
                nama = block.get('name', 'unknown')
                skor_cc = block.get('complexity', 1)
                grade = block.get('rank', 'A')
                
                feedback_lines.append(f"- {tipe.capitalize()} '{nama}': Grade {grade} (Skor CC: {skor_cc})")
        
        if len(feedback_lines) == 1:
            feedback_lines.append("- Semua blok kode memiliki efisiensi yang sangat baik (Grade A).")
            
        return "\n".join(feedback_lines)

    except Exception as e:
        return f"\n[Peringatan] Gagal memproses data kompleksitas: {str(e)}"

# ==============================================================================
# BAGIAN LOGIKA SKRIP
# ==============================================================================

# --- Langkah 1: Ambil Variabel dari GitHub Actions Environment ---
MOODLE_TOKEN = os.environ.get('MOODLE_TOKEN')
GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME')

if not MOODLE_TOKEN or not GITHUB_USERNAME:
    print("❌ Error: Variabel MOODLE_TOKEN atau GITHUB_USERNAME tidak ditemukan.")
    exit(1)

# --- Langkah 2: Hitung Nilai dari Hasil Tes (Pytest) ---
grade = 0
pytest_feedback = ""
TOTAL_SOAL = 20

try:
    with open('report.json') as f:
        report = json.load(f)
    
    passed_tests = report['summary'].get('passed', 0)
    failed_tests = TOTAL_SOAL - passed_tests
    grade = (passed_tests / TOTAL_SOAL) * 100
    
    pytest_feedback = f"Hasil Tes Otomatis:\n- Total Soal: {TOTAL_SOAL}\n- Benar: {passed_tests}\n- Salah/Gagal: {failed_tests}\n\nNilai Fungsional: {grade:.2f} / 100"
    print(f"✅ Berhasil menghitung nilai: {grade}")

except FileNotFoundError:
    grade = 0
    pytest_feedback = f"Gagal menjalankan tes. File `report.json` tidak ditemukan. Nilai: 0.00"
    print("⚠️ Warning: File report.json tidak ditemukan.")
except Exception as e:
    grade = 0
    pytest_feedback = f"Terjadi error saat memproses hasil tes: {e}"

# --- Langkah baru: Ambil Analisis Kompleksitas (Radon) ---
radon_feedback = get_complexity_feedback('complexity.json')

# GABUNGKAN SEMUA FEEDBACK
final_feedback = f"{pytest_feedback}\n{radon_feedback}"

# --- Langkah 3: Cari User Moodle Berdasarkan Email ---
moodle_email = GITHUB_TO_EMAIL_MAP.get(GITHUB_USERNAME)

if not moodle_email:
    print(f"❌ Error: Username GitHub '{GITHUB_USERNAME}' tidak terdaftar.")
    exit(1)

search_params = {
    'wstoken': MOODLE_TOKEN,
    'wsfunction': 'core_user_get_users',
    'moodlewsrestformat': 'json',
    'criteria[0][key]': 'email',
    'criteria[0][value]': moodle_email
}

user_id = None 
try:
    response = requests.get(f"{MOODLE_URL}/webservice/rest/server.php", params=search_params)
    users = response.json().get('users', [])
    if not users:
        print(f"❌ Error: Email '{moodle_email}' tidak ditemukan di Moodle.")
        exit(1)
    user_id = users[0]['id'] 
    print(f"✅ User ID ditemukan: {user_id}")
except Exception as e:
    print(f"❌ Error saat mencari user: {e}")
    exit(1)

# --- Langkah 4: Kirim Nilai dan Gabungan Feedback ke Moodle ---
if user_id: 
    grade_params = {
        'wstoken': MOODLE_TOKEN,
        'wsfunction': 'mod_assign_save_grade',
        'moodlewsrestformat': 'json',
        'assignmentid': ASSIGNMENT_ID,
        'userid': user_id, 
        'grade': grade,
        'attemptnumber': -1,
        'addattempt': 0,
        'workflowstate': 'graded',
        'applytoall': 1,
        'plugindata[assignfeedbackcomments_editor][text]': final_feedback,
        'plugindata[assignfeedbackcomments_editor][format]': 1
    }

    try:
        response = requests.post(f"{MOODLE_URL}/webservice/rest/server.php", params=grade_params)
        
        print("\n--- BUKTI INTEGRASI API MOODLE ---")
        print(f"Status Code HTTP: {response.status_code}")
        print(f"Balasan Server: {response.text}")
        print("----------------------------------\n")
        
        # Simpan respons JSON ke dalam variabel
        json_response = response.json()
        
        # Cek apakah balasan berupa dictionary (objek) DAN memiliki kata 'exception'
        if isinstance(json_response, dict) and 'exception' in json_response:
            print(f"❌ Error API: {json_response}")
        else:
            # Jika balasan null atau tidak ada exception, berarti sukses!
            print("✅ SUKSES! Nilai dan analisis kualitas kode berhasil dikirim ke Moodle.")

    except Exception as e:
        print(f"❌ Error saat mengirim data: {e}")
