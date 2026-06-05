import streamlit as st
import pandas as pd

# ==============================================================================
# CONFIRGURASI HALAMAN & TEMA (Karakteristik User-Friendly)
# ==============================================================================
st.set_page_config(
    page_title="E-Modul Bioinformatika: Sintesis Protein",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Kamus Kode Genetik (Mesin Logika Transkripsi & Translasi)
TABEL_KODON = {
    'UUU': 'Fenilalanin (Phe)', 'UUC': 'Fenilalanin (Phe)', 'UUA': 'Leusin (Leu)', 'UUG': 'Leusin (Leu)',
    'CUU': 'Leusin (Leu)', 'CUC': 'Leusin (Leu)', 'CUA': 'Leusin (Leu)', 'CUG': 'Leusin (Leu)',
    'AUU': 'Isoleusin (Ile)', 'AUC': 'Isoleusin (Ile)', 'AUA': 'Isoleusin (Ile)', 'AUG': 'Metionin (Met) [START]',
    'GUU': 'Valin (Val)', 'GUC': 'Valin (Val)', 'GUA': 'Valin (Val)', 'GUG': 'Valin (Val)',
    'UCU': 'Serin (Ser)', 'UCC': 'Serin (Ser)', 'UCA': 'Serin (Ser)', 'UCG': 'Serin (Ser)',
    'CCU': 'Prolin (Pro)', 'CCC': 'Prolin (Pro)', 'CCA': 'Prolin (Pro)', 'CCG': 'Prolin (Pro)',
    'ACU': 'Treonin (Thr)', 'ACC': 'Treonin (Thr)', 'ACA': 'Treonin (Thr)', 'ACG': 'Treonin (Thr)',
    'GCU': 'Alanin (Ala)', 'GCC': 'Alanin (Ala)', 'GCA': 'Alanin (Ala)', 'GCG': 'Alanin (Ala)',
    'UAU': 'Tirosin (Tyr)', 'UAC': 'Tirosin (Tyr)', 'UAA': 'STOP', 'UAG': 'STOP',
    'CAU': 'Histidin (His)', 'CAC': 'Histidin (His)', 'CAA': 'Glutamin (Gln)', 'CAG': 'Glutamin (Gln)',
    'AAU': 'Asparagin (Asn)', 'AAC': 'Asparagin (Asn)', 'AAA': 'Lisin (Lys)', 'AAG': 'Lisin (Lys)',
    'GAU': 'Asam Aspartat (Asp)', 'GAC': 'Asam Aspartat (Asp)', 'GAA': 'Asam Glutamat (Glu)', 'GAG': 'Asam Glutamat (Glu)',
    'UGU': 'Sistein (Cys)', 'UGC': 'Sistein (Cys)', 'UGA': 'STOP', 'UGG': 'Triptofan (Trp)',
    'CGU': 'Arginin (Arg)', 'CGC': 'Arginin (Arg)', 'CGA': 'Arginin (Arg)', 'CGG': 'Arginin (Arg)',
    'AGU': 'Serin (Ser)', 'AGC': 'Serin (Ser)', 'AGA': 'Arginin (Arg)', 'AGG': 'Arginin (Arg)',
    'GGU': 'Glisin (Gly)', 'GGC': 'Glisin (Gly)', 'GGA': 'Glisin (Gly)', 'GGG': 'Glisin (Gly)'
}

# ==============================================================================
# SIDEBAR / PANEL NAVIGASI (Menggunakan Banyak Elemen Kontrol Streamlit)
# ==============================================================================
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/e/e5/Untirta_logo.png", width=100)
st.sidebar.title("Navigasi E-Modul")
st.sidebar.caption("Pengembangan E-Modul Bioinformatika Berbantuan Python")

# Pilihan Menu Utama
menu = st.sidebar.radio(
    "Pilih Ruang Belajar:",
    ["Halaman Utama & Panduan", "1. Materi Transkripsi", "2. Materi Translasi", "3. Laboratorium Komputasi (Simulasi)", "4. Evaluasi Mandiri"]
)

# Indikator Progress Belajar Siswa
st.sidebar.markdown("---")
st.sidebar.subheader("Progress Belajar Kamu")
prog_utama = st.sidebar.slider("Persentase Pemahaman Sesi Ini", 0, 100, 25)
st.sidebar.progress(prog_utama)

# ==============================================================================
# 1. HALAMAN UTAMA & PANDUAN
# ==============================================================================
if menu == "Halaman Utama & Panduan":
    st.title("🧬 E-Modul Bioinformatika & Sintesis Protein")
    st.subheader("Pendekatan Komputasi untuk Memahami Proses Kehidupan Molekuler")
    
    st.info("""
    **Selamat Datang di Dunia Biologi Masa Depan!** E-modul ini dirancang khusus untuk membantumu memvisualisasikan bagaimana informasi genetik pada DNA 
    diubah menjadi protein fungsional menggunakan bantuan baris kode pemrograman Python.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 🎯 Tujuan Pembelajaran:
        1. Memahami mekanisme **Transkripsi** (pembentukan mRNA dari DNA cetakan).
        2. Memahami mekanisme **Translasi** (penerjemahan mRNA menjadi rantai asam amino/protein).
        3. Mampu menganalisis sekuens genetik menggunakan logika pemrograman sederhana.
        """)
    with col2:
        st.markdown("""
        ### 🛠️ Cara Menggunakan E-Modul:
        * Gunakan menu di **Panel Kiri (Sidebar)** untuk berpindah materi.
        * Ikuti simulasi di **Laboratorium Komputasi** untuk bereksperimen dengan DNA buatanmu sendiri.
        * Kerjakan kuis interaktif di akhir sesi untuk menguji pemahaman konsepmu.
        """)

# ==============================================================================
# 2. MATERI TRANSKRIPSI (DENGAN TAMBAHAN VIDEO ANIMASI)
# ==============================================================================
elif menu == "1. Materi Transkripsi":
    st.title("📑 Tahap 1: Transkripsi (Penyalinan Kode)")
    
    st.markdown("""
    **Transkripsi** adalah proses sintesis untai RNA dari cetakan DNA. Proses ini terjadi di dalam nukleus (inti sel). 
    Enzim utama yang berperan dalam proses ini adalah **RNA Polimerase**.
    
    Aturan dasar pemasangan basa nitrogen dari DNA ke RNA:
    * Adenin (**A**) pada DNA dicetak menjadi Urasil (**U**) pada RNA.
    * Timin (**T**) pada DNA dicetak menjadi Adenin (**A**) pada RNA.
    * Sitosin (**C**) pada DNA dicetak menjadi Guanin (**G**) pada RNA.
    * Guanin (**G**) pada DNA dicetak menjadi Sitosin (**C**) pada RNA.
    """)
    
    # --- ELEMEN BARU: SEMATAN VIDEO TRANSKRIPSI ---
    st.subheader("🎬 Video Animasi Mekanisme Transkripsi")
    st.caption("Tonton video di bawah ini untuk melihat bagaimana untai mRNA disintesis secara dinamis di dalam inti sel:")
    # Menyematkan video edukasi visual transkripsi dari YouTube
    st.video("https://www.youtube.com/watch?v=gG7uCskUOrA")
    
    # Elemen Interaktif Expander untuk Detail Proses
    with st.expander("🔍 Lihat 3 Langkah Utama Transkripsi"):
        st.markdown("""
        1. **Inisiasi:** RNA Polimerase menempel pada wilayah promoter DNA.
        2. **Elongasi:** Pemanjangan untai mRNA seiring bergeraknya enzim di sepanjang DNA cetakan.
        3. **Terminasi:** Transkripsi berhenti ketika enzim mencapai sekuens terminator.
        """)
        
    # Fitur Cek Pemahaman Instan
    st.subheader("💡 Cek Pemahaman Cepat")
    pilihan_trans = st.radio(
        "Jika untai DNA Template memiliki sekuens 'TAC', maka sekuens mRNA hasil transkripsinya adalah...",
        ["ATG", "AUG", "UAC", "GUG"]
    )
    if st.button("Cek Jawaban"):
        if pilihan_trans == "AUG":
            st.success("🎉 Benar sekali! T berpasangan dengan A, A dengan U, dan C dengan G.")
        else:
            st.error("❌ Belum tepat. Ingat, pada RNA tidak ada Timin (T), melainkan digantikan oleh Urasil (U).")

# ==============================================================================
# 3. MATERI TRANSLASI (DENGAN TAMBAHAN VIDEO ANIMASI)
# ==============================================================================
elif menu == "2. Materi Translasi":
    st.title("📑 Tahap 2: Translasi (Penerjemahan Kode)")
    st.markdown("""
    Setelah mRNA matang terbentuk, ia akan keluar dari nukleus menuju **Ribosom** di sitoplasma. 
    Di ribosom inilah terjadi **Translasi**, yaitu proses penerjemahan urutan nukleotida (kodon) 
    pada mRNA menjadi urutan asam amino yang menyusun protein.
    """)
    
    # --- ELEMEN BARU: SEMATAN VIDEO TRANSLASI ---
    st.subheader("🎬 Video Animasi Mekanisme Translasi")
    st.caption("Tonton video di bawah ini untuk memvisualisasikan bagaimana ribosom membaca kodon triplet menjadi rantai asam amino:")
    # Menyematkan video edukasi visual translasi dari YouTube
    st.video("https://www.youtube.com/watch?v=5bLEDd-PSTQ")
    
    # Menampilkan Tabel Kodon Interaktif bawaan Streamlit (Menggunakan Dataframe)
    st.subheader("📋 Kamus Kodon Asam Amino Digital")
    st.write("Berikut adalah sebagian contoh data penerjemahan kodon triplet berdasarkan algoritma biopython:")
    
    contoh_data = {
        "Kodon (Triplet)": ["AUG", "UUU", "UUA", "GUC", "UAA"],
        "Asam Amino Hasil": ["Metionin (START)", "Fenilalanin", "Leusin", "Valin", "STOP (Berhenti)"]
    }
    st.dataframe(pd.DataFrame(contoh_data), use_container_width=True)

# ==============================================================================
# 4. LABORATORIUM KOMPUTASI (SIMULASI INTERAKTIF STREAMLIT)
# ==============================================================================
elif menu == "3. Laboratorium Komputasi (Simulasi)":
    st.title("🧪 Laboratorium Komputasi Bioinformatika")
    st.subheader("Simulasikan Transkripsi & Translasi Menggunakan Mesin Logika Python")
    
    st.write("""
    Di sini kamu bertindak sebagai peneliti muda! Masukkan rantai **DNA Template (Sense)** kamu sendiri, 
    dan lihat bagaimana komputer mengeksekusi transkripsi dan translasi secara langsung.
    """)
    
    # Input Teks untuk Sekuens DNA
    input_dna = st.text_input("Masukkan Sekuens DNA (Gunakan huruf A, T, C, G saja):", value="TACTTCCGCACT").upper()
    
    # Validasi Input secara sederhana
    valid_bases = set("ATCG")
    if not set(input_dna).issubset(valid_bases):
        st.warning("⚠️ Peringatan: Sekuens DNA hanya boleh mengandung karakter basa A, T, C, dan G!")
    else:
        st.success("✅ Sekuens DNA valid dan siap diproses komputasi.")
        
        # Tombol Eksekusi Utama
        if st.button("🧬 Jalankan Simulasi Bioinformatika"):
            st.markdown("---")
            
            # --- PROSES TRANSKRIPSI (LOGIKA PYTHON) ---
            peta_transkripsi = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
            mrna_list = [peta_transkripsi[basa] for basa in input_dna]
            mrna_hasil = "".join(mrna_list)
            
            st.subheader("1. Hasil Tahap Transkripsi")
            col_dna, col_arrow, col_rna = st.columns([4, 1, 4])
            col_dna.metric(label="DNA Template (Input)", value=input_dna)
            col_arrow.markdown("<h2 style='text-align: center;'>➡️</h2>", unsafe_allow_html=True)
            col_rna.metric(label="mRNA Hasil Cetakan", value=mrna_hasil)
            
            # --- PROSES TRANSLASI (LOGIKA PYTHON) ---
            st.subheader("2. Hasil Tahap Translasi (Pencarian Kodon Triplet)")
            
            # Memecah mRNA menjadi triplet (Kodon)
            kodon_list = [mrna_hasil[i:i+3] for i in range(0, len(mrna_hasil), 3)]
            st.write(f"Kodon yang terdeteksi komputer dari rantai mRNA: `{kodon_list}`")
            
            # Menerjemahkan menggunakan Kamus Kodon
            asam_amino_hasil = []
            for kodon in kodon_list:
                if len(kodon) == 3: # Memastikan triplet lengkap
                    nama_asam = TABEL_KODON.get(kodon, "Tidak Diketahui")
                    asam_amino_hasil.append(f"**{kodon}** ➡️ {nama_asam}")
            
            # Menampilkan hasil rantai protein dalam bentuk list terstruktur
            for item in asam_amino_hasil:
                st.write(f"* {item}")
                
            st.balloons() # Efek animasi keberhasilan simulasi

# ==============================================================================
# 5. EVALUASI MANDIRI (KUIS INTERAKTIF)
# ==============================================================================
elif menu == "4. Evaluasi Mandiri":
    st.title("📝 Uji Pemahaman Konsep (Evaluasi Mandiri)")
    st.write("Jawablah pertanyaan di bawah ini untuk menguji sejauh mana pemahamanmu tentang materi ini.")
    
    # Form untuk mengunci jawaban kuis sebelum dinilai
    with st.form("kuis_sintesis"):
        st.markdown("### **Soal 1**")
        q1 = st.radio(
            "Di organel manakah proses translasi mRNA menjadi protein terjadi?",
            ["Nukleus", "Mitokondria", "Ribosom", "Badan Golgi"]
        )
        
        st.markdown("### **Soal 2**")
        q2 = st.radio(
            "Kodon yang bertindak sebagai penanda dimulainya proses sintesis protein (Start Codon) adalah...",
            ["UAA", "AUG", "UGA", "UAG"]
        )
        
        # Tombol Submit Form
        submit_kuis = st.form_submit_button("Kirim Jawaban")
        
        if submit_kuis:
            skor = 0
            # Cek Soal 1
            if q1 == "Ribosom":
                skor += 50
            # Cek Soal 2
            if q2 == "AUG":
                skor += 50
                
            st.markdown("### 📊 Hasil Evaluasi Kamu:")
            if skor == 100:
                st.success(f"Selamat! Nilai kamu **{skor}/100**. Kamu sudah menguasai konsep sintesis protein dengan sangat baik!")
            else:
                st.warning(f"Nilai kamu **{skor}/100**. Jangan berkecil hati, silakan ulas kembali materi atau coba laboratorium simulasi lagi!")
