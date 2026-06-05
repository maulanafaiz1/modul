import streamlit as st

# ==========================================
# CONFIGURE PAGE
# ==========================================
st.set_page_config(
    page_title="E-Modul Bioinformatika: Sintesis Protein",
    page_icon="🧬",
    layout="wide"
)

# Fungsi bantuan untuk simulasi Bioinformatika sederhana
def transkripsi(dna):
    # Mengganti Timin (T) dengan Urasil (U) untuk membentuk mRNA
    return dna.upper().replace('T', 'U')

def translasi(mrna):
    # Tabel Kodon Standar
    tabel_kodon = {
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M (Start)',
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
        'UAC':'Y', 'UAU':'Y', 'UAA':'STOP', 'UAG':'STOP',
        'UGA':'STOP', 'UGC':'C', 'UGU':'C', 'UGG':'W',
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    }
    
    mrna = mrna.upper().strip()
    asam_amino = []
    
    # Membaca per 3 basa nitrogen (kodon)
    for i in range(0, len(mrna) - (len(mrna) % 3), 3):
        kodon = mrna[i:i+3]
        if kodon in tabel_kodon:
            simbol = tabel_kodon[kodon]
            asam_amino.append(simbol)
            if "STOP" in simbol:
                break
                
    return " - ".join(asam_amino) if asam_amino else "Kodon tidak dikenali atau rantai terlalu pendek."

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.title("🧬 E-Modul Bioinformatika")
st.sidebar.markdown("**Materi:** Sintesis Protein")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Daftar Isi:",
    [
        "Halaman Utama", 
        "1. Konsep Sintesis Protein", 
        "2. Pendekatan Bioinformatika", 
        "3. Lab Virtual (Simulasi Python)", 
        "4. Kuis Evaluasi Pemahaman"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Petunjuk:** Pelajari materi secara berurutan untuk meningkatkan pemahaman konsep Anda.")

# ==========================================
# KONTEN HALAMAN
# ==========================================

# --- HALAMAN UTAMA ---
if menu == "Halaman Utama":
    st.title("🔬 Pengembangan E-Modul Bioinformatika Berbantuan Python")
    st.subheader("Materi: Sintesis Protein untuk Meningkatkan Pemahaman Konsep")
    
    st.markdown("""
    Selamat datang di **E-Modul Interaktif Bioinformatika**! 
    
    Modul digital ini menggabungkan konsep biologi molekuler dengan ilmu komputer (Python). Melalui pendekatan ini, Anda tidak hanya menghafal proses sintesis protein, tetapi juga memahami bagaimana data genetik diolah secara komputasi seperti yang dilakukan oleh para ilmuwan modern.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("🎯 **Tujuan Pembelajaran:**\n1. Memahami tahap Transkripsi dan Translasi.\n2. Menganalisis perubahan kodon menjadi asam amino.\n3. Mengaplikasikan algoritma pemrograman Python untuk memproses data sekuens DNA.")
    with col2:
        st.info("💻 **Prasyarat:**\nTidak perlu mahir coding! Kode Python di modul ini dirancang sesederhana mungkin agar mudah dipahami sebagai alat bantu visualisasi logika biologi.")

# --- MATERI 1: KONSEP SINTESIS PROTEIN ---
elif menu == "1. Konsep Sintesis Protein":
    st.title("🧬 Konsep Dasar Sintesis Protein")
    st.write("Sintesis protein adalah proses pembentukan protein dari informasi genetik yang terdapat pada DNA. Proses ini mengikuti **Dogma Sentral Biologi Molekuler**: **DNA → RNA → Protein**.")
    
    tab1, tab2 = st.tabs(["1. Transkripsi", "2. Translasi"])
    
    with tab1:
        st.header("Tahap Transkripsi")
        st.write("""
        Transkripsi adalah proses penyalinan kode genetik dari rantai **DNA Template (cetakan)** menjadi rantai **mRNA (messenger RNA)**. 
        Proses ini terjadi di dalam **Nukleus (Inti Sel)**.
        
        * **Aturan Pasangan Basa pada RNA:**
            * Adenin (A) berpasangan dengan Urasil (U) *(Bukan Timin!)*
            * Timin (T) pada DNA tetap berpasangan dengan Adenin (A) pada RNA
            * Sitosin (C) berpasangan dengan Guanin (G)
            * Guanin (G) berpasangan dengan Sitosin (C)
        """)
        
    with tab2:
        st.header("Tahap Translasi")
        st.write("""
        Translasi adalah proses penerjemahan urutan kodon (tiga basa nitrogen) pada mRNA menjadi rangkaian **Asam Amino** yang membentuk protein. 
        Proses ini terjadi di **Ribosom** di sitoplasma.
        
        * **Kodon Start:** AUG (Metionin), menandai dimulainya sintesis protein.
        * **Kodon Stop:** UAA, UAG, UGA, menandai berakhirnya pembentukan rantai protein.
        """)

# --- MATERI 2: PENDEKATAN BIOINFORMATIKA ---
elif menu == "2. Pendekatan Bioinformatika":
    st.title("💻 Bagaimana Python Membantu Bioinformatika?")
    st.write("""
    Dalam dunia nyata, rantai DNA manusia terdiri dari miliaran basa nitrogen. Sangat mustahil bagi ilmuwan untuk menerjemahkannya satu per satu secara manual. 
    Di sinilah **Python** digunakan untuk mempercepat analisis string/teks data genetik.
    """)
    
    st.subheader("Logika Kode Python untuk Sintesis Protein")
    st.write("Berikut adalah logika dasar bagaimana kita memprogram komputer untuk melakukan transkripsi dan translasi:")
    
    # Menampilkan potongan kode edukatif
    st.code("""
# 1. Logika Transkripsi (Mengganti T dengan U)
def transkripsi(dna):
    return dna.replace("T", "U")

# 2. Logika Translasi (Memotong tiap 3 huruf / Kodon)
# Contoh: "AUGGCC" dipotong menjadi ["AUG", "GCC"]
# Lalu dicocokkan dengan kamus (dictionary) Asam Amino.
    """, language="python")

# --- MATERI 3: LAB VIRTUAL ---
elif menu == "3. Lab Virtual (Simulasi Python)":
    st.title("🧪 Lab Virtual Bioinformatika")
    st.write("Silakan masukkan rantai **DNA Sense / Template** Anda sendiri di bawah ini untuk melihat bagaimana Python melakukan Transkripsi dan Translasi secara instan!")
    
    # Input dari pengguna
    input_dna = st.text_input("Masukkan Urutan DNA (Gunakan huruf A, T, C, G saja):", "ATGGCCGCAUGA")
    
    # Validasi input sederhana
    input_dna = input_dna.upper().strip()
    valid_bases = set("ATCG")
    is_valid = all(base in valid_bases for base in input_dna)
    
    if input_dna and not is_valid:
        st.warning("⚠️ Input mengandung karakter selain A, T, C, G. Mohon periksa kembali rantai DNA Anda.")
    
    if st.button("Jalankan Proses Simulasi 🚀") and is_valid:
        st.markdown("### 📊 Hasil Pemrosesan Komputasi:")
        
        # Proses Transkripsi
        hasil_mrna = transkripsi(input_dna)
        st.info(f"**1. Hasil Transkripsi (mRNA):** \n `{hasil_mrna}`")
        
        # Proses Translasi
        hasil_protein = translasi(hasil_mrna)
        st.success(f"**2. Hasil Translasi (Rantai Asam Amino):** \n **{hasil_protein}**")
        
        # Penjelasan Konseptual
        st.markdown("---")
        st.markdown("**Analisis Konsep:**")
        st.write(f"Komputer membaca rantai DNA sepanjang **{len(input_dna)} basa**. Hasil transkripsi menghasilkan mRNA dengan panjang yang sama namun basa **Timin (T) diganti menjadi Urasil (U)**. Pada tahap translasi, setiap **3 basa** dikelompokkan menjadi satu kodon untuk menentukan jenis asam aminonya.")

# --- MATERI 4: KUIS EVALUASI ---
elif menu == "4. Kuis Evaluasi Pemahaman":
    st.title("✍️ Kuis Evaluasi Pemahaman Konsep")
    st.write("Uji pemahaman konsep Anda mengenai Sintesis Protein dan penerapannya dalam komputasi di sini.")
    
    # Form untuk kuis
    with st.form("kuis_sintesis"):
        # Pertanyaan 1
        q1 = st.radio(
            "1. Jika sekuens DNA Template adalah 'TAC', maka sekuens mRNA hasil transkripsinya adalah...",
            ["ATG", "AUG", "UAC", "GUG"]
        )
        
        # Pertanyaan 2
        q2 = st.radio(
            "2. Di organel sel manakah fungsi kode perintah Python 'Translasi' terjadi di dunia biologi nyata?",
            ["Nukleus", "Mitokondria", "Ribosom", "Badan Golgi"]
        )
        
        # Pertanyaan 3
        q3 = st.radio(
            "3. Mengapa pendekatan komputasi (Bioinformatika) penting dalam menganalisis sintesis protein?",
            ["Karena protein di dalam tubuh berbentuk digital", "Untuk mempercepat penerjemahan rantai sekuens DNA yang berukuran raksasa", "Agar rantai DNA berubah menjadi bahasa pemrograman", "Karena komputer bisa mematikan mutasi genetik"]
        )
        
        # Tombol submit form
        submitted = st.form_submit_button("Kirim Jawaban")
        
        if submitted:
            skor = 0
            
            # Cek Q1
            if q1 == "AUG":
                skor += 1
