# 🎵 QUICK START GUIDE

## ⚡ Bắt đầu nhanh trong 3 bước

### 1️⃣ CHUẨN BỊ FILES
```
Đặt những files này cùng thư mục:
├── app_upgraded.py
├── spotify_songs_expanded.csv
├── model_lr.pkl
├── scaler.pkl
└── requirements_upgraded.txt
```

### 2️⃣ CÀI ĐẶT
```bash
# Install dependencies
pip install -r requirements_upgraded.txt
```

### 3️⃣ CHẠY
```bash
# Run the app
streamlit run app_upgraded.py
```

✅ App mở tại: http://localhost:8501

---

## 🎮 CÁCH DÙNG

### Predict Popularity
1. **Login** → Tạo tài khoản hoặc login
2. **Go to "🎵 Predictor"**
3. **Enter song details:**
   - Song title
   - Artist name
4. **Adjust sliders:**
   - Danceability, Energy, Valence, etc.
5. **Click "🚀 PREDICT POPULARITY"**
6. **Get result!** 📊

### Share Results
Sau khi có kết quả:
- **📸 Instagram** → Share trực tiếp
- **𝕏 Twitter** → Tweet kết quả
- **💬 WhatsApp** → Gửi bạn bè
- **❤️ Favorites** → Lưu bài hát
- **📊 Analytics** → Xem chi tiết

### Browse Songs
1. Go to **"🎧 Browse"**
2. Filter by popularity
3. Search artists
4. Like songs (❤️)

### View Stats
- **📊 Analytics** → Top artists, trends
- **❤️ Favorites** → Your saved songs
- **👤 Profile** → Your statistics

---

## 🎨 FEATURES

✨ **Spotify UI Design**
- Dark theme with green accents
- Smooth animations
- Interactive cards

🎵 **Music Visualizer**
- Animated bouncing bars
- Real-time effects

📱 **Direct Share Links**
- Instagram, Twitter, WhatsApp
- Pre-filled messages
- One-click sharing

🔍 **Advanced Browse**
- Filter & search
- View song features
- Like system

📊 **Analytics**
- Top artists ranking
- Popularity metrics
- Trend analysis

---

## ⚙️ SONG FEATURES EXPLAINED

| Slider | Range | Meaning |
|--------|-------|---------|
| 💃 Danceability | 0-1 | Suitable for dancing |
| ⚡ Energy | 0-1 | Intensity level |
| 😊 Valence | 0-1 | Positivity/happiness |
| 🎸 Acousticness | 0-1 | Acoustic vs electronic |
| 🎤 Speechiness | 0-1 | Spoken words |
| 🎼 Instrumentalness | 0-1 | Lack of vocals |
| 🎤 Liveness | 0-1 | Live performance feel |
| 🎹 Key | 0-11 | Musical key |
| 🎶 Tempo | 50-200 | Speed in BPM |
| ⏱️ Duration | 60-600s | Length in seconds |

---

## 🐛 TROUBLESHOOTING

**App won't start?**
```bash
pip install --upgrade streamlit
streamlit run app_upgraded.py
```

**Import errors?**
```bash
pip install pandas numpy scikit-learn
```

**Dataset not found?**
- Check file name: `spotify_songs_expanded.csv`
- Check file location: Same folder as app

**Model errors?**
- Make sure `model_lr.pkl` exists
- Run 02_Model_Training.py first

---

## 🎯 MAIN SECTIONS

### 🎵 Predictor (Main Feature)
- Input song features
- Get popularity prediction
- See key insights
- Share to social media

### 🎧 Browse
- Browse 500+ songs
- Filter by popularity
- Search artists
- Like songs

### 📊 Analytics
- View top artists
- See average metrics
- Analyze trends
- Database statistics

### ❤️ Favorites
- View saved songs
- See timestamps
- Delete favorites
- Quick access

### 👤 Profile
- View statistics
- Predictions made
- Favorites count
- Badges earned

---

## 💡 PRO TIPS

1. **High Danceability** → Popular in clubs (0.7+)
2. **High Energy** → Good for workouts (0.7+)
3. **High Valence** → Uplifting songs (0.6+)
4. **Low Acousticness** → Electronic music (0-0.2)
5. **High Tempo** → Fast-paced tracks (140+ BPM)

---

## 🔗 SHARE EXAMPLES

**What gets shared:**

Instagram:
```
🎵 Check out this song: [Song Title] - Predicted 
popularity: [Score]/100! 🎧
```

Twitter:
```
🎵 Check out this song: [Song Title] - Predicted 
popularity: [Score]/100! 🎧 #SpotifyPredictor #Music
```

WhatsApp:
```
🎵 Check out this song: [Song Title] - Predicted 
popularity: [Score]/100! 🎧
```

---

## 📈 TYPICAL SCORE RANGES

| Score | Status | Meaning |
|-------|--------|---------|
| 80-100 | 🔥 Hit | Very likely to be popular |
| 60-80 | ⭐ Good | Solid track |
| 40-60 | 📈 Fair | Has potential |
| 0-40 | 📉 Low | Needs improvement |

---

## ✅ CHECKLIST

- [ ] Python 3.7+ installed
- [ ] requirements_upgraded.txt installed
- [ ] All files in same folder
- [ ] model_lr.pkl present
- [ ] spotify_songs_expanded.csv present
- [ ] No errors when running streamlit

---

## 🎉 YOU'RE READY!

```bash
streamlit run app_upgraded.py
```

Enjoy predicting! 🎵

---

**Need help?**
- Check README_UPGRADED.md for detailed docs
- Check FEATURES_SUMMARY.md for all features
- View console for error messages

**Have fun!** 🎧❤️
