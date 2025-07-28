import streamlit as st
from PIL import Image
import time

st.set_page_config(
    page_title="Meeting Room Self-Service Kiosk", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load Gambar
@st.cache_data
def load_image(path):
    try:
        return Image.open(path)
    except:
        return None

# Custom CSS untuk tampilan kiosk
st.markdown("""
    <style>
        /* Hide Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display:none;}
        
        /* Background and main container */
        .stApp {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        /* Welcome header */
        .welcome-header {
            background: rgba(255, 255, 255, 0.95);
            padding: 2rem;
            border-radius: 20px;
            margin: 2rem 0;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        
        .welcome-title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 0.5rem;
            text-align: center;
        }
        
        .welcome-subtitle {
            font-size: 1.2rem;
            color: #7f8c8d;
            text-align: center;
            line-height: 1.6;
        }
        
        /* Kiosk button styling */
        .kiosk-button {
            background: linear-gradient(145deg, #6c5ce7, #a29bfe);
            border: none;
            border-radius: 25px;
            padding: 2rem 1.5rem;
            margin: 1rem;
            color: white;
            font-size: 1.1rem;
            font-weight: 600;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 8px 25px rgba(108, 92, 231, 0.3);
            min-height: 120px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-decoration: none;
        }
        
        .kiosk-button:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 35px rgba(108, 92, 231, 0.4);
            background: linear-gradient(145deg, #5f4fcf, #9b94ff);
        }
        
        .kiosk-button-icon {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        
        .kiosk-button-text {
            font-size: 1.1rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .kiosk-button-desc {
            font-size: 0.9rem;
            opacity: 0.9;
            margin-top: 0.3rem;
        }
        
        /* Content area */
        .content-area {
            background: rgba(255, 255, 255, 0.95);
            padding: 2rem;
            border-radius: 20px;
            margin: 2rem 0;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        
        /* Navigation buttons */
        .nav-button {
            background: #74b9ff;
            color: white;
            border: none;
            padding: 0.8rem 2rem;
            border-radius: 15px;
            font-weight: 600;
            margin: 0.5rem;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .nav-button:hover {
            background: #0984e3;
            transform: translateY(-2px);
        }
        
        .nav-button.active {
            background: #00b894;
        }
        
        /* Time display */
        .time-display {
            position: fixed;
            bottom: 20px;
            left: 20px;
            background: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 10px 20px;
            border-radius: 10px;
            font-weight: bold;
        }
        
        /* Steps styling */
        .step-item {
            background: #f8f9fa;
            padding: 1.5rem;
            margin: 1rem 0;
            border-radius: 15px;
            border-left: 5px solid #6c5ce7;
        }
        
        .step-number {
            background: #6c5ce7;
            color: white;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            margin-right: 1rem;
        }
        
        /* Warning and info boxes */
        .warning-box {
            background: linear-gradient(145deg, #ffeaa7, #fdcb6e);
            padding: 1.5rem;
            border-radius: 15px;
            margin: 1rem 0;
            border-left: 5px solid #e17055;
        }
        
        .info-box {
            background: linear-gradient(145deg, #74b9ff, #0984e3);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            margin: 1rem 0;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# Time display
current_time = time.strftime("%H:%M")
current_date = time.strftime("%A, %d %B %Y")
st.markdown(f"""
    <div class="time-display">
        {current_time}<br>
        <small>{current_date}</small>
    </div>
""", unsafe_allow_html=True)

# Main navigation function
def show_home():
    # Welcome header
    st.markdown("""
        <div class="welcome-header">
            <div class="welcome-title">Welcome</div>
            <div class="welcome-subtitle">Self Registration Kiosk<br>
            Meeting Room Equipment Guidelines</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Main menu buttons in grid layout
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📺", key="projector_btn", help="Panduan Proyektor"):
            st.session_state.current_page = 'projector'
            st.rerun()
        st.markdown("""
            <div class="kiosk-button" onclick="">
                <div class="kiosk-button-icon">📺</div>
                <div class="kiosk-button-text">PROYEKTOR</div>
                <div class="kiosk-button-desc">Panduan menghubungkan proyektor</div>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎛️", key="remote_btn", help="Remote & Fitur"):
            st.session_state.current_page = 'remote'
            st.rerun()
        st.markdown("""
            <div class="kiosk-button">
                <div class="kiosk-button-icon">🎛️</div>
                <div class="kiosk-button-text">REMOTE & FITUR</div>
                <div class="kiosk-button-desc">Penggunaan remote control</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if st.button("📷", key="camera_btn", help="Panduan Kamera"):
            st.session_state.current_page = 'camera'
            st.rerun()
        st.markdown("""
            <div class="kiosk-button">
                <div class="kiosk-button-icon">📷</div>
                <div class="kiosk-button-text">KAMERA</div>
                <div class="kiosk-button-desc">Setup kamera meeting</div>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("❓", key="faq_btn", help="FAQ & Troubleshooting"):
            st.session_state.current_page = 'faq'
            st.rerun()
        st.markdown("""
            <div class="kiosk-button">
                <div class="kiosk-button-icon">❓</div>
                <div class="kiosk-button-text">FAQ & HELP</div>
                <div class="kiosk-button-desc">Bantuan dan troubleshooting</div>
            </div>
        """, unsafe_allow_html=True)

def show_projector_guide():
    st.markdown('<div class="content-area">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 8])
    with col1:
        if st.button("🏠 Home", key="home_from_proj"):
            st.session_state.current_page = 'home'
            st.rerun()
    with col2:
        st.markdown("<h1 style='color: #2c3e50;'>📺 Panduan Menyambungkan Proyektor</h1>", unsafe_allow_html=True)

    st.markdown("""
        <div class="step-item">
            <span class="step-number">A</span>
            <strong>Menggunakan Shortcut Keyboard</strong>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("1. Pastikan proyektor menyala (tombol power di remote).")
    st.write("2. Tekan tombol `Windows + K` pada laptop Anda.")
    
    # Try to load and display image
    img = load_image("assets/windows_k_shortcut.png")
    if img:
        st.image(img, caption="Shortcut Windows + K")
    else:
        st.info("📷 Gambar shortcut Windows + K")
    
    st.write("3. Pilih nama ruang meeting yang muncul.")

    st.markdown("---")

    st.markdown("""
        <div class="step-item">
            <span class="step-number">B</span>
            <strong>Menggunakan Kabel HDMI/VGA</strong>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("1. Sambungkan kabel dari proyektor ke laptop.")
    st.write("2. Pilih input HDMI/VGA di layar proyektor.")
    st.write("3. Jika berhasil, tampilan laptop akan muncul di layar.")

    st.markdown("""
        <div class="warning-box">
            <strong>🔌 Jangan lupa matikan proyektor setelah digunakan.</strong>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_camera_guide():
    st.markdown('<div class="content-area">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 8])
    with col1:
        if st.button("🏠 Home", key="home_from_cam"):
            st.session_state.current_page = 'home'
            st.rerun()
    with col2:
        st.markdown("<h1 style='color: #2c3e50;'>📷 Panduan Penggunaan Kamera Kandao</h1>", unsafe_allow_html=True)

    st.markdown("""
        <div class="step-item">
            <span class="step-number">A</span>
            <strong>🔹 Koneksi ke Laptop</strong>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    1. Aktifkan kamera Kandao dengan menekan tombol **ON/OFF**.  
    2. Hubungkan kamera ke laptop menggunakan kabel **USB OUT**.  
    3. Buka aplikasi **Zoom** atau **Microsoft Teams**.  
    4. Pilih **Kandao Meeting Pro** di pengaturan kamera.  
    5. Pastikan **lampu biru** menyala.
    """)
    
    # Try to load and display images for laptop connection
    img1 = load_image("assets/kandao_power_button.png")
    if img1:
        st.image(img1, caption="Tombol Power Kamera")
    else:
        st.info("📷 Gambar: Tombol Power Kamera")
        
    img2 = load_image("assets/Picture15.png")
    if img2:
        st.image(img2, caption="Koneksi Kamera ke laptop")
    else:
        st.info("📷 Gambar: Koneksi Kamera ke laptop")

    st.markdown("""
        <div class="step-item">
            <span class="step-number">B</span>
            <strong>🔹 Koneksi ke Proyektor</strong>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    1. Hubungkan kamera ke layar/monitor melalui kabel **HDMI**.  
    2. Nyalakan kamera jika belum aktif.  
    3. Sambungkan ke jaringan Wi-Fi **TU MOBILE**.  
    4. Pastikan lampu biru menyala sebagai indikator.
    """)
    
    img3 = load_image("assets/Picture13.png")
    if img3:
        st.image(img3, caption="Koneksi Kamera ke Proyektor")
    else:
        st.info("📷 Gambar: Koneksi Kamera ke Proyektor")
    
    st.markdown("""
        <div class="step-item">
            <span class="step-number">C</span>
            <strong>🔸 Flowchart Topologi Penggunaan Kamera Kandao</strong>
        </div>
    """, unsafe_allow_html=True)
    
    img4 = load_image("assets/Picture14.png")
    if img4:
        st.image(img4, caption="Topologi Sistem Kamera Kandao")
    else:
        st.info("📷 Gambar: Topologi Sistem Kamera Kandao")
    
    st.markdown("""
    1. Hubungkan ADAPTER ke Device dan listrik menggunakan kabel USB C to C.  
    2. Nyalakan kamera pastikan lampu power menyala.  
    3. Hubungkan kabel HDMI dari proyektor ke kamera.  
    4. Kamera sudah terdisplay di screen projector.
    5. Buka aplikasi yang digunakan dan terima undangan meeting dengan remote control.
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_remote_guide():
    st.markdown('<div class="content-area">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 8])
    with col1:
        if st.button("🏠 Home", key="home_from_remote"):
            st.session_state.current_page = 'home'
            st.rerun()
    with col2:
        st.markdown("<h1 style='color: #2c3e50;'>🎛️ Remote Control & Fitur Kamera Kandao</h1>", unsafe_allow_html=True)

    st.markdown("""
        <div class="step-item">
            <span class="step-number">📱</span>
            <strong>Fungsi Remote</strong>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    - **Tombol Daya:** Nyalakan/matikan kamera  
    - **Mode Mouse:** Navigasi kursor pada layar  
    - **Volume:** Atur suara  
    - **Mikrofon:** Aktif/nonaktif suara
    """)

    st.markdown("""
        <div class="info-box">
            <h3>🔹 Fitur Unggulan Kamera Kandao Meeting Pro</h3>
            <ul>
                <li>🎙️ <strong>Audio Jernih</strong></li>
                <li>🎥 <strong>Video Berkualitas Tinggi</strong></li>
                <li>⚡ <strong>Kemudahan Instalasi</strong></li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_faq():
    st.markdown('<div class="content-area">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 8])
    with col1:
        if st.button("🏠 Home", key="home_from_faq"):
            st.session_state.current_page = 'home'
            st.rerun()
    with col2:
        st.markdown("<h1 style='color: #2c3e50;'>❓ FAQ & Troubleshooting</h1>", unsafe_allow_html=True)

    st.markdown("""
        <div class="step-item">
            <span class="step-number">?</span>
            <strong>Proyektor tidak terdeteksi?</strong>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    - Cek apakah proyektor sudah menyala.  
    - Ganti kabel HDMI/VGA jika perlu.  
    - Pastikan port laptop tidak bermasalah.
    """)

    st.markdown("""
        <div class="step-item">
            <span class="step-number">?</span>
            <strong>Kamera tidak muncul di Zoom/Teams?</strong>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    - Pastikan kabel USB tersambung dengan baik.  
    - Periksa pengaturan perangkat di aplikasi.  
    - Coba restart Zoom/Teams.
    """)

    st.markdown("""
        <div class="info-box">
            <h3>📞 Kontak Bantuan</h3>
            <p>Hubungi tim <strong>Facility</strong> atau <strong>IT Support</strong> untuk bantuan lebih lanjut melalui grup internal atau nomor resmi.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Main app logic
if st.session_state.current_page == 'home':
    show_home()
elif st.session_state.current_page == 'projector':
    show_projector_guide()
elif st.session_state.current_page == 'camera':
    show_camera_guide()
elif st.session_state.current_page == 'remote':
    show_remote_guide()
elif st.session_state.current_page == 'faq':
    show_faq()
