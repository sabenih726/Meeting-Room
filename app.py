import streamlit as st
from PIL import Image

st.set_page_config(page_title="User Guidelines Projektor & Camera Meeting", layout="wide")

# Load Gambar
@st.cache_data
def load_image(path):
    return Image.open(path)

# Styling tambahan
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .stApp {
            background-color: #f0f2f6;
        }
        .main {
            padding-top: 1rem;
        }
        h1, h2, h3 {
            color: #003366;
        }
        .title-header {
            font-size: 32px;
            font-weight: bold;
            color: #1a237e;
        }
        .subtitle {
            font-size: 18px;
            color: #424242;
        }
    </style>
""", unsafe_allow_html=True)

# Navigasi
page = st.radio("📖 Pilih Halaman:", 
                ("Beranda", "Panduan Proyektor", "Panduan Kamera", "Remote & Fitur", "FAQ & Troubleshooting"),
                horizontal=True)

# Halaman Beranda
if page == "Beranda":
    col1, col2 = st.columns([1, 8])
    with col1:
        st.image(load_image("assets/logo_trakindo.png"), width=400)
    with col2:
        st.markdown("<div class='title-header'>Panduan Proyektor dan Kamera Kandao</div>", unsafe_allow_html=True)
        st.markdown("<div class='subtitle'>Website ini dirancang untuk membantu Anda menghubungkan laptop ke proyektor dan menggunakan kamera Kandao Meeting Pro dengan mudah.</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.info("📌 **Silakan pilih panduan dari menu di atas untuk memulai.**")

# Halaman Panduan Proyektor
elif page == "Panduan Proyektor":
    st.title("📺 Panduan Menyambungkan Proyektor")

    st.markdown("#### A. Menggunakan Shortcut Keyboard")
    st.write("1. Pastikan proyektor menyala (tombol power di remote).")
    st.write("2. Tekan tombol `Windows + K` pada laptop Anda.")
    st.image(load_image("assets/windows_k_shortcut.png"), caption="Shortcut Windows + K")
    st.write("3. Pilih nama ruang meeting yang muncul.")

    st.divider()

    st.markdown("#### B. Menggunakan Kabel HDMI/VGA")
    st.write("1. Sambungkan kabel dari proyektor ke laptop.")
    st.image(load_image("assets/colokan_hdmi.png"), caption="Contoh port HDMI")
    st.write("2. Pilih input HDMI/VGA di layar proyektor.")
    st.image(load_image("assets/home_screen_hdmi.png"), caption="Input HDMI")
    st.write("3. Jika berhasil, tampilan laptop akan muncul di layar.")
    st.image(load_image("assets/Picture11.png"), caption="Tampilan Proyektor")

    st.warning("🔌 **Jangan lupa matikan proyektor setelah digunakan.**")
    st.image(load_image("assets/Picture12.png"), caption="Remote Power Off")

# Halaman Panduan Kamera
elif page == "Panduan Kamera":
    st.title("📷 Panduan Penggunaan Kamera Kandao")

    st.subheader("🔹 A. Koneksi ke Laptop")
    st.markdown("""
    1. Aktifkan kamera Kandao dengan menekan tombol **ON/OFF**.  
    2. Hubungkan kamera ke laptop menggunakan kabel **USB OUT**.  
    3. Buka aplikasi **Zoom** atau **Microsoft Teams**.  
    4. Pilih **Kandao Meeting Pro** di pengaturan kamera.  
    5. Pastikan **lampu biru** menyala.
    """)
    st.image(load_image("assets/kandao_power_button.png"), caption="Tombol Power Kamera")

    st.subheader("🔹 B. Koneksi ke Proyektor")
    st.markdown("""
    1. Hubungkan kamera ke layar/monitor melalui kabel **HDMI**.  
    2. Nyalakan kamera jika belum aktif.  
    3. Sambungkan ke jaringan Wi-Fi **TU MOBILE**.  
    4. Pastikan lampu biru menyala sebagai indikator.
    """)
    st.image(load_image("assets/Picture13.png"), caption="Koneksi Kamera ke Proyektor")
    st.image(load_image("assets/Picture13.png"), caption="Koneksi Kamera ke Proyektor")

    st.subheader("🔸 C. Flowchart Topologi Penggunaan Kamera Kandao")
    st.image(load_image("assets/flowchart_topologi_kandao.png"), caption="Topologi Sistem Kamera Kandao")  # Ganti dengan flowchart Anda

# Halaman Remote & Fitur
elif page == "Remote & Fitur":
    st.title("🎛️ Remote Control & Fitur Kamera Kandao")

    st.subheader("🔹 Fungsi Remote")
    st.markdown("""
    - **Tombol Daya:** Nyalakan/matikan kamera  
    - **Mode Mouse:** Navigasi kursor pada layar  
    - **Volume:** Atur suara  
    - **Mikrofon:** Aktif/nonaktif suara
    """)
    st.image(load_image("assets/kandao_remote_buttons.png"), caption="Remote Kamera")

    st.subheader("🔹 Fitur Unggulan Kamera Kandao Meeting Pro")
    st.markdown("""
    - 🎙️ **Audio Jernih**  
    - 🎥 **Video Berkualitas Tinggi**  
    - ⚡ **Kemudahan Instalasi**
    """)
    st.image(load_image("assets/kandao_features_summary.png.png"), caption="Fitur Unggulan")

# Halaman FAQ & Troubleshooting
elif page == "FAQ & Troubleshooting":
    st.title("❓ FAQ & Troubleshooting")

    st.subheader("🔹 Proyektor tidak terdeteksi?")
    st.markdown("""
    - Cek apakah proyektor sudah menyala.  
    - Ganti kabel HDMI/VGA jika perlu.  
    - Pastikan port laptop tidak bermasalah.
    """)

    st.subheader("🔹 Kamera tidak muncul di Zoom/Teams?")
    st.markdown("""
    - Pastikan kabel USB tersambung dengan baik.  
    - Periksa pengaturan perangkat di aplikasi.  
    - Coba restart Zoom/Teams.
    """)

    st.subheader("🔹 Kontak Bantuan")
    st.markdown("""
    Hubungi tim **Facility** atau **IT Support** untuk bantuan lebih lanjut melalui grup internal atau nomor resmi.
    """)
