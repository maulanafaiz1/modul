import streamlit as st
import pandas as pd

# ==============================================================================
# 1. KONFIGURASI HALAMAN & TEMA (User-Friendly & Professional Layout)
# ==============================================================================
st.set_page_config(
    page_title="E-Modul Bioinformatika: Sintesis Protein Lengkap",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Database Kodon Genetik Lengkap
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
# 2. SIDEBAR NAVIGATION & PROGRESS TRACKER
# ==============================================================================
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/e/e5/Untirta_logo.png", width=110)
st.sidebar.title("🧬 Menu E-Modul v2")
st.sidebar.caption("Pendekatan Komputasi untuk Miskonsepsi Sintesis Protein")

menu = st.sidebar.radio(
    "Silakan Pilih Sub-Materi:",
    [
        "Halaman Utama & Silabus", 
        "1. Pendalaman Materi Transkripsi", 
        "2. Pendalaman Materi Translasi", 
        "3. Kamus Kodon Interaktif",
        "4. Laboratorium Komputasi & Mutasi", 
        "5. Bank Soal Evaluasi Mandiri"
    ]
)

st.sidebar.markdown("---")
st.sidebar.subheader("📊 Tracking Belajar Mandiri")
baca_materi = st.sidebar.checkbox("Sudah Membaca Semua Materi")
ikut_lab = st.sidebar.checkbox("Sudah Mencoba Laboratorium")
ikut_kuis = st.sidebar.checkbox("Sudah Mengerjakan Evaluasi")

# Hitung progress berdasarkan checkbox yang dicentang
progress_score = sum([baca_materi, ikut_lab, ikut_kuis]) * 33.3
st.sidebar.progress(int(progress_score))
st.sidebar.caption(f"Progress Penyelesaian Modul: {int(progress_score)}%")

# ==============================================================================
# 3. HALAMAN UTAMA & SILABUS
# ==============================================================================
if menu == "Halaman Utama & Silabus":
    st.title("🧬 E-Modul Interaktif Bioinformatika Berbantuan Python")
    st.subheader("Materi Pokok: Mekanisme Ekspresi Gen dan Sintesis Protein")
    
    st.info("""
    **Deskripsi E-Modul:** Media pembelajaran ini dikembangkan untuk memberikan visualisasi konkret 
    mengenai fenomena molekuler abstrak dalam materi Sintesis Protein. Dengan bantuan algoritma komputasi Python, 
    kamu tidak hanya menghafal, melainkan dapat memanipulasi sekuens basa nitrogen dan melihat dampaknya secara langsung.
    """)
    
    tabs = st.tabs(["🎯 Capaian Pembelajaran", "📖 Petunjuk Penggunaan", "👥 Tim Pengembang"])
    with tabs[0]:
        st.markdown("""
        * **Menganalisis** hubungan antara struktur DNA, gen, dan kromosom dalam penentuan sifat makhluk hidup.
        * **Menjelaskan** tahapan mekanisme transkripsi (inisiasi, elongasi, terminasi) dan modifikasi pasca-transkripsi.
        * **Menjelaskan** tahapan mekanisme translasi pada ribosom serta meramalkan dampak mutasi titik (*point mutation*).
        """)
    with tabs[1]:
        st.markdown("""
        1. Mulailah dengan mempelajari materi pada **Menu 1** dan **Menu 2**, lalu tonton video animasinya.
        2. Gunakan **Menu 3** untuk mencari dan mencocokkan kodon triplet.
        3. Lakukan eksperimen mandiri di **Menu 4** dengan memasukkan sekuens DNA pilihanmu dan pelajari efek mutasinya.
        4. Kerjakan evaluasi di **Menu 5** untuk mengukur tingkat ketuntasan belajarmu.
        """)
    with tabs[2]:
        st.markdown("""
        * **Peneliti:** Jurusan Pendidikan Biologi, Universitas Sultan Ageng Tirtayasa (UNTIRTA).
        * **Subjek Uji Coba:** Peserta Didik Kelas XI SMAN 1 Cikande.
        """)

# ==============================================================================
# 4. PENDALAMAN MATERI TRANSKRIPSI
# ==============================================================================
elif menu == "1. Pendalaman Materi Transkripsi":
    st.title("📑 Tahap I: Transkripsi (Sintesis RNA)")
    
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        **Transkripsi** merupakan proses penyalinan kode-kode genetik yang terdapat pada urutan DNA menjadi urutan nukleotida RNA. 
        Proses ini terjadi di nukleus dan dikatalisis oleh enzim **RNA Polimerase**.
        
        #### 🕒 Tiga Langkah Utama Mekanisme Transkripsi:
        1. **Inisiasi (Permulaan):** RNA polimerase berikatan dengan wilayah **Promoter** (sekuens DNA spesifik penanda awal gen, seperti *TATA Box*). Ikatan ini menyebabkan untai ganda DNA membuka.
        2. **Elongasi (Pemanjangan):** RNA polimerase bergerak di sepanjang untai cetakan DNA (*Template/Sense*) dari arah 3' ke 5', sambil merangkai ribonukleotida menjadi untai mRNA baru dari arah 5' ke 3'.
        3. **Terminasi (Pengakhiran):** Transkripsi berlangsung sampai RNA polimerase mentranskripsi urutan DNA yang disebut **Terminator**. Setelah itu, mRNA lepas dan RNA polimerase memisahkan diri dari DNA.
        """)
    with col2:
        st.warning("""
        **⚠️ Perbedaan Penting Basa Nitrogen:**
        * DNA memiliki basa **Timin (T)** yang berpasangan dengan Adenin (A).
        * RNA tidak memiliki Timin, posisinya digantikan oleh **Urasil (U)**. Jadi, jika pada DNA cetakan terdapat basa **A**, maka RNA hasil cetakannya berpasangan dengan **U**.
        """)

    st.subheader("🎬 Video Visualisasi Mekanisme Transkripsi")
    st.video("https://www.youtube.com/watch?v=gG7uCskUOrA")
    
    with st.expander("🔬 Info Pengayaan Ilmu: Modifikasi Pasca-Transkripsi (Eukariotik)"):
        st.markdown("""
        Sebelum keluar dari nukleus menuju sitoplasma, pre-mRNA pada organisme eukariotik harus melalui 3 pemrosesan penting:
        * **Pemberian Cap 5' (5' Capping):** Penambahan molekul guanin termodifikasi pada ujung 5' untuk melindungi mRNA dari degradasi enzim hidrolitik.
        * **Pemberian Ekor Poly-A (Poly-A Tail):** Penambahan 50-250 nukleotida adenin pada ujung 3' untuk membantu transportasi mRNA keluar nukleus.
        * **Penyambungan RNA (RNA Splicing):** Pemotongan bagian non-coding (**Intron**) dan penyambungan kembali bagian coding (**Ekson**) oleh kompleks *spliseosom*.
        """)

# ==============================================================================
# 5. PENDALAMAN MATERI TRANSLASI
# ==============================================================================
elif menu == "2. Pendalaman Materi Translasi":
    st.title("📑 Tahap II: Translasi (Penerjemahan Kodon)")
    
    st.markdown("""
    **Translasi** adalah proses sintesis polipeptida (protein) dengan spesifikasi urutan asam amino berdasarkan kode genetik 
    yang dibawa oleh mRNA. Proses ini berlangsung di **Ribosom** di dalam sitoplasma sel.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        #### ⚙️ Komponen Utama yang Terlibat:
        * **mRNA (messenger RNA):** Membawa salinan kodon (kode genetik triplet dari inti sel).
        * **tRNA (transfer RNA):** Membawa asam amino yang sesuai dari sitoplasma menuju ribosom. tRNA memiliki ujung penyusun bernama **Antikodon** yang akan berpasangan secara komplementer dengan kodon mRNA.
        * **Ribosom:** Terdiri dari sub-unit besar dan sub-unit kecil yang berfungsi sebagai tempat penataan molekuler.
        """)
    with col2:
        st.markdown("""
        #### 🏛️ Struktur Situs Aktif Ribosom Sub-Unit Besar:
        1. **Situs A (Aminoasil-tRNA):** Tempat masuknya molekul tRNA pembawa asam amino baru.
        2. **Situs P (Peptidil-tRNA):** Tempat tRNA memegang rantai polipeptida (asam amino) yang sedang tumbuh.
        3. **Situs E (Exit):** Tempat tRNA yang sudah kosong (kehilangan asam aminonya) bersiap untuk keluar dari ribosom.
        """)

    st.subheader("🎬 Video Visualisasi Mekanisme Translasi")
    st.video("https://www.youtube.com/watch?v=5bLEDd-PSTQ")

# ==============================================================================
# 6. KAMUS KODON INTERAKTIF (FITUR ELEMEN BARU)
# ==============================================================================
elif menu == "3. Kamus Kodon Interaktif":
    st.title("📋 Kamus Kodon Asam Amino Digital")
    st.write("Gunakan fitur interaktif ini untuk mencari pasangan nama asam amino berdasarkan kodon triplet secara cepat.")
    
    # Membuat tabel dataframe dari kamus lengkap
    df_kodon = pd.DataFrame(list(TABEL_KODON.items()), columns=["Kodon Triplet (mRNA)", "Asam Amino / Keterangan"])
    
    # Elemen Search Input bawaan Streamlit
    cari_kodon = st.text_input("🔍 Ketikkan 3 digit kodon untuk memfilter data (Contoh: AUG atau UUU):").upper()
    
    if cari_kodon:
        df_filtered = df_kodon[df_kodon["Kodon Triplet (mRNA)"].str.contains(cari_kodon)]
        st.dataframe(df_filtered, use_container_width=True)
    else:
        st.dataframe(df_kodon, use_container_width=True)

# ==============================================================================
# 7. LABORATORIUM KOMPUTASI & MUTASI GENETIK
# ==============================================================================
elif menu == "4. Laboratorium Komputasi & Mutasi":
    st.title("🧪 Laboratorium Simulasi Bioinformatika & Mutasi Genetik")
    st.write("Ujilah sekuens DNA buatanmu sendiri untuk melihat proses komputasi transkripsi, translasi, serta analisis jenis mutasi.")
    
    # Input sekuens default
    input_dna = st.text_input("Masukkan Urutan DNA Template (Gunakan kombinasi A, T, C, G):", value="TACTTCCGCACT").upper()
    
    # Validasi
    if not set(input_dna).issubset(set("ATCG")):
        st.error("⚠️ Input Salah! Urutan DNA hanya boleh terdiri dari karakter huruf A, T, C, atau G.")
    else:
        st.success("✅ Urutan DNA valid dan siap dianalisis sistem.")
        
        if st.button("🧬 Jalankan Komputasi Ekspresi Gen"):
            # Proses Transkripsi
            peta_trans = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
            mrna_hasil = "".join([peta_trans[basa] for basa in input_dna])
            
            st.markdown("### 🧬 1. Hasil Cetakan Tahap Transkripsi")
            c1, c2 = st.columns(2)
            c1.metric(label="DNA Template (Input)", value=input_dna)
            c2.metric(label="mRNA (Hasil Transkripsi)", value=mrna_hasil)
            
            # Proses Translasi
            st.markdown("### 🧵 2. Hasil Penerjemahan Tahap Translasi")
            kodon_list = [mrna_hasil[i:i+3] for i in range(0, len(mrna_hasil), 3)]
            
            protein_list = []
            for k in kodon_list:
                if len(k) == 3:
                    protein_list.append(TABEL_KODON.get(k, "Tidak Diketahui"))
            
            st.write("Rantai Asam Amino (Protein) yang Terbentuk:")
            st.code(" ➡️ ".join(protein_list))
            
        st.markdown("---")
        st.subheader("👾 Simulasi Studi Kasus Mutasi Titik (Point Mutation)")
        st.write("Bagaimana jika terjadi kesalahan penyalinan satu basa nitrogen? Mari kita bandingkan DNA normal dengan DNA bermutasi.")
        
        # Contoh studi kasus mutasi bawaan modul
        kasus_mutasi = st.selectbox(
            "Pilih Jenis Studi Kasus Mutasi:",
            ["Mutasi Diam (Silent Mutation)", "Mutasi Salah Arti (Missense Mutation)", "Mutasi Tanpa Arti (Nonsense Mutation)"]
        )
        
        if kasus_mutasi == "Mutasi Diam (Silent Mutation)":
            st.info("**Penjelasan:** Terjadi perubahan satu basa nitrogen pada DNA, namun tidak mengubah jenis asam amino yang dihasilkan karena kodon baru mengode asam amino yang sama.")
            st.write("* DNA Normal: `TAC` ➡️ mRNA: `AUG` ➡️ Asam Amino: **Metionin**")
            st.write("* DNA Mutasi: `TAT` ➡️ mRNA: `AUA` ➡️ Asam Amino: **Isoleusin** (Contoh lain: Perubahan kodon UUU menjadi UUC tetap menghasilkan **Fenilalanin**)")
        
        elif kasus_mutasi == "Mutasi Salah Arti (Missense Mutation)":
            st.info("**Penjelasan:** Perubahan basa nitrogen menyebabkan perubahan kodon mRNA yang berakibat pada berubahnya jenis asam amino yang dikodekan. Hal ini bisa berdampak pada perubahan struktur fungsi protein.")
            st.write("* DNA Normal: `TTT` ➡️ mRNA: `AAA` ➡️ Asam Amino: **Lisin**")
            st.write("* DNA Mutasi: `GTT` ➡️ mRNA: `CAA` ➡️ Asam Amino: **Glutamin**")
            
        elif kasus_mutasi == "Mutasi Tanpa Arti (Nonsense Mutation)":
            st.info("**Penjelasan:** Perubahan satu basa nitrogen menyebabkan terbentuknya **Stop Codon** sebelum waktunya, sehingga proses sintesis protein terhenti prematur dan menghasilkan protein yang tidak fungsional.")
            st.write("* DNA Normal: `TAC` ➡️ mRNA: `AUG` ➡️ Asam Amino: **Metionin**")
            st.write("* DNA Mutasi: `ATT` ➡️ mRNA: `UAA` ➡️ Asam Amino: **STOP (Proses Berhenti Prematur)**")

# ==============================================================================
# 8. BANK SOAL EVALUASI MANDIRI (BANYAK SOAL INTERAKTIF)
# ==============================================================================
elif menu == "5. Bank Soal Evaluasi Mandiri":
    st.title("📝 Bank Soal Evaluasi Mandiri Interaktif")
    st.write("Silakan jawab semua soal di bawah ini dengan saksama untuk menguji ketuntasan pemahaman belajarmu.")
    
    with st.form("form_evaluasi_lengkap"):
        # Soal 1
        st.markdown("#### **Soal 1 (C2 - Pemahaman)**")
        ans1 = st.radio(
            "Manakah urutan tahapan sintesis protein yang benar di bawah ini?",
            [
                "A. Translasi - Transkripsi - Pembentukan Protein", 
                "B. Transkripsi - Translasi - Pembentukan Protein", 
                "C. Replikasi - Transkripsi - Translasi", 
                "D. Transkripsi - Replikasi - Pembentukan Protein"
            ]
        )
        
        # Soal 2
        st.markdown("#### **Soal 2 (C3 - Aplikasi)**")
        ans2 = st.radio(
            "Apabila urutan basa nitrogen pada rantai DNA cetakan (Sense) adalah GCT - TCA - AAA, maka kode genetik triplet yang terbentuk pada mRNA adalah...",
            [
                "A. CGA - AGU - UUU", 
                "B. CGU - AGU - UUU", 
                "C. CGA - AGT - TTT", 
                "D. GCU - UCA - AAA"
            ]
        )
        
        # Soal 3
        st.markdown("#### **Soal 3 (C4 - Analisis)**")
        ans3 = st.radio(
            "Apa yang membedakan proses transkripsi pada sel organisme prokariotik dengan eukariotik?",
            [
                "A. Pada prokariotik terjadi di inti sel, eukariotik di sitoplasma.",
                "B. Pada eukariotik, hasil pre-mRNA harus melalui proses splicing (pemotongan intron) terlebih dahulu sebelum translasi.",
                "C. Prokariotik membutuhkan enzim RNA polimerase, eukariotik tidak.",
                "D. Eukariotik melakukan transkripsi secara langsung tanpa promoter."
            ]
        )
        
        # Soal 4
        st.markdown("#### **Soal 4 (C4 - Analisis Mutasi)**")
        ans4 = st.radio(
            "Jika terjadi mutasi titik pada DNA yang berakibat berubahnya satu kodon triplet mRNA dari UGG menjadi UGA, dampak mutasi tersebut dikelompokkan ke dalam jenis...",
            [
                "A. Silent Mutation", 
                "B. Missense Mutation", 
                "C. Nonsense Mutation", 
                "D. Frameshift Mutation"
            ]
        )
        
        # Soal 5
        st.markdown("#### **Soal 5 (C2 - Pemahaman Organel)**")
        ans5 = st.radio(
            "Di dalam struktur ribosom sub-unit besar, bagian manakah yang berfungsi sebagai tempat berikatannya molekul tRNA yang mengikat asam amino baru yang akan dirangkai?",
            [
                "A. Situs P", 
                "B. Situs A", 
                "C. Situs E", 
                "D. Situs Promoter"
            ]
        )
        
        # Tombol Kirim Jawaban Form
        submit_btn = st.form_submit_button("Submit & Hitung Skor Akhir")
        
    if submit_btn:
        skor_akhir = 0
        detail_hasil = []
        
        # Koreksi Soal 1
        if ans1 == "B. Transkripsi - Translasi - Pembentukan Protein":
            skor_akhir += 20
            detail_hasil.append("✅ **Soal 1 Benar:** Alur ekspresi gen dimulai dari penyalinan DNA ke mRNA (Transkripsi) lalu penerjemahan di ribosom (Translasi).")
        else:
            detail_hasil.append("❌ **Soal 1 Salah:** Urutan yang benar adalah Transkripsi terlebih dahulu, baru dilanjutkan dengan Translasi.")
            
        # Koreksi Soal 2
        if ans2 == "A. CGA - AGU - UUU":
            skor_akhir += 20
            detail_hasil.append("✅ **Soal 2 Benar:** Aturan komplementer G➡️C, C➡️G, T➡️A, A➡️U.")
        else:
            detail_hasil.append("❌ **Soal 2 Salah:** Ingat bahwa A berpasangan dengan Urasil (U) pada mRNA, bukan Timin (T).")
            
        # Koreksi Soal 3
        if ans3 == "B. Pada eukariotik, hasil pre-mRNA harus melalui proses splicing (pemotongan intron) terlebih dahulu sebelum translasi.":
            skor_akhir += 20
            detail_hasil.append("✅ **Soal 3 Benar:** Sel eukariotik memiliki intron (non-coding) yang wajib dibuang melalui proses splicing.")
        else:
            detail_hasil.append("❌ **Soal 3 Salah:** Sel eukariotik memiliki struktur materi genetik kompleks yang memerlukan proses pematangan mRNA (splicing).")
            
        # Koreksi Soal 4
        if ans4 == "C. Nonsense Mutation":
            skor_akhir += 20
            detail_hasil.append("✅ **Soal 4 Benar:** UGG mengodekan Triptofan, sedangkan UGA adalah STOP codon. Terbentuknya stop codon secara prematur disebut Nonsense Mutation.")
        else:
            detail_hasil.append("❌ **Soal 4 Salah:** Perubahan yang memunculkan STOP codon lebih awal dikategorikan sebagai Nonsense Mutation.")
            
        # Koreksi Soal 5
        if ans5 == "B. Situs A":
            skor_akhir += 20
            detail_hasil.append("✅ **Soal 5 Benar:** Situs A (Aminoasil) adalah pintu masuk untuk tRNA pembawa asam amino baru.")
        else:
            detail_hasil.append("❌ **Soal 5 Salah:** Situs P adalah tempat rantai polipeptida tumbuh, sedangkan pintu masuk asam amino baru berada di Situs A.")
            
        # Tampilkan Hasil Nilai Akhir
        st.markdown("---")
        st.subheader("📊 Hasil Evaluasi Kompetensi")
        
        if skor_akhir >= 80:
            st.success(f"Selamat! Nilai kamu **{skor_akhir} / 100**. Kamu sudah mencapai kriteria ketuntasan dengan sangat memuaskan!")
            st.balloons()
        elif skor_akhir >= 60:
            st.warning(f"Nilai kamu **{skor_akhir} / 100**. Cukup bagus, silakan baca ulang kembali pembahasan materi yang masih keliru.")
        else:
            st.error(f"Nilai kamu **{skor_akhir} / 100**. Kamu belum mencapai ketuntasan minimum. Ayo coba gunakan menu Laboratorium Komputasi lagi untuk memperkuat konsep!")
            
        # Tampilkan detail pembahasan per soal
        for hint in detail_hasil:
            st.write(hint)
