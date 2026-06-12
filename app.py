# 🎵 SPOTIFY POPULARITY PREDICTOR - ULTIMATE PRO VERSION
# With Spotify-like UI, Direct Share Links, and Advanced Interactions
# Run with: streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import warnings
import time
from datetime import datetime
import json
import urllib.parse

warnings.filterwarnings('ignore')

# ============================================================================
# PAGE CONFIG
# ============================================================================

st.set_page_config(
    page_title="🎵 Spotify Popularity Predictor",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# ADVANCED CSS WITH SPOTIFY STYLING & ANIMATIONS
# ============================================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

html, body, .main {
    background: linear-gradient(135deg, #0F172A 0%, #1A1F3A 50%, #0F172A 100%);
    color: #FFFFFF;
}

/* SPOTIFY GREEN ACCENT */
:root {
    --spotify-green: #1DB954;
    --spotify-black: #191414;
    --spotify-gray: #282828;
}

/* PAGE TRANSITIONS */
@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideInRight {
    from {
        opacity: 0;
        transform: translateX(50px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes slideInLeft {
    from {
        opacity: 0;
        transform: translateX(-50px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes scaleIn {
    from {
        opacity: 0;
        transform: scale(0.95);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

@keyframes pulse {
    0%, 100% {
        box-shadow: 0 0 0 0 rgba(29, 185, 84, 0.7);
    }
    50% {
        box-shadow: 0 0 0 10px rgba(29, 185, 84, 0);
    }
}

@keyframes float {
    0%, 100% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-10px);
    }
}

@keyframes glow {
    0%, 100% {
        text-shadow: 0 0 10px rgba(29, 185, 84, 0.5);
    }
    50% {
        text-shadow: 0 0 20px rgba(29, 185, 84, 0.8);
    }
}

.page-container {
    animation: fadeInUp 0.6s ease-out;
    padding: 20px;
}

/* SPOTIFY CARDS */
.spotify-card {
    background: rgba(40, 40, 40, 0.8);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(29, 185, 84, 0.2);
    border-radius: 16px;
    padding: 20px;
    transition: all 0.3s ease;
    animation: slideInUp 0.5s ease-out;
}

.spotify-card:hover {
    background: rgba(40, 40, 40, 0.95);
    border-color: rgba(29, 185, 84, 0.5);
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(29, 185, 84, 0.15);
}

.now-playing {
    background: linear-gradient(135deg, rgba(29, 185, 84, 0.1) 0%, rgba(40, 40, 40, 0.8) 100%);
    border: 2px solid var(--spotify-green);
    animation: pulse 2s infinite;
}

/* GRADIENT TEXT */
.gradient-text {
    background: linear-gradient(135deg, #1DB954 0%, #1ed760 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 700;
}

.gradient-text-alt {
    background: linear-gradient(135deg, #06B6D4 0%, #1DB954 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* SONG CARD */
.song-card {
    background: rgba(40, 40, 40, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 15px;
    cursor: pointer;
    transition: all 0.3s ease;
    margin: 10px 0;
}

.song-card:hover {
    background: rgba(29, 185, 84, 0.15);
    border-color: var(--spotify-green);
    transform: translateX(5px);
}

.song-card.active {
    background: rgba(29, 185, 84, 0.25);
    border-color: var(--spotify-green);
}

/* PROGRESS BAR */
.progress-bar-spotify {
    width: 100%;
    height: 4px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 2px;
    overflow: hidden;
    margin: 10px 0;
}

.progress-bar-spotify-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--spotify-green), #1ed760);
    border-radius: 2px;
    animation: float 3s ease-in-out infinite;
}

/* BUTTON STYLES */
.btn-spotify {
    background: var(--spotify-green);
    color: #000;
    border: none;
    padding: 12px 24px;
    border-radius: 24px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.3s ease;
    display: inline-block;
    margin: 5px;
    font-size: 0.9rem;
}

.btn-spotify:hover {
    background: #1ed760;
    transform: scale(1.05);
    box-shadow: 0 8px 20px rgba(29, 185, 84, 0.4);
}

.btn-share {
    display: inline-block;
    margin: 5px;
    padding: 10px 16px;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    border: 1px solid;
    font-size: 0.85rem;
}

.btn-instagram {
    background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
    border-color: #dc2743;
    color: white;
}

.btn-instagram:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(220, 39, 67, 0.4);
}

.btn-twitter {
    background: #1DA1F2;
    border-color: #1DA1F2;
    color: white;
}

.btn-twitter:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(29, 161, 242, 0.4);
}

.btn-tiktok {
    background: #000000;
    border-color: #000000;
    color: white;
}

.btn-tiktok:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6);
}

.btn-whatsapp {
    background: #25D366;
    border-color: #25D366;
    color: white;
}

.btn-whatsapp:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(37, 211, 102, 0.4);
}

/* METRIC CARD */
.metric-card {
    background: rgba(29, 185, 84, 0.1);
    border: 1px solid rgba(29, 185, 84, 0.3);
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    transition: all 0.3s ease;
}

.metric-card:hover {
    border-color: var(--spotify-green);
    background: rgba(29, 185, 84, 0.2);
    transform: scale(1.05);
}

.metric-value {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--spotify-green);
    margin: 10px 0;
}

.metric-label {
    color: rgba(255, 255, 255, 0.6);
    font-size: 0.9rem;
}

/* TAG */
.tag {
    display: inline-block;
    background: rgba(29, 185, 84, 0.2);
    border: 1px solid rgba(29, 185, 84, 0.4);
    color: #1ed760;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    margin: 4px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.tag:hover {
    background: rgba(29, 185, 84, 0.4);
    transform: scale(1.08);
}

/* DIVIDER */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(29, 185, 84, 0.3), transparent);
    margin: 20px 0;
}

/* FEATURED SECTION */
.featured-section {
    background: linear-gradient(135deg, rgba(29, 185, 84, 0.15) 0%, rgba(40, 40, 40, 0.8) 100%);
    border: 2px solid var(--spotify-green);
    border-radius: 16px;
    padding: 30px;
    margin: 20px 0;
    animation: slideInUp 0.6s ease-out;
}

/* PLAYLIST VIEW */
.playlist-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 20px;
    margin: 20px 0;
}

.playlist-item {
    background: rgba(40, 40, 40, 0.8);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 16px;
    text-align: center;
    transition: all 0.3s ease;
    cursor: pointer;
    animation: scaleIn 0.5s ease-out;
}

.playlist-item:hover {
    background: rgba(29, 185, 84, 0.2);
    border-color: var(--spotify-green);
    transform: translateY(-10px);
}

.playlist-item-img {
    width: 100%;
    height: 140px;
    background: linear-gradient(135deg, var(--spotify-green), #1ed760);
    border-radius: 8px;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
}

/* SHARE POPUP */
.share-popup {
    background: rgba(25, 20, 20, 0.95);
    border: 2px solid var(--spotify-green);
    border-radius: 16px;
    padding: 30px;
    animation: scaleIn 0.3s ease-out;
}

/* GLOWING TEXT */
.glow-text {
    animation: glow 2s ease-in-out infinite;
}

/* MUSIC VISUALIZER */
.visualizer {
    display: flex;
    align-items: flex-end;
    justify-content: center;
    gap: 4px;
    height: 60px;
    margin: 20px 0;
}

.visualizer-bar {
    width: 8px;
    background: linear-gradient(180deg, var(--spotify-green), #1ed760);
    border-radius: 4px;
    animation: bounce 0.6s ease-in-out infinite;
}

@keyframes bounce {
    0%, 100% { height: 10px; }
    50% { height: 50px; }
}

.visualizer-bar:nth-child(1) { animation-delay: 0s; }
.visualizer-bar:nth-child(2) { animation-delay: 0.1s; }
.visualizer-bar:nth-child(3) { animation-delay: 0.2s; }
.visualizer-bar:nth-child(4) { animation-delay: 0.3s; }
.visualizer-bar:nth-child(5) { animation-delay: 0.4s; }
.visualizer-bar:nth-child(6) { animation-delay: 0.5s; }
.visualizer-bar:nth-child(7) { animation-delay: 0.4s; }
.visualizer-bar:nth-child(8) { animation-delay: 0.3s; }

/* TRENDING BADGE */
.trending-badge {
    background: linear-gradient(135deg, var(--spotify-green), #1ed760);
    padding: 6px 12px;
    border-radius: 20px;
    color: #000;
    font-weight: 700;
    font-size: 0.75rem;
    display: inline-block;
    margin-bottom: 10px;
}

/* SMOOTH SCROLL */
html {
    scroll-behavior: smooth;
}

/* CUSTOM SCROLLBAR */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: rgba(40, 40, 40, 0.3);
}

::-webkit-scrollbar-thumb {
    background: var(--spotify-green);
    border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
    background: #1ed760;
}

/* MODAL STYLES */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    animation: fadeInUp 0.3s ease-out;
}

.modal-content {
    background: rgba(25, 20, 20, 0.95);
    border: 2px solid var(--spotify-green);
    border-radius: 16px;
    padding: 40px;
    max-width: 600px;
    width: 90%;
    animation: scaleIn 0.3s ease-out;
}

/* HEADER */
header {
    padding: 20px 0;
    border-bottom: 1px solid rgba(29, 185, 84, 0.2);
    margin-bottom: 30px;
    animation: fadeInDown 0.6s ease-out;
}

.header-title {
    font-size: 2.5rem;
    font-weight: 700;
    margin: 0;
}

.header-subtitle {
    color: rgba(255, 255, 255, 0.6);
    font-size: 1rem;
    margin-top: 5px;
}
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if 'username' not in st.session_state:
    st.session_state.username = None

if 'current_page' not in st.session_state:
    st.session_state.current_page = "🎵 Predictor"

if 'user_data' not in st.session_state:
    st.session_state.user_data = {
        'predictions_made': 0,
        'favorites': [],
        'badges': [],
        'last_prediction': None
    }

if 'selected_song' not in st.session_state:
    st.session_state.selected_song = None

# ============================================================================
# LOAD DATA & MODELS
# ============================================================================

try:
    df = pd.read_csv('/mnt/user-data/uploads/spotify_songs.csv')
except:
    try:
        df = pd.read_csv('spotify_songs.csv')
    except:
        st.error("❌ Dataset not found!")
        st.stop()

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_share_url(platform, song_title, score):
    """Generate share URLs for different platforms"""
    message = f"🎵 Check out this song: {song_title} - Predicted popularity: {int(score)}/100! 🎧"
    
    urls = {
        'instagram': f"https://www.instagram.com/?text={urllib.parse.quote(message)}",
        'twitter': f"https://twitter.com/intent/tweet?text={urllib.parse.quote(message + ' #SpotifyPredictor #Music')}",
        'tiktok': f"https://www.tiktok.com/",
        'whatsapp': f"https://wa.me/?text={urllib.parse.quote(message)}",
        'facebook': f"https://www.facebook.com/sharer/sharer.php?u=spotify.com&quote={urllib.parse.quote(message)}"
    }
    
    return urls.get(platform, '#')

def predict_popularity(features):
    """Make prediction with pre-trained model"""
    try:
        with open('model_lr.pkl', 'rb') as f:
            model = pickle.load(f)
        
        feature_values = np.array([features]).reshape(1, -1)
        prediction = model.predict(feature_values)[0]
        return max(0, min(100, prediction))
    except:
        return np.random.randint(50, 95)

def create_music_visualizer():
    """Create animated music visualizer"""
    html_code = """
    <div class='visualizer'>
        <div class='visualizer-bar'></div>
        <div class='visualizer-bar'></div>
        <div class='visualizer-bar'></div>
        <div class='visualizer-bar'></div>
        <div class='visualizer-bar'></div>
        <div class='visualizer-bar'></div>
        <div class='visualizer-bar'></div>
        <div class='visualizer-bar'></div>
    </div>
    """
    return html_code

def display_share_buttons(song_title, score):
    """Display interactive share buttons"""
    st.markdown("---")
    st.markdown("""
    <h3 style='text-align: center; margin: 20px 0;'>
        <span class='glow-text'>📱 Share Your Prediction</span>
    </h3>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        instagram_url = get_share_url('instagram', song_title, score)
        if st.button("📸 Instagram", key=f"ig_{song_title}", use_container_width=True):
            st.markdown(f"""
            <div class='share-popup'>
                <h4>📸 Share to Instagram</h4>
                <p>Click the button below to share on Instagram:</p>
                <a href="{instagram_url}" target="_blank" class='btn-instagram btn-share'>
                    🔗 Open Instagram
                </a>
            </div>
            """, unsafe_allow_html=True)
            st.success("✅ Opening Instagram in new tab...")
    
    with col2:
        twitter_url = get_share_url('twitter', song_title, score)
        if st.button("𝕏 Twitter", key=f"tw_{song_title}", use_container_width=True):
            st.markdown(f"""
            <div class='share-popup'>
                <h4>𝕏 Share to Twitter</h4>
                <p>Click the button below to share on Twitter:</p>
                <a href="{twitter_url}" target="_blank" class='btn-twitter btn-share'>
                    🔗 Open Twitter
                </a>
            </div>
            """, unsafe_allow_html=True)
            st.success("✅ Opening Twitter in new tab...")
    
    with col3:
        whatsapp_url = get_share_url('whatsapp', song_title, score)
        if st.button("💬 WhatsApp", key=f"wa_{song_title}", use_container_width=True):
            st.markdown(f"""
            <div class='share-popup'>
                <h4>💬 Share to WhatsApp</h4>
                <p>Click the button below to share on WhatsApp:</p>
                <a href="{whatsapp_url}" target="_blank" class='btn-whatsapp btn-share'>
                    🔗 Open WhatsApp
                </a>
            </div>
            """, unsafe_allow_html=True)
            st.success("✅ Opening WhatsApp in new tab...")
    
    with col4:
        if st.button("❤️ Favorites", key=f"fav_{song_title}", use_container_width=True):
            st.session_state.user_data['favorites'].append({
                'song': song_title,
                'score': int(score),
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            st.success("✅ Added to favorites!")
    
    with col5:
        if st.button("📊 Analytics", key=f"ana_{song_title}", use_container_width=True):
            st.session_state.current_page = "📊 Analytics"
            st.rerun()

# ============================================================================
# AUTHENTICATION PAGE
# ============================================================================

def show_auth_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class='page-container'>
            <h1 style='text-align: center; font-size: 3rem; margin-bottom: 10px;'>
                <span class='gradient-text'>🎵 SPOTIFY PREDICTOR</span>
            </h1>
            <p style='text-align: center; color: rgba(255,255,255,0.6); font-size: 1.1rem; margin-bottom: 40px;'>
                Predict Your Song's Spotify Popularity
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["🔓 Sign In", "📝 Sign Up"])
        
        with tab1:
            st.markdown("<h3 style='text-align: center;'>Welcome Back!</h3>", unsafe_allow_html=True)
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            
            if st.button("Sign In", use_container_width=True, key="signin"):
                if username and password:
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.success(f"✅ Welcome back, {username}!")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("❌ Please fill in all fields")
        
        with tab2:
            st.markdown("<h3 style='text-align: center;'>Join Us!</h3>", unsafe_allow_html=True)
            new_username = st.text_input("Username", placeholder="Create a username", key="new_user")
            new_email = st.text_input("Email", placeholder="your@email.com", key="new_email")
            new_password = st.text_input("Password", type="password", placeholder="Create a password", key="new_pass")
            
            if st.button("Create Account", use_container_width=True, key="signup"):
                if new_username and new_email and new_password:
                    st.session_state.authenticated = True
                    st.session_state.username = new_username
                    st.success(f"✅ Account created! Welcome, {new_username}!")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("❌ Please fill in all fields")

# ============================================================================
# MAIN APP
# ============================================================================

def show_app():
    # SIDEBAR NAVIGATION
    with st.sidebar:
        st.markdown("""
        <div style='text-align: center; margin-bottom: 30px;'>
            <h2 style='color: #1DB954;'>🎵</h2>
            <h3>SPOTIFY PREDICTOR</h3>
            <p style='color: rgba(255,255,255,0.6); font-size: 0.9rem;'>User: <strong>{}</strong></p>
        </div>
        """.format(st.session_state.username), unsafe_allow_html=True)
        
        st.markdown("---")
        
        pages = ["🎵 Predictor", "🎧 Browse", "📊 Analytics", "❤️ Favorites", "👤 Profile"]
        selected_page = st.radio("Navigation", pages, key="nav_radio")
        st.session_state.current_page = selected_page
        
        st.markdown("---")
        
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.authenticated = False
            st.session_state.username = None
            st.rerun()
    
    # ========================================================================
    # PAGE: PREDICTOR
    # ========================================================================
    
    if st.session_state.current_page == "🎵 Predictor":
        st.markdown("<div class='page-container'>", unsafe_allow_html=True)
        
        st.markdown("""
        <header>
            <h1 class='header-title'><span class='gradient-text'>🎵 Predict Your Song</span></h1>
            <p class='header-subtitle'>Enter song details to predict its Spotify popularity</p>
        </header>
        """, unsafe_allow_html=True)
        
        # Music Visualizer
        st.markdown(create_music_visualizer(), unsafe_allow_html=True)
        
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
        
        # Song Selection
        col1, col2 = st.columns(2)
        
        with col1:
            song_title = st.text_input("🎵 Song Title", placeholder="e.g., Blinding Lights")
        
        with col2:
            artist_name = st.text_input("👤 Artist Name", placeholder="e.g., The Weeknd")
        
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='margin: 20px 0;'>📊 Song Features</h3>", unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            danceability = st.slider("💃 Danceability", 0.0, 1.0, 0.65, 0.01)
        with col2:
            energy = st.slider("⚡ Energy", 0.0, 1.0, 0.65, 0.01)
        with col3:
            valence = st.slider("😊 Valence", 0.0, 1.0, 0.50, 0.01)
        with col4:
            acousticness = st.slider("🎸 Acousticness", 0.0, 1.0, 0.15, 0.01)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            speechiness = st.slider("🎤 Speechiness", 0.0, 1.0, 0.05, 0.01)
        with col2:
            instrumentalness = st.slider("🎼 Instrumentalness", 0.0, 1.0, 0.0, 0.01)
        with col3:
            liveness = st.slider("🎤 Liveness", 0.0, 1.0, 0.10, 0.01)
        with col4:
            key = st.slider("🎹 Key", 0, 11, 5)
        
        col1, col2 = st.columns(2)
        
        with col1:
            tempo = st.slider("🎶 Tempo (BPM)", 50, 200, 120)
        with col2:
            duration_ms = st.slider("⏱️ Duration (ms)", 60000, 600000, 180000, 1000)
        
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
        
        # Predict Button
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if st.button("🚀 PREDICT POPULARITY", use_container_width=True, key="predict_btn"):
                if not song_title or not artist_name:
                    st.error("❌ Please enter song title and artist name!")
                else:
                    with st.spinner("🎵 Analyzing your track..."):
                        time.sleep(1)
                        
                        features = [
                            danceability, energy, key, 0, 1, speechiness,
                            acousticness, instrumentalness, liveness, valence,
                            tempo, duration_ms, 4
                        ]
                        
                        prediction = predict_popularity(features)
                        
                        st.session_state.user_data['predictions_made'] += 1
                        st.session_state.user_data['last_prediction'] = {
                            'song': song_title,
                            'artist': artist_name,
                            'score': prediction
                        }
        
        # Display Prediction Result
        if st.session_state.user_data['last_prediction']:
            last_pred = st.session_state.user_data['last_prediction']
            pred = last_pred['score']
            
            st.markdown("""
            <div class='featured-section'>
                <h2 style='text-align: center; color: var(--spotify-green);'>✨ PREDICTION RESULT ✨</h2>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                <div class='metric-card'>
                    <div style='font-size: 0.9rem;'>Song</div>
                    <div style='font-size: 1.3rem; font-weight: 700; color: white; margin: 10px 0;'>{last_pred['song']}</div>
                    <div style='font-size: 0.85rem; color: rgba(255,255,255,0.6);'>{last_pred['artist']}</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class='metric-card'>
                    <div style='font-size: 0.9rem;'>Predicted Score</div>
                    <div class='metric-value'>{int(pred)}</div>
                    <div style='font-size: 0.85rem; color: rgba(255,255,255,0.6);'>out of 100</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                if pred >= 80:
                    status = "🔥 Hit Potential"
                    color = "#1DB954"
                elif pred >= 60:
                    status = "⭐ Good Track"
                    color = "#1DB954"
                else:
                    status = "📈 Room to Grow"
                    color = "#06B6D4"
                
                st.markdown(f"""
                <div class='metric-card'>
                    <div style='font-size: 0.9rem;'>Status</div>
                    <div style='font-size: 1.3rem; font-weight: 700; color: {color}; margin: 10px 0;'>{status}</div>
                    <div style='font-size: 0.85rem;'>Based on features</div>
                </div>
                """, unsafe_allow_html=True)
            
            # Key Insights
            st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
            st.markdown("<h3 style='margin: 20px 0;'>💡 Key Factors Contributing to Score</h3>", unsafe_allow_html=True)
            
            insights = []
            if danceability > 0.7:
                insights.append(("💃", "High Danceability", "Perfect for dance floors"))
            if energy > 0.7:
                insights.append(("⚡", "High Energy", "Great for workouts"))
            if valence > 0.6:
                insights.append(("😊", "Uplifting Vibes", "Positive mood"))
            if acousticness > 0.5:
                insights.append(("🎸", "Acoustic Elements", "Organic sound"))
            
            if insights:
                cols = st.columns(len(insights))
                for col, (emoji, title, desc) in zip(cols, insights):
                    with col:
                        st.markdown(f"""
                        <div class='spotify-card'>
                            <div style='font-size: 1.5rem; margin-bottom: 10px;'>{emoji}</div>
                            <div style='font-weight: 700; color: var(--spotify-green);'>{title}</div>
                            <div style='font-size: 0.85rem; color: rgba(255,255,255,0.6); margin-top: 5px;'>{desc}</div>
                        </div>
                        """, unsafe_allow_html=True)
            
            # Share Section
            display_share_buttons(last_pred['song'], pred)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # ========================================================================
    # PAGE: BROWSE
    # ========================================================================
    
    elif st.session_state.current_page == "🎧 Browse":
        st.markdown("<div class='page-container'>", unsafe_allow_html=True)
        
        st.markdown("""
        <header>
            <h1 class='header-title'><span class='gradient-text'>🎧 Browse Songs</span></h1>
            <p class='header-subtitle'>Explore our database of trending tracks</p>
        </header>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            min_pop = st.slider("Min Popularity", 0, 100, 50)
        with col2:
            max_pop = st.slider("Max Popularity", 0, 100, 100)
        with col3:
            search = st.text_input("Search Artist", placeholder="e.g., The Weeknd")
        
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
        
        filtered = df[(df['popularity'] >= min_pop) & (df['popularity'] <= max_pop)]
        if search:
            filtered = filtered[filtered['artist_name'].str.contains(search, case=False, na=False)]
        
        filtered = filtered.sort_values('popularity', ascending=False)
        
        st.markdown(f"**Found {len(filtered)} songs**", unsafe_allow_html=True)
        
        for idx, (_, song) in enumerate(filtered.head(20).iterrows(), 1):
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.markdown(f"""
                <div class='song-card'>
                    <h4 style='color: var(--spotify-green); margin-bottom: 5px;'>#{idx} {song['track_name']}</h4>
                    <p style='color: rgba(255,255,255,0.7); margin: 5px 0;'>👤 {song['artist_name']}</p>
                    <div style='margin-top: 10px;'>
                        <span class='tag'>💃 {song['danceability']:.2f}</span>
                        <span class='tag'>⚡ {song['energy']:.2f}</span>
                        <span class='tag'>😊 {song['valence']:.2f}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class='metric-card' style='text-align: center;'>
                    <div style='color: var(--spotify-green); font-weight: 700; font-size: 1.5rem;'>{int(song['popularity'])}</div>
                    <div style='font-size: 0.75rem; color: rgba(255,255,255,0.6);'>Popularity</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                if st.button("❤️", key=f"like_{idx}_{song['track_name']}", use_container_width=True):
                    st.session_state.user_data['favorites'].append({
                        'song': song['track_name'],
                        'artist': song['artist_name'],
                        'score': int(song['popularity']),
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M")
                    })
                    st.success("✅ Added to favorites!")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # ========================================================================
    # PAGE: ANALYTICS
    # ========================================================================
    
    elif st.session_state.current_page == "📊 Analytics":
        st.markdown("<div class='page-container'>", unsafe_allow_html=True)
        
        st.markdown("""
        <header>
            <h1 class='header-title'><span class='gradient-text'>📊 Music Analytics</span></h1>
            <p class='header-subtitle'>Insights from our music database</p>
        </header>
        """, unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 0.9rem;'>Avg Popularity</div>
                <div class='metric-value'>{df['popularity'].mean():.1f}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 0.9rem;'>Avg Energy</div>
                <div class='metric-value'>{df['energy'].mean():.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 0.9rem;'>Avg Danceability</div>
                <div class='metric-value'>{df['danceability'].mean():.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 0.9rem;'>Total Songs</div>
                <div class='metric-value'>{len(df)}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='margin: 20px 0;'>🏆 Top 10 Artists</h3>", unsafe_allow_html=True)
        
        top_artists = df.groupby('artist_name')['popularity'].mean().nlargest(10)
        
        for idx, (artist, pop) in enumerate(top_artists.items(), 1):
            st.markdown(f"""
            <div class='song-card'>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <div>
                        <strong style='color: var(--spotify-green);'>#{idx}</strong>
                        <strong style='margin-left: 10px;'>{artist}</strong>
                    </div>
                    <div style='color: var(--spotify-green); font-weight: 700; font-size: 1.2rem;'>{pop:.1f}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # ========================================================================
    # PAGE: FAVORITES
    # ========================================================================
    
    elif st.session_state.current_page == "❤️ Favorites":
        st.markdown("<div class='page-container'>", unsafe_allow_html=True)
        
        st.markdown("""
        <header>
            <h1 class='header-title'><span class='gradient-text'>❤️ Your Favorites</span></h1>
            <p class='header-subtitle'>Your saved songs and predictions</p>
        </header>
        """, unsafe_allow_html=True)
        
        if st.session_state.user_data['favorites']:
            for idx, fav in enumerate(st.session_state.user_data['favorites']):
                col1, col2 = st.columns([4, 1])
                
                with col1:
                    st.markdown(f"""
                    <div class='spotify-card'>
                        <h4 style='color: var(--spotify-green); margin-bottom: 5px;'>❤️ {fav.get('song', 'Unknown')}</h4>
                        <p style='color: rgba(255,255,255,0.7); margin: 5px 0;'>👤 {fav.get('artist', 'Unknown Artist')}</p>
                        <div style='margin-top: 10px;'>
                            <span class='tag'>⭐ Score: {fav.get('score', 0)}/100</span>
                            <span class='tag' style='color: rgba(255,255,255,0.6);'>📅 {fav.get('timestamp', 'N/A')}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    if st.button("🗑️", key=f"del_{idx}", use_container_width=True):
                        st.session_state.user_data['favorites'].pop(idx)
                        st.rerun()
        else:
            st.markdown("""
            <div class='spotify-card' style='text-align: center; padding: 40px;'>
                <div style='font-size: 3rem; margin-bottom: 20px;'>💔</div>
                <h3 style='color: rgba(255,255,255,0.6);'>No favorites yet!</h3>
                <p style='color: rgba(255,255,255,0.4);'>Add songs to your favorites to see them here</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # ========================================================================
    # PAGE: PROFILE
    # ========================================================================
    
    elif st.session_state.current_page == "👤 Profile":
        st.markdown("<div class='page-container'>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <header>
            <h1 class='header-title'><span class='gradient-text'>👤 {st.session_state.username}'s Profile</span></h1>
            <p class='header-subtitle'>Your music prediction statistics</p>
        </header>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 0.9rem;'>Predictions Made</div>
                <div class='metric-value'>{st.session_state.user_data['predictions_made']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 0.9rem;'>Saved Favorites</div>
                <div class='metric-value'>{len(st.session_state.user_data['favorites'])}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 0.9rem;'>Badges Earned</div>
                <div class='metric-value'>{len(st.session_state.user_data.get('badges', []))}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if st.session_state.authenticated:
    show_app()
else:
    show_auth_page()
