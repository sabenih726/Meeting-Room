import streamlit as st

st.set_page_config(page_title="Panduan Proyektor & Kamera Kandao", layout="wide")

# Simpan halaman yang dipilih di session_state supaya state-nya tetap walau refresh
if "page" not in st.session_state:
    st.session_state.page = "Beranda"

def set_page(page_name):
    st.session_state.page = page_name

# Halaman utama: tombol menu di tengah halaman
if st.session_state.page == "Beranda":
    st.title("📽️ Panduan Proyektor dan Kamera Kandao")
    st.write("Selamat datang di panduan interaktif ini. Website ini dirancang untuk membantu Anda menghubungkan laptop ke proyektor dan menggunakan kamera Kandao Meeting Pro dengan mudah.")
    st.markdown("Pilih panduan di bawah ini:")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("Beranda"):
            set_page("Beranda")
    with col2:
        if st.button("Panduan Proyektor"):
            set_page("Panduan Proyektor")
    with col3:
        if st.button("Panduan Kamera"):
            set_page("Panduan Kamera")
    with col4:
        if st.button("Remote & Fitur"):
            set_page("Remote & Fitur")
    with col5:
        if st.button("FAQ & Troubleshooting"):
            set_page("FAQ & Troubleshooting")

# Halaman Panduan Proyektor
elif st.session_state.page == "Panduan Proyektor":
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

    if st.button("Kembali ke Menu"):
        set_page("Beranda")

# Halaman Panduan Kamera
elif st.session_state.page == "Panduan Kamera":
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

    if st.button("Kembali ke Menu"):
        set_page("Beranda")

# Halaman Remote & Fitur
elif st.session_state.page == "Remote & Fitur":
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

    if st.button("Kembali ke Menu"):
        set_page("Beranda")

# Halaman FAQ & Troubleshooting
elif st.session_state.page == "FAQ & Troubleshooting":
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

    if st.button("Kembali ke Menu"):
        set_page("Beranda")
