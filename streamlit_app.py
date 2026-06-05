import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="E-Modul Interaktif",
    page_icon="📖",
    layout="centered"
)

# 2. Navigasi Sidebar (Daftar Isi)
st.sidebar.title("📚 Daftar Isi")
menu = st.sidebar.radio(
    "Pilih Bab:",
    ["Halaman Depan", "Bab 1: Pengenalan", "Bab 2: Materi Inti", "Kuis Interaktif"]
)

# 3. Konten Berdasarkan Menu yang Dipilih
# --- HALAMAN DEPAN ---
if menu == "Halaman Depan":
    st.title("📖 E-Modul Interaktif Pemrograman Python")
    st.subheader("Selamat Datang di Modul Digital!")
    st.write("""
    Modul ini dirancang untuk membantu kamu belajar Python dengan cara yang seru dan interaktif. 
    Gunakan menu di samping kiri untuk berpindah bab.
    """)
    st.info("💡 **Tips:** Selesaikan materi secara berurutan ya!")

# --- BAB 1 ---
elif menu == "Bab 1: Pengenalan":
    st.title("Bab 1: Apa itu Python?")
    st.write("""
    **Python** adalah bahasa pemrograman tingkat tinggi yang sangat populer karena sintaksisnya yang mudah dibaca 
    dan dipahami. Python digunakan untuk berbagai hal, seperti:
    """)
    
    # Menggunakan Bullet Points
    st.markdown("- **Web Development** (Django, Flask)")
    st.markdown("- **Data Science & AI** (Pandas, TensorFlow)")
    st.markdown("- **Automasi / Scripting**")
    
    # Menambahkan File Gambar (Pastikan ada gambar bernama 'python_logo.png' di folder yang sama, atau gunakan URL)
    # st.image("https://www.python.org/static/community_logos/python-logo-master-v3-TM.png", caption="Logo Python")

# --- BAB 2 ---
elif menu == "Bab 2: Materi Inti":
    st.title("Bab 2: Variabel dan Tipe Data")
    st.write("Di dalam Python, kita bisa menyimpan data ke dalam wadah yang disebut **Variabel**.")
    
    # Menampilkan contoh kode dengan format rapi
    st.code("""
# Contoh membuat variabel di Python
nama = "Budi"
umur = 17
tinggi = 165.5

print(nama)
    """, language="python")
    
    # Menambahkan Video Penjelasan (Bisa dari YouTube)
    st.subheader("📺 Video Pendukung")
    st.video("https://www.youtube.com/watch?v=kqtD5dpn9C8") # Ganti dengan URL video kamu sendiri

# --- KUIS INTERAKTIF ---
elif menu == "Kuis Interaktif":
    st.title("✍️ Kuis Evaluasi")
    st.write("Uji pemahamanmu setelah membaca materi di atas!")
    
    # Pertanyaan 1
    q1 = st.radio(
        "1. Siapa pencipta bahasa pemrograman Python?",
        ["Dennis Ritchie", "Guido van Rossum", "James Gosling", "Mark Zuckerberg"]
    )
    
    # Tombol Cek Jawaban
    if st.button("Cek Jawaban"):
        if q1 == "Guido van Rossum":
            st.success("🎉 Benar sekali! Guido van Rossum menciptakan Python pada tahun 1991.")
        else:
            st.error("❌ Salah. Yuk baca lagi Bab 1!")
