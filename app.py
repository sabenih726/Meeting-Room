import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="User Guidelines Projektor & Camera Meeting", 
    layout="wide",
    page_icon="🎥",
    initial_sidebar_state="collapsed"
)

# ============ LOAD GAMBAR ============
@st.cache_data
def load_image(path):
    try:
        return Image.open(path)
    except:
        st.error(f"⚠️ Gambar tidak ditemukan: {path}")
        return None

# ============ STYLING CSS LENGKAP ============
st.markdown("""
    <style>
        /* ========== RESET & BASE STYLES ========== */
        * {
            box-sizing: border-box;
        }
        
        body {
            background-color: #f0f2f6;
        }
        
        .stApp {
            background-color: #f0f2f6;
        }
        
        .main {
            padding-top: 1rem;
        }
        
        /* ========== TYPOGRAPHY ========== */
        h1, h2, h3 {
            color: #003366 !important;
        }
        
        .title-header {
            font-size: 32px;
            font-weight: bold;
            color: #1a237e;
            margin-bottom: 0;
        }
        
        .subtitle {
            font-size: 18px;
            color: #424242;
            margin-top: 10px;
        }
        
        /* ========== DROPDOWN SELECTBOX STYLES ========== */
        
        /* Container utama selectbox */
        .stSelectbox {
            color-scheme: light;
        }
        
        /* Label selectbox */
        .stSelectbox > label {
            color: #1a237e !important;
            font-weight: 600;
            font-size: 16px;
            margin-bottom: 8px;
        }
        
        /* Dropdown trigger button */
        .stSelectbox > div > div > div {
            background-color: white !important;
            border: 2px solid #1976D2 !important;
            border-radius: 10px !important;
            padding: 10px 15px !important;
        }
        
        /* Text inside dropdown */
        .stSelectbox [data-baseweb="select"] > div,
        .stSelectbox [data-baseweb="select"] span,
        .stSelectbox [data-baseweb="select"] div {
            color: #212121 !important;
            font-size: 16px !important;
        }
        
        /* Dropdown arrow icon */
        .stSelectbox svg {
            fill: #1976D2 !important;
        }
        
        /* Dropdown menu saat dibuka */
        ul[role="listbox"] {
            background-color: white !important;
            border: 1px solid #1976D2 !important;
            border-radius: 8px !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
            margin-top: 4px !important;
        }
        
        /* Each option in dropdown */
        li[role="option"] {
            color: #212121 !important;
            background-color: white !important;
            padding: 12px 16px !important;
            font-size: 15px !important;
        }
        
        /* Option on hover */
        li[role="option"]:hover {
            background-color: #E3F2FD !important;
            color: #1565C0 !important;
            cursor: pointer !important;
        }
        
        /* Selected option */
        li[role="option"][aria-selected="true"] {
            background-color: #BBDEFB !important;
            color: #0D47A1 !important;
            font-weight: 600 !important;
        }
        
        /* ========== KONTROL UKURAN GAMBAR (MAIN SECTION) ========== */
        
        /* Container gambar - Center alignment */
        .stImage {
            text-align: center;
            margin: 20px 0;
        }
        
        /* Default: Semua gambar maksimal 500px */
        .stImage > img {
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            max-width: 500px !important;
            width: auto !important;
            height: auto !important;
            margin: 15px auto;
            display: block;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        /* Hover effect pada gambar */
        .stImage > img:hover {
            transform: scale(1.02);
            box-shadow: 0 4px 16px rgba(0,0,0,0.15);
            cursor: pointer;
        }
        
        /* Caption styling - lebih jelas */
        .stImage > figcaption {
            font-size: 14px !important;
            color: #666 !important;
            font-style: italic;
            margin-top: 10px;
            text-align: center;
            line-height: 1.4;
        }
        
        /* ========== UKURAN GAMBAR BERDASARKAN LOKASI ========== */
        
        /* Gambar di dalam kolom (lebih kecil) */
        .stColumn .stImage > img {
            max-width: 320px !important;
        }
        
        /* Gambar di kolom kanan (biasanya lebih kecil) */
        .stColumn:nth-child(2) .stImage > img {
            max-width: 280px !important;
        }
        
        /* Gambar di kolom tengah (sedang) */
        .stColumn:nth-child(3) .stImage > img {
            max-width: 400px !important;
        }
        
        /* Gambar dalam expander (sedang) */
        .streamlit-expanderContent .stImage > img {
            max-width: 450px !important;
        }
        
        /* Gambar dalam expander yang terbuka (expanded) */
        details[open] .stImage > img {
            max-width: 480px !important;
        }
        
        /* Gambar di container utama (lebih besar) */
        .main > .block-container .stImage > img {
            max-width: 600px !important;
        }
        
        /* ========== UKURAN KHUSUS BERDASARKAN JENIS ========== */
        
        /* Screenshot besar (untuk diagram/flowchart) */
        .stImage[data-testid*="screenshot"] > img,
        .stImage.large-image > img {
            max-width: 700px !important;
        }
        
        /* Gambar kecil (icon/button) */
        .stImage.small-image > img {
            max-width: 200px !important;
        }
        
        /* Gambar medium (ilustrasi) */
        .stImage.medium-image > img {
            max-width: 400px !important;
        }
        
        /* ========== RESPONSIVE BREAKPOINTS ========== */
        
        /* Tablet (max-width: 1024px) */
        @media (max-width: 1024px) {
            .stImage > img {
                max-width: 450px !important;
            }
            
            .stColumn .stImage > img {
                max-width: 280px !important;
            }
        }
        
        /* Mobile Large (max-width: 768px) */
        @media (max-width: 768px) {
            .stImage > img {
                max-width: 100% !important;
                max-height: 400px !important;
            }
            
            .stColumn .stImage > img {
                max-width: 100% !important;
            }
            
            /* Di mobile, gambar dalam kolom juga full width */
            .stColumn:nth-child(2) .stImage > img {
                max-width: 100% !important;
            }
        }
        
        /* Mobile Small (max-width: 480px) */
        @media (max-width: 480px) {
            .stImage > img {
                max-width: 100% !important;
                max-height: 300px !important;
            }
            
            .stImage > figcaption {
                font-size: 12px !important;
            }
        }
        
        /* ========== LAYOUT KOLOM ========== */
        
        /* Kolom dengan rasio 3:2 (teks lebih besar) */
        .row-widget.stColumns > div:nth-child(1) {
            flex: 3;
        }
        
        .row-widget.stColumns > div:nth-child(2) {
            flex: 2;
        }
        
        /* ========== HIDE SIDEBAR ========== */
        [data-testid="stSidebar"] {
            display: none;
        }
        
        /* ========== DIVIDER ========== */
        hr {
            margin: 2rem 0;
            border: none;
            border-top: 2px solid #e0e0e0;
        }
        
        .stDivider {
            margin: 1.5rem 0;
        }
        
        /* ========== ALERT BOXES ========== */
        .stAlert {
            border-radius: 8px;
            padding: 15px;
            margin: 15px 0;
        }
        
        .stAlert > div {
            padding: 5px 0;
        }
        
        /* Info box */
        .stAlert[data-baseweb="notification"][kind="info"] {
            background-color: #E3F2FD;
            border-left: 4px solid #1976D2;
        }
        
        /* Warning box */
        .stAlert[data-baseweb="notification"][kind="warning"] {
            background-color: #FFF3E0;
            border-left: 4px solid #F57C00;
        }
        
        /* Success box */
        .stAlert[data-baseweb="notification"][kind="success"] {
            background-color: #E8F5E9;
            border-left: 4px solid #388E3C;
        }
        
        /* Error box */
        .stAlert[data-baseweb="notification"][kind="error"] {
            background-color: #FFEBEE;
            border-left: 4px solid #D32F2F;
        }
        
        /* ========== EXPANDER STYLES ========== */
        .streamlit-expanderHeader {
            font-size: 16px;
            font-weight: 600;
            color: #1a237e;
            background-color: #f5f5f5;
            border-radius: 8px;
            padding: 12px 16px;
        }
        
        .streamlit-expanderHeader:hover {
            background-color: #e0e0e0;
        }
        
        .streamlit-expanderContent {
            padding: 20px 10px;
            border-left: 2px solid #1976D2;
            margin-left: 10px;
        }
        
        /* ========== BUTTONS ========== */
        .stButton > button {
            background-color: #1976D2;
            color: white;
            border-radius: 8px;
            padding: 10px 24px;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background-color: #1565C0;
            box-shadow: 0 4px 12px rgba(25, 118, 210, 0.3);
            transform: translateY(-2px);
        }
        
        /* ========== CONTAINERS & SPACING ========== */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }
        
        .element-container {
            margin-bottom: 1rem;
        }
        
        /* ========== SCROLLBAR CUSTOM ========== */
        ::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #1976D2;
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #1565C0;
        }
        
        /* ========== SPECIAL CLASSES (untuk custom usage) ========== */
        
        /* Class untuk gambar full width */
        .full-width-image {
            max-width: 100% !important;
        }
        
        /* Class untuk gambar thumbnail */
        .thumbnail-image {
            max-width: 150px !important;
        }
        
        /* Class untuk gambar hero/banner */
        .hero-image {
            max-width: 900px !important;
        }
        
        /* ========== UTILITIES ========== */
        
        /* Center content */
        .center-content {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        /* Text alignment */
        .text-center {
            text-align: center;
        }
        
        .text-left {
            text-align: left;
        }
        
        .text-right {
            text-align: right;
        }
        
        /* Spacing utilities */
        .mt-1 { margin-top: 0.5rem; }
        .mt-2 { margin-top: 1rem; }
        .mt-3 { margin-top: 1.5rem; }
        .mt-4 { margin-top: 2rem; }
        
        .mb-1 { margin-bottom: 0.5rem; }
        .mb-2 { margin-bottom: 1rem; }
        .mb-3 { margin-bottom: 1.5rem; }
        .mb-4 { margin-bottom: 2rem; }
        
        /* ========== DARK MODE OVERRIDE (jika diperlukan) ========== */
        @media (prefers-color-scheme: dark) {
            .stSelectbox, 
            .stSelectbox *,
            [data-baseweb="select"],
            [data-baseweb="select"] * {
                color: #212121 !important;
                background-color: white !important;
            }
            
            /* Paksa gambar tetap terlihat di dark mode */
            .stImage > img {
                background-color: white;
                padding: 5px;
            }
        }
        
        /* ========== PRINT STYLES ========== */
        @media print {
            .stImage > img {
                max-width: 100% !important;
                page-break-inside: avoid;
            }
            
            .stButton, .stSelectbox {
                display: none;
            }
        }
        
    </style>
""", unsafe_allow_html=True)

# ============ HEADER ============
col1, col2 = st.columns([1, 8])
with col1:
    logo = load_image("assets/logo_trakindo.png")
    if logo:
        st.image(logo, width=400)
with col2:
    st.markdown("<div class='title-header'>User Guidelines Projektor & Camera Meeting</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Panduan lengkap untuk membantu Anda menghubungkan laptop ke proyektor dan menggunakan kamera Kandao Meeting Pro dengan mudah.</div>", unsafe_allow_html=True)

st.markdown("")  # Spacing

# ============ DROPDOWN NAVIGATION ============
col_left, col_center, col_right = st.columns([1, 3, 1])

with col_center:
    page = st.selectbox(
        "📖 Pilih Panduan:",
        [
            "🏠 Beranda",
            "📺 Panduan Proyektor",
            "📷 Panduan Kamera",
            "🎛️ Remote & Fitur",
            "❓ FAQ & Troubleshooting"
        ],
        index=0,
        help="Pilih panduan yang ingin Anda pelajari",
        label_visibility="visible"
    )

st.markdown("---")

# Clean page name (remove emoji)
page_clean = page.split(" ", 1)[1] if " " in page else page

# ============ HALAMAN BERANDA ============
if page_clean == "Beranda":
    
    # Welcome Section
    st.markdown("### 👋 Selamat Datang!")
    st.info("📌 **Silakan pilih panduan dari menu dropdown di atas untuk memulai.**")
    
    st.markdown("")
    
    # Quick Links Cards
    st.markdown("### 🚀 Akses Cepat")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown("""
                <div style='padding: 20px; background-color: white; border-radius: 10px; border-left: 4px solid #1976D2;'>
                    <h4 style='margin-top:0; color: #1976D2;'>📺 Panduan Proyektor</h4>
                    <p>Pelajari cara menyambungkan laptop ke proyektor menggunakan:</p>
                    <ul>
                        <li>Shortcut keyboard (Windows + K)</li>
                        <li>Kabel HDMI/VGA</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown("""
                <div style='padding: 20px; background-color: white; border-radius: 10px; border-left: 4px solid #1976D2;'>
                    <h4 style='margin-top:0; color: #1976D2;'>📷 Panduan Kamera</h4>
                    <p>Setup dan penggunaan Kamera Kandao Meeting Pro:</p>
                    <ul>
                        <li>Koneksi ke laptop</li>
                        <li>Koneksi ke proyektor</li>
                        <li>Topologi sistem</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("")
    
    col3, col4 = st.columns(2)
    
    with col3:
        with st.container():
            st.markdown("""
                <div style='padding: 20px; background-color: white; border-radius: 10px; border-left: 4px solid #1976D2;'>
                    <h4 style='margin-top:0; color: #1976D2;'>🎛️ Remote & Fitur</h4>
                    <p>Panduan penggunaan remote control dan fitur unggulan kamera Kandao</p>
                </div>
            """, unsafe_allow_html=True)
    
    with col4:
        with st.container():
            st.markdown("""
                <div style='padding: 20px; background-color: white; border-radius: 10px; border-left: 4px solid #1976D2;'>
                    <h4 style='margin-top:0; color: #1976D2;'>❓ FAQ & Troubleshooting</h4>
                    <p>Solusi untuk masalah umum dan kontak bantuan</p>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("")
    st.success("💡 **Tips:** Gunakan menu dropdown di atas untuk navigasi cepat antar panduan!")

# ============ HALAMAN PANDUAN PROYEKTOR ============
# ============ HALAMAN PANDUAN PROYEKTOR (REVISED) ============
elif page_clean == "Panduan Proyektor":
    st.title("📺 Panduan Menyambungkan Proyektor")
    
    # Metode A
    st.markdown("### 🔹 A. Menggunakan Shortcut Keyboard")
    
    with st.expander("📖 Lihat Langkah-langkah", expanded=True):
        st.markdown("""
        **Langkah-langkah:**
        
        1. **Pastikan proyektor menyala** (tekan tombol power di remote proyektor)
        2. **Tekan kombinasi tombol** `Windows + K` pada keyboard laptop Anda
        3. **Pilih nama ruang meeting** yang muncul di layar
        """)
        
        st.markdown("")
        
        img = load_image("assets/windows_k_shortcut.png")
        if img:
            # Gambar di tengah dengan ukuran sedang
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(img, caption="Shortcut Windows + K", width=400)
    
    st.divider()
    
    # Metode B
    st.markdown("### 🔹 B. Menggunakan Kabel HDMI/VGA")
    
    with st.expander("📖 Lihat Langkah-langkah", expanded=True):
        
        # Langkah 1
        st.markdown("#### **Langkah 1: Sambungkan Kabel**")
        col1, col2 = st.columns([3, 2])  # Teks lebih besar dari gambar
        
        with col1:
            st.markdown("""
            - Ambil kabel HDMI atau VGA yang tersedia
            - Sambungkan satu ujung ke proyektor
            - Sambungkan ujung lainnya ke port laptop Anda
            - Pastikan kabel terpasang dengan kencang
            """)
        
        with col2:
            img = load_image("assets/colokan_hdmi.png")
            if img:
                st.image(img, caption="Port HDMI", width=250)  # Ukuran kecil
        
        st.markdown("---")
        
        # Langkah 2
        st.markdown("#### **Langkah 2: Pilih Input**")
        col3, col4 = st.columns([3, 2])
        
        with col3:
            st.markdown("""
            - Gunakan remote proyektor
            - Pilih input HDMI atau VGA sesuai kabel yang digunakan
            - Tunggu beberapa saat hingga layar terdeteksi
            - Jika tidak muncul, tekan `Windows + P` dan pilih "Duplicate"
            """)
        
        with col4:
            img = load_image("assets/home_screen_hdmi.png")
            if img:
                st.image(img, caption="Pilih Input HDMI", width=250)
        
        st.markdown("---")
        
        # Langkah 3
        st.markdown("#### **Langkah 3: Verifikasi Koneksi**")
        st.markdown("""
        - Jika berhasil, tampilan laptop akan muncul di layar proyektor
        - Sesuaikan resolusi jika diperlukan melalui `Settings > Display`
        - Atur mode tampilan: Duplicate (sama) atau Extend (perpanjang)
        """)
        
        st.markdown("")
        
        img = load_image("assets/Picture11.png")
        if img:
            # Gambar lebih besar untuk screenshot penting
            col1, col2, col3 = st.columns([1, 3, 1])
            with col2:
                st.image(img, caption="Tampilan Proyektor Berhasil Terhubung", width=600)
    
    st.markdown("")
    
    # Warning
    st.warning("🔌 **Penting:** Jangan lupa matikan proyektor setelah selesai digunakan untuk menghemat energi!")
    
    img = load_image("assets/Picture12.png")
    if img:
        col1, col2, col3 = st.columns([1.5, 2, 1.5])
        with col2:
            st.image(img, caption="Tekan tombol Power Off pada remote", width=350)

# ============ HALAMAN PANDUAN KAMERA ============
# ============ HALAMAN PANDUAN KAMERA (REVISED) ============
elif page_clean == "Panduan Kamera":
    st.title("📷 Panduan Penggunaan Kamera Kandao Meeting Pro")
    
    # Metode A - Koneksi ke Laptop
    st.markdown("### 🔹 A. Koneksi ke Laptop")
    
    with st.expander("📖 Lihat Langkah-langkah", expanded=True):
        
        # Teks penjelasan di atas
        st.markdown("""
        **Langkah-langkah:**
        
        1. **Aktifkan kamera Kandao**
           - Tekan dan tahan tombol **ON/OFF** pada kamera
           - Tunggu hingga lampu indikator menyala
        
        2. **Hubungkan ke laptop**
           - Gunakan kabel **USB OUT** yang tersedia
           - Sambungkan ke port USB laptop Anda
        
        3. **Buka aplikasi meeting**
           - Jalankan **Zoom**, **Microsoft Teams**, atau aplikasi meeting lainnya
        
        4. **Pilih kamera di pengaturan**
           - Masuk ke Settings > Video/Camera
           - Pilih **Kandao Meeting Pro** sebagai kamera
        
        5. **Verifikasi koneksi**
           - Pastikan **lampu biru** pada kamera menyala
           - Cek preview video di aplikasi meeting
        """)
        
        st.markdown("---")
        st.markdown("**Ilustrasi:**")
        
        # Gambar di bawah dengan ukuran sedang
        col1, col2 = st.columns(2)
        
        with col1:
            img = load_image("assets/kandao_power_button.png")
            if img:
                st.image(img, caption="Tombol Power Kamera Kandao", width=300)
        
        with col2:
            img = load_image("assets/Picture15.png")
            if img:
                st.image(img, caption="Koneksi Kamera ke Laptop", width=300)
    
    st.divider()
    
    # Metode B - Koneksi ke Proyektor
    st.markdown("### 🔹 B. Koneksi ke Proyektor")
    
    with st.expander("📖 Lihat Langkah-langkah", expanded=True):
        
        st.markdown("""
        **Langkah-langkah:**
        
        1. **Hubungkan kabel HDMI**
           - Sambungkan kamera ke layar/monitor melalui kabel **HDMI**
        
        2. **Aktifkan kamera**
           - Nyalakan kamera jika belum aktif
           - Pastikan proyektor juga sudah menyala
        
        3. **Sambungkan ke Wi-Fi**
           - Akses menu Wi-Fi pada kamera
           - Pilih jaringan **TU MOBILE**
           - Masukkan password jika diminta
        
        4. **Verifikasi koneksi**
           - Pastikan **lampu biru** menyala sebagai indikator koneksi aktif
           - Layar proyektor seharusnya menampilkan output kamera
        """)
        
        st.markdown("---")
        st.markdown("**Ilustrasi:**")
        
        img = load_image("assets/Picture13.png")
        if img:
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(img, caption="Koneksi Kamera ke Proyektor", width=450)
    
    st.divider()
    
    # Topologi Sistem
    st.markdown("### 🔹 C. Flowchart Topologi Penggunaan Kamera Kandao")
    
    with st.expander("📖 Lihat Diagram Topologi", expanded=True):
        
        st.markdown("""
        **Alur Koneksi:**
        
        1. **Hubungkan ADAPTER ke Device**
           - Gunakan kabel USB Type-C to Type-C
           - Sambungkan ke sumber listrik
        
        2. **Nyalakan Kamera**
           - Tekan tombol power
           - Pastikan lampu indikator menyala (hijau/biru)
        
        3. **Hubungkan HDMI ke Proyektor**
           - Sambungkan kabel HDMI dari port kamera ke proyektor
           - Pilih input HDMI di proyektor
        
        4. **Verifikasi Display**
           - Kamera sudah terdisplay di screen projector
           - Interface kamera terlihat di layar
        
        5. **Mulai Meeting**
           - Buka aplikasi meeting yang digunakan
           - Terima undangan meeting menggunakan remote control
           - Mulai presentasi atau video conference
        """)
        
        st.markdown("---")
        st.markdown("**Diagram Topologi:**")
        
        img = load_image("assets/Picture14.png")
        if img:
            # Diagram bisa agak besar karena perlu detail
            col1, col2, col3 = st.columns([0.5, 3, 0.5])
            with col2:
                st.image(img, caption="Topologi Sistem Kamera Kandao", width=700)
        
        st.markdown("")
        st.info("💡 **Catatan:** Pastikan semua kabel terpasang dengan benar dan kencang untuk menghindari gangguan koneksi.")

# ============ HALAMAN REMOTE & FITUR ============
elif page_clean == "Remote & Fitur":
    st.title("🎛️ Remote Control & Fitur Kamera Kandao")
    
    # Fungsi Remote
    st.markdown("### 🔹 Fungsi Remote Control")
    
    with st.expander("📖 Lihat Detail Fungsi Remote", expanded=True):
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("""
            **Tombol dan Fungsinya:**
            
            1. **Tombol Daya (Power)**
               - Nyalakan/matikan kamera
               - Tekan dan tahan selama 2-3 detik
            
            2. **Mode Mouse**
               - Aktifkan untuk navigasi kursor pada layar
               - Gunakan directional pad untuk menggerakkan kursor
               - Tekan OK untuk klik
            
            3. **Volume +/-**
               - Atur volume speaker kamera
               - Volume+ untuk menaikkan
               - Volume- untuk menurunkan
            
            4. **Tombol Mikrofon (Mute)**
               - Aktifkan/nonaktifkan audio
               - Indikator LED akan berubah warna saat mute
            
            5. **Directional Pad (Atas/Bawah/Kiri/Kanan)**
               - Navigasi menu pada interface kamera
               - Kontrol pointer di mode mouse
            
            6. **Tombol OK/Enter**
               - Konfirmasi pilihan
               - Klik saat mode mouse aktif
            
            7. **Tombol Back/Return**
               - Kembali ke menu sebelumnya
               - Batalkan aksi
            """)
        
        with col2:
            img = load_image("assets/kandao_remote_buttons.png")
            if img:
                st.image(img, caption="Remote Control Kamera Kandao", use_container_width=True)
        
        st.markdown("")
        st.warning("⚠️ **Perhatian:** Arahkan remote ke sensor IR pada kamera untuk respons optimal (jarak maksimal ~5 meter)")
    
    st.divider()
    
    # Fitur Unggulan
    st.markdown("### 🔹 Fitur Unggulan Kamera Kandao Meeting Pro")
    
    with st.expander("📖 Lihat Fitur Lengkap", expanded=True):
        
        # Feature Grid
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
                <div style='padding: 20px; background-color: #E3F2FD; border-radius: 10px; text-align: center;'>
                    <h3 style='color: #1976D2;'>🎙️</h3>
                    <h4 style='margin-top:0;'>Audio Jernih</h4>
                    <p style='font-size: 14px;'>
                    • 8 Microphone Array<br>
                    • Noise Cancellation<br>
                    • Echo Reduction<br>
                    • 360° Audio Pickup
                    </p>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
                <div style='padding: 20px; background-color: #E8F5E9; border-radius: 10px; text-align: center;'>
                    <h3 style='color: #388E3C;'>🎥</h3>
                    <h4 style='margin-top:0;'>Video Berkualitas Tinggi</h4>
                    <p style='font-size: 14px;'>
                    • 360° Panoramic View<br>
                    • 4K Resolution<br>
                    • Auto Focus & Tracking<br>
                    • Wide Dynamic Range
                    </p>
                </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
                <div style='padding: 20px; background-color: #FFF3E0; border-radius: 10px; text-align: center;'>
                    <h3 style='color: #F57C00;'>⚡</h3>
                    <h4 style='margin-top:0;'>Kemudahan Instalasi</h4>
                    <p style='font-size: 14px;'>
                    • Plug & Play<br>
                    • Multi-platform Support<br>
                    • Wireless Connectivity<br>
                    • Remote Control
                    </p>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("")
        
        # Additional Features
        st.markdown("**Fitur Tambahan:**")
        
        col4, col5 = st.columns(2)
        
        with col4:
            st.markdown("""
            - ✅ **Smart Tracking:** Kamera otomatis mengikuti pembicara
            - ✅ **Multi-view Mode:** Tampilan split screen untuk peserta berbeda
            - ✅ **AI-Powered:** Teknologi kecerdasan buatan untuk framing optimal
            - ✅ **Low Light Performance:** Performa baik di kondisi cahaya minim
            """)
        
        with col5:
            st.markdown("""
            - ✅ **Compatible:** Zoom, Teams, Google Meet, Skype, dll
            - ✅ **Wireless Presentation:** Screen mirroring tanpa kabel
            - ✅ **Recording:** Rekam meeting langsung dari device
            - ✅ **Cloud Integration:** Sinkronisasi dengan cloud storage
            """)
        
        st.markdown("")
        
        img = load_image("assets/kandao_features_summary.png.png")
        if img:
            st.image(img, caption="Ringkasan Fitur Kamera Kandao Meeting Pro", use_container_width=True)
    
    st.markdown("")
    st.success("🌟 **Pro Tip:** Manfaatkan fitur auto-tracking untuk presentasi yang lebih dinamis dan profesional!")

# ============ HALAMAN FAQ & TROUBLESHOOTING ============
elif page_clean == "FAQ & Troubleshooting":
    st.title("❓ FAQ & Troubleshooting")
    
    st.markdown("### 🔧 Solusi Masalah Umum")
    
    # Problem 1 - Proyektor
    with st.expander("❌ Proyektor tidak terdeteksi?", expanded=False):
        st.markdown("""
        **Kemungkinan Penyebab & Solusi:**
        
        1. **Proyektor belum menyala**
           - ✅ Cek apakah proyektor sudah dinyalakan
           - ✅ Pastikan indikator power menyala
           - ✅ Tunggu 30-60 detik untuk warm-up proyektor
        
        2. **Masalah pada kabel**
           - ✅ Pastikan kabel terpasang dengan benar di kedua ujung
           - ✅ Coba gunakan kabel HDMI/VGA lain
           - ✅ Periksa kondisi fisik kabel (tidak bengkok/rusak)
        
        3. **Port laptop bermasalah**
           - ✅ Coba port HDMI/VGA lain jika tersedia
           - ✅ Bersihkan port dari debu
           - ✅ Test dengan perangkat lain untuk verifikasi
        
        4. **Pengaturan display belum benar**
           - ✅ Tekan `Windows + P` untuk memilih mode display
           - ✅ Pilih "Duplicate" atau "Extend"
           - ✅ Refresh detection dengan `Windows + Ctrl + Shift + B`
        
        5. **Driver display perlu update**
           - ✅ Update driver graphics card
           - ✅ Restart laptop setelah update
        """)
        
        st.info("💡 **Quick Fix:** Tekan `Windows + P` → Pilih 'Duplicate' → Tunggu 5 detik")
    
    # Problem 2 - Kamera tidak muncul
    with st.expander("❌ Kamera tidak muncul di Zoom/Teams?", expanded=False):
        st.markdown("""
        **Kemungkinan Penyebab & Solusi:**
        
        1. **Koneksi USB bermasalah**
           - ✅ Pastikan kabel USB terpasang dengan baik
           - ✅ Coba port USB lain
           - ✅ Gunakan port USB 3.0 untuk performa optimal
           - ✅ Hindari menggunakan USB hub, sambungkan langsung
        
        2. **Kamera belum dipilih di aplikasi**
           - ✅ Buka Settings di Zoom/Teams
           - ✅ Masuk ke menu Video/Camera
           - ✅ Pilih **Kandao Meeting Pro** dari dropdown
           - ✅ Klik "Test Video" untuk verifikasi
        
        3. **Aplikasi belum memiliki permission**
           - ✅ Windows Settings > Privacy > Camera
           - ✅ Pastikan "Allow apps to access camera" ON
           - ✅ Scroll ke Zoom/Teams dan enable access
        
        4. **Kamera digunakan aplikasi lain**
           - ✅ Tutup aplikasi yang mungkin menggunakan kamera
           - ✅ Task Manager > End task untuk aplikasi video
           - ✅ Restart Zoom/Teams
        
        5. **Software kamera perlu update**
           - ✅ Cek website Kandao untuk driver terbaru
           - ✅ Install/update Kandao Meeting software
           - ✅ Restart komputer setelah instalasi
        """)
        
        st.warning("⚠️ **Penting:** Pastikan hanya 1 aplikasi yang menggunakan kamera pada satu waktu")
    
    # Problem 3 - Audio issues
    with st.expander("❌ Audio kamera tidak terdengar?", expanded=False):
        st.markdown("""
        **Kemungkinan Penyebab & Solusi:**
        
        1. **Kamera dalam mode mute**
           - ✅ Periksa indikator mute pada kamera (LED merah)
           - ✅ Tekan tombol mute di remote untuk unmute
           - ✅ Cek icon mute di aplikasi meeting
        
        2. **Volume terlalu rendah**
           - ✅ Naikkan volume menggunakan remote kamera
           - ✅ Naikkan volume system Windows
           - ✅ Cek volume di aplikasi Zoom/Teams
        
        3. **Microphone tidak dipilih**
           - ✅ Settings > Audio di Zoom/Teams
           - ✅ Pilih **Kandao Meeting Pro** sebagai microphone
           - ✅ Test microphone
        
        4. **Audio driver issue**
           - ✅ Update audio driver
           - ✅ Restart audio service di Windows
           - ✅ Cabut dan pasang kembali USB
        """)
    
    # Problem 4 - Remote tidak respon
    with st.expander("❌ Remote control tidak berfungsi?", expanded=False):
        st.markdown("""
        **Kemungkinan Penyebab & Solusi:**
        
        1. **Baterai remote habis**
           - ✅ Ganti dengan baterai baru (AAA)
           - ✅ Pastikan polaritas baterai benar (+/-)
        
        2. **Jarak terlalu jauh**
           - ✅ Arahkan remote ke sensor IR kamera
           - ✅ Jarak maksimal ~5 meter
           - ✅ Pastikan tidak ada penghalang
        
        3. **Sensor IR tertutup/kotor**
           - ✅ Bersihkan sensor IR di kamera
           - ✅ Bersihkan LED di ujung remote
        
        4. **Remote perlu di-pair ulang**
           - ✅ Lihat manual untuk pairing procedure
           - ✅ Reset kamera dan pair ulang
        """)
    
    # Problem 5 - Koneksi WiFi
    with st.expander("❌ Tidak bisa connect ke WiFi TU MOBILE?", expanded=False):
        st.markdown("""
        **Kemungkinan Penyebab & Solusi:**
        
        1. **Password WiFi salah**
           - ✅ Verifikasi password dengan IT Support
           - ✅ Perhatikan huruf besar/kecil
        
        2. **WiFi kamera tidak aktif**
           - ✅ Masuk ke Settings kamera
           - ✅ Enable WiFi module
           - ✅ Scan ulang network available
        
        3. **Signal lemah**
           - ✅ Pindahkan kamera lebih dekat ke access point
           - ✅ Cek apakah WiFi sedang maintenance
        
        4. **MAC address belum terdaftar**
           - ✅ Hubungi IT untuk whitelist MAC address
           - ✅ Berikan MAC address kamera
        """)
    
    st.divider()
    
    # Tips & Best Practices
    st.markdown("### 💡 Tips & Best Practices")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Sebelum Meeting:**
        - ✅ Test equipment 15 menit sebelum meeting
        - ✅ Charge/ganti baterai remote
        - ✅ Pastikan semua kabel tersedia
        - ✅ Test audio & video di aplikasi
        - ✅ Tutup aplikasi yang tidak perlu
        """)
    
    with col2:
        st.markdown("""
        **Setelah Meeting:**
        - ✅ Matikan proyektor & kamera
        - ✅ Cabut semua kabel dengan hati-hati
        - ✅ Rapikan kabel & remote
        - ✅ Laporkan jika ada kerusakan
        - ✅ Feedback untuk perbaikan
        """)
    
    st.divider()
    
    # Kontak Bantuan
    st.markdown("### 📞 Kontak Bantuan")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div style='padding: 20px; background-color: #E3F2FD; border-radius: 10px; text-align: center;'>
                <h3 style='color: #1976D2;'>🏢</h3>
                <h4 style='margin-top:0;'>Facility Team</h4>
                <p style='font-size: 14px;'>
                Untuk masalah hardware:<br>
                proyektor, kabel, remote
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='padding: 20px; background-color: #E8F5E9; border-radius: 10px; text-align: center;'>
                <h3 style='color: #388E3C;'>💻</h3>
                <h4 style='margin-top:0;'>IT Support</h4>
                <p style='font-size: 14px;'>
                Untuk masalah software:<br>
                driver, aplikasi, network
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div style='padding: 20px; background-color: #FFF3E0; border-radius: 10px; text-align: center;'>
                <h3 style='color: #F57C00;'>📱</h3>
                <h4 style='margin-top:0;'>Helpdesk</h4>
                <p style='font-size: 14px;'>
                Emergency support:<br>
                Hubungi melalui grup internal
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("")
    
    st.info("""
    📧 **Cara Menghubungi:**
    - Grup Internal Telegram/WhatsApp
    - Email ke IT Support: itsupport@company.com
    - Telepon: ext. 1234 (Facility) | ext. 5678 (IT)
    - Ticketing System: helpdesk.company.com
    """)
    
    st.success("✅ **Saat menghubungi bantuan, siapkan informasi:** Nama ruang meeting, jenis masalah, screenshot error (jika ada)")

# ============ FOOTER ============
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; font-size: 14px; padding: 20px;'>
        <p>© 2024 Trakindo - User Guidelines Projektor & Camera Meeting</p>
        <p>Terakhir diupdate: Januari 2024 | Version 1.0</p>
    </div>
""", unsafe_allow_html=True)
