# 🎬 Movie Recommendation System

**My 1st EVER PROJECT**

Welcome to my **Streamlit-powered Movie Recommender App**!  
It suggests similar movies based on the one you select — complete with poster previews and beautiful hover animations.

🔗 **Try the Live App**: [Click here to open](https://your-app-url.streamlit.app)

> Replace the above URL with your real Streamlit app link!

---

## 📦 Features

✅ Recommends 15 similar movies using cosine similarity  
✅ Stylish UI with glowing borders, hover effects, and starfield animation  
✅ Uses TMDb API to fetch real movie posters  
✅ Built using Python, Streamlit, and `scikit-learn`  

---

## 🎥 Sample Movies You Can Try

- Inception  
- Interstellar  
- The Dark Knight  
- The Matrix  
- Fight Club  
- Forrest Gump  
- Titanic  
- Avengers: Endgame  
- Joker  
- The Godfather  

(Just start typing any title in the dropdown and the app will autocomplete it!)

---

## 🛠 How It Works

1. Select a movie from the dropdown.
2. The app finds the top 15 most similar movies using a precomputed similarity matrix.
3. It fetches posters from **TMDb** using their API.
4. Posters are shown with a rainbow glow hover animation.

---

## 🧠 Tech Stack

- Python
- Streamlit
- pandas, scikit-learn
- TMDb API
- Custom HTML/CSS/JS (for starfield & particle effects)
- Google Drive + gdown (for large model file loading)

---

## 🚀 Deployment

The app is deployed on [Streamlit Cloud](https://streamlit.io/cloud), and the similarity matrix (`sim.pkl`) is loaded at runtime from Google Drive using `gdown`.

---

## 🙋‍♂️ About Me

I'm **Somesh Biswas**, a 2nd-year BSDS student at ISI Kolkata, building projects to learn real-world applications of data science.

📫 Contact me: [someshbiswas71@gmail.com]

---

⭐ If you like the project, feel free to **star the repo** or share the app!


