import streamlit as st

st.set_page_config(page_title="Panduan Proyektor & Kamera Kandao", layout="wide")

# Sidebar navigasi
st.sidebar.title("Menu Panduan")
menu = st.sidebar.radio("Pilih Halaman:", [
    "Beranda",
    "Panduan Proyektor",
    "Panduan Kamera",
    "Remote & Fitur",
    "FAQ & Troubleshooting"
])

# Halaman Beranda
if menu == "Beranda":
    st.title("📽️ Panduan Proyektor dan Kamera Kandao")
    st.write("""
    Selamat datang di panduan interaktif ini. Website ini dirancang untuk membantu Anda menghubungkan laptop ke proyektor 
    dan menggunakan kamera Kandao Meeting Pro dengan mudah.
    """)
    st.markdown("Silakan pilih panduan dari menu sebelah kiri.")

# Halaman Panduan Proyektor (dari 1_Panduan_Proyektor.py)
elif menu == "Panduan Proyektor":
    st.title("📺 Panduan Menyambungkan Proyektor")

    st.markdown("#### A. Menggunakan Shortcut Keyboard")
    st.write("1. Pastikan proyektor menyala (tombol power di remote).")
    st.write("2. Tekan tombol `Windows + K` pada laptop Anda.")
    st.image("assets/windows_k_shortcut.png", caption="Shortcut Windows + K")
    st.write("3. Pilih nama ruang meeting yang muncul.")

    st.markdown("---")

    st.markdown("#### B. Menggunakan Kabel HDMI/VGA")
    st.write("1. Sambungkan kabel dari proyektor ke laptop.")
    st.image("assets/colokan_hdmi.png", caption="Contoh port HDMI")
    st.write("2. Pilih input HDMI/VGA di layar proyektor.")
    st.image("assets/home_screen_hdmi.png", caption="Shortcut port HDMI")
    st.write("3. Jika berhasil, tampilan laptop akan muncul di layar.")
    st.image("assets/Picture11.png", caption="Shortcut HDMI")

    st.markdown("> 🔌 **Pastikan untuk mematikan proyektor setelah digunakan.**")
    st.image("assets/Picture12.png", caption="Shortcut Remote OFF")

# Halaman Panduan Kamera (dari 2_Panduan_Kamera.py)
elif menu == "Panduan Kamera":
    st.title("📷 Panduan Penggunaan Kamera Kandao")

    st.subheader("🔹 A. Koneksi ke Laptop")
    st.markdown("""
    1. Aktifkan kamera Kandao dengan menekan tombol **ON/OFF**.
    2. Hubungkan kamera ke laptop menggunakan kabel **USB OUT**.
    3. Buka aplikasi **Zoom** atau **Microsoft Teams**.
    4. Pada pengaturan kamera dan mikrofon, pilih **Kandao Meeting Pro**.
    5. Pastikan **lampu biru** menyala untuk menandakan koneksi berhasil.
    """)
    st.image("assets/kandao_power_button.png", caption="Kandao On Meeting")

    st.subheader("🔹 B. Koneksi ke Proyektor")
    st.markdown("""
    1. Hubungkan kamera ke layar/penampil melalui kabel **HDMI**.
    2. Aktifkan kamera jika belum menyala.
    3. Hubungkan ke jaringan Wi-Fi **TU MOBILE**.
    4. Periksa lampu biru menyala sebagai indikator sukses koneksi.
    """)
    st.image("assets/Picture13.png", caption="Kandao Connect Proyektor")

# Halaman Remote & Fitur (dari 3_Remote_&_Fitur.py)
elif menu == "Remote & Fitur":
    st.title("🎛️ Remote Control & Fitur Kamera Kandao")

    st.subheader("🔹 Fungsi Remote")
    st.markdown("""
    - **Tombol Daya:** Menghidupkan / Mematikan kamera
    - **Mode Mouse:** Menggerakkan kursor pada layar
    - **Volume:** Menyesuaikan volume suara
    - **Mikrofon:** Mute/unmute suara
    """)
    st.image("assets/kandao_remote_buttons.png", caption="Fungsi Remote")

    st.subheader("🔹 Fitur Unggulan Kamera Kandao Meeting Pro")
    st.markdown("""
    - **Audio Jernih:** Mikrofon internal menangkap suara dengan jelas.
    - **Video Berkualitas Tinggi:** Gambar tajam dan detail untuk semua peserta rapat.
    - **Kemudahan Penggunaan:** Instalasi cepat tanpa konfigurasi rumit.
    """)
    st.image("assets/kandao_features_summary.png.png", caption="Fitur Unggulan Kamera Kandao Meeting Pro")

# Halaman FAQ & Troubleshooting (dari 4_FAQ_Troubleshooting.py)
elif menu == "FAQ & Troubleshooting":
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

