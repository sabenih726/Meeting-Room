import streamlit as st
from PIL import Image

st.set_page_config(page_title="Panduan Proyektor & Kamera Kandao", layout="wide")

# Cache gambar agar tidak load berulang
@st.cache_data
def load_image(path):
    return Image.open(path)

# Navigasi halaman dengan radio
page = st.radio("📖 Pilih Halaman:", 
                ("Beranda", "Panduan Proyektor", "Panduan Kamera", "Remote & Fitur", "FAQ & Troubleshooting"),
                horizontal=True)

# Halaman Beranda
if page == "Beranda":
    col1, col2 = st.columns([1, 8])
    with col1:
        st.image(load_image("assets/logo_trakindo.png"), width=80)
    with col2:
        st.title("📽️ Panduan Proyektor dan Kamera Kandao")

    st.write("Selamat datang di panduan interaktif ini. Website ini dirancang untuk membantu Anda menghubungkan laptop ke proyektor dan menggunakan kamera Kandao Meeting Pro dengan mudah.")
    st.markdown("Silakan pilih panduan dari menu di atas.")

# Halaman Panduan Proyektor
elif page == "Panduan Proyektor":
    st.title("📺 Panduan Menyambungkan Proyektor")

    st.markdown("#### A. Menggunakan Shortcut Keyboard")
    st.write("1. Pastikan proyektor menyala (tombol power di remote).")
    st.write("2. Tekan tombol `Windows + K` pada laptop Anda.")
    st.image(load_image("assets/windows_k_shortcut.png"), caption="Shortcut Windows + K")
    st.write("3. Pilih nama ruang meeting yang muncul.")

    st.markdown("---")

    st.markdown("#### B. Menggunakan Kabel HDMI/VGA")
    st.write("1. Sambungkan kabel dari proyektor ke laptop.")
    st.image(load_image("assets/colokan_hdmi.png"), caption="Contoh port HDMI")
    st.write("2. Pilih input HDMI/VGA di layar proyektor.")
    st.image(load_image("assets/home_screen_hdmi.png"), caption="Shortcut port HDMI")
    st.write("3. Jika berhasil, tampilan laptop akan muncul di layar.")
    st.image(load_image("assets/Picture11.png"), caption="Shortcut HDMI")

    st.markdown("> 🔌 **Pastikan untuk mematikan proyektor setelah digunakan.**")
    st.image(load_image("assets/Picture12.png"), caption="Shortcut Remote OFF")

# Halaman Panduan Kamera
elif page == "Panduan Kamera":
    st.title("📷 Panduan Penggunaan Kamera Kandao")

    st.subheader("🔹 A. Koneksi ke Laptop")
    st.markdown("""
    1. Aktifkan kamera Kandao dengan menekan tombol **ON/OFF**.
    2. Hubungkan kamera ke laptop menggunakan kabel **USB OUT**.
    3. Buka aplikasi **Zoom** atau **Microsoft Teams**.
    4. Pada pengaturan kamera dan mikrofon, pilih **Kandao Meeting Pro**.
    5. Pastikan **lampu biru** menyala untuk menandakan koneksi berhasil.
    """)
    st.image(load_image("assets/kandao_power_button.png"), caption="Kandao On Meeting")

    st.subheader("🔹 B. Koneksi ke Proyektor")
    st.markdown("""
    1. Hubungkan kamera ke layar/penampil melalui kabel **HDMI**.
    2. Aktifkan kamera jika belum menyala.
    3. Hubungkan ke jaringan Wi-Fi **TU MOBILE**.
    4. Periksa lampu biru menyala sebagai indikator sukses koneksi.
    """)
    st.image(load_image("assets/Picture13.png"), caption="Kandao Connect Proyektor")

# Halaman Remote & Fitur
elif page == "Remote & Fitur":
    st.title("🎛️ Remote Control & Fitur Kamera Kandao")

    st.subheader("🔹 Fungsi Remote")
    st.markdown("""
    - **Tombol Daya:** Menghidupkan / Mematikan kamera
    - **Mode Mouse:** Menggerakkan kursor pada layar
    - **Volume:** Menyesuaikan volume suara
    - **Mikrofon:** Mute/unmute suara
    """)
    st.image(load_image("assets/kandao_remote_buttons.png"), caption="Fungsi Remote")

    st.subheader("🔹 Fitur Unggulan Kamera Kandao Meeting Pro")
    st.markdown("""
    - **Audio Jernih:** Mikrofon internal menangkap suara dengan jelas.
    - **Video Berkualitas Tinggi:** Gambar tajam dan detail untuk semua peserta rapat.
    - **Kemudahan Penggunaan:** Instalasi cepat tanpa konfigurasi rumit.
    """)
    st.image(load_image("assets/kandao_features_summary.png.png"), caption="Fitur Unggulan Kamera Kandao Meeting Pro")

# Halaman FAQ & Troubleshooting
elif page == "FAQ & Troubleshooting":
    st.title("❓ FAQ & Troubleshooting")

    st.subheader("🔹 Proyektor tidak terdeteksi?")
    st.markdown("""
    - Pastikan proyektor dalam kondisi menyala.
    - Coba gunakan kabel HDMI/VGA lain.
    - Cek apakah port HDMI/VGA laptop berfungsi normal.
    """)

    st.subheader("🔹 Kamera tidak muncul di Zoom/Teams?")
    st.markdown("""
    - Pastikan kabel USB terpasang dengan benar.
    - Periksa pengaturan kamera dan pilih *Kandao Meeting Pro*.
    - Restart aplikasi Zoom/Teams jika belum muncul.
    """)

    st.subheader("🔹 Siapa yang bisa dihubungi jika ada kendala?")
    st.markdown("""
    - Hubungi tim **Facility** atau **IT Support** melalui grup internal atau nomor yang disediakan.
    """)
