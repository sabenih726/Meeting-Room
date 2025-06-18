# app.py
import streamlit as st

st.set_page_config(
    page_title="Panduan Proyektor & Kamera Kandao",
    layout="wide",
    page_icon="📽️"
)

st.title("📽️ Panduan Penggunaan Proyektor & Kamera Kandao")

st.write("""
Selamat datang! Website ini dirancang untuk membantu Anda menghubungkan perangkat ke proyektor dan menggunakan kamera Kandao Meeting Pro secara efektif.

Gunakan menu di sebelah kiri untuk memilih panduan yang ingin Anda lihat.
""")

# Struktur folder yang diasumsikan:
# pages/
# ├── 1_Panduan_Proyektor.py
# ├── 2_Panduan_Kamera.py
# ├── 3_Remote_&_Fitur.py
# └── 4_FAQ_Troubleshooting.py
