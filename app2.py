
import streamlit as st
import pickle
import pandas as pd
import requests
import pathlib

import gdown
import os

if not os.path.exists("sim.pkl"):
    url = "https://drive.google.com/file/d/1EBhrlQWMbhkR5bCIZDjRwKlGTliew7Lq/view?usp=sharing"  # <-- replace with your ID
    gdown.download(url, "sim.pkl", quiet=False)

with open("sim.pkl", "rb") as f:
    sim = pickle.load(f)




## Button style
# Load custom CSS
st.markdown('<style>link rel="stylesheet" href="style.css"></style>', unsafe_allow_html=True)
# Function to load CSS from the 'assets' folder
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load the external CSS
css_path = pathlib.Path("style.css")
load_css(css_path)


## Actual Model
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
#sim = pickle.load(open('sim.pkl', 'rb'))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def rec_movie(movie):
    rm = []
    rmp = []
    for i in sorted(list(enumerate(sim[movies[movies['title'] == movie].index[0]])), reverse = True,  key = lambda x:x[1] )[1:11]:
        movie_id = movies.iloc[i[0]].movie_id
        rm.append(movies.iloc[i[0]].title)
        rmp.append(fetch_poster(movie_id))
    return rm, rmp





st.title("🔮Movie recommenadtion system")
st.text("by SOMESH BISWAS", )
selected_movie = st.selectbox(
    "Enter movie name",
    movies['title'].values
)

if st.button('Show Recommendation', key='glow'):
    recommended_movie_names, recommended_movie_posters = rec_movie(selected_movie)
    # Add your CSS once
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet">

        <style>
        .poster-container {
            position: relative;
            width: 100%;
            margin: 10px auto;
            z-index: 0;
        }

        .poster-img {
            width: 100%;
            border-radius: 20px;
            transition: transform 0.3s ease, opacity 0.5s ease;
            position: relative;
            z-index: 1;
        }

        .poster-container:hover .poster-img {
            transform: scale(1.15);
            opacity: 0.75;
        }

        .poster-container::before {
            content: "";
            position: absolute;
            top: -9px;
            left: -9px;
            right: -9px;
            bottom: -9px;
            border-radius: 25px;
            background: linear-gradient(45deg,
                #ff0000, #ff7300, #fffb00,
                #48ff00, #00ffd5, #002bff,
                #7a00ff, #ff00c8, #ff0000);
            background-size: 400% 400%;
            animation: borderRun 3s linear infinite;
            z-index: 0;
            filter: blur(6px);
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .poster-container:hover::before {
            opacity: 1;
        }

        @keyframes borderRun {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .poster-title {
            font-family: 'Orbitron', sans-serif;
            text-align: center;
            color: white;
            margin-top: 5px;
            letter-spacing: 0.5px;
            z-index: 0;
        }

        .poster-group {
            display: flex;
            gap: 10px;
        }

        .poster-group:hover .poster-container {
            opacity: 0.3;
            transition: opacity 0.3s ease;
        }

        .poster-group .poster-container:hover {
            opacity: 1 !important;
        }


        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="poster-group">', unsafe_allow_html=True)

    # Display posters in columns
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown(f"""
                    <div class="poster-container">
                        <img src="{recommended_movie_posters[i]}" class="poster-img">
                    </div>
                    <div class="poster-title">{recommended_movie_names[i]}</div>
                """, unsafe_allow_html=True)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown(f"""
                        <div class="poster-container">
                            <img src="{recommended_movie_posters[i + 5]}" class="poster-img">
                        </div>
                        <div class="poster-title">{recommended_movie_names[i + 5]}</div>
                    """, unsafe_allow_html=True)

    # Close the poster group
    st.markdown('</div>', unsafe_allow_html=True)


## Network animation:-

from streamlit.components.v1 import html

html(
    """
<html>
<head>
   <script src="https://cdnjs.cloudflare.com/ajax/libs/tsparticles/1.18.11/tsparticles.min.js"></script>
   <style>
        html, body {
         margin: 0;
         padding: 0;
         width: 100vw;
         height: 100vh;
         overflow: hidden;
         }

      #particles {
         position: fixed;
         top: 0;
         left: 0;
         width: 80%;
         height: 80%;
      }
   </style>
</head>
<body>
   <div id="particles"></div>
   <script>
      if (typeof tsParticles !== 'undefined') {
         tsParticles.load("particles", {
            particles: {
               number: { value: 70 },
               color: { value: "#a5b198" },
               shape: { type: "circle" },
               opacity: { value: 0.7 },
               size: { value: 3 },
               links: {
                  enable: true,
                  distance: 150,
                  color: "#a5b198",
                  opacity: 0.4,
                  width: 1
               },
               move: {
                  enable: true,
                  speed: 2,
                  direction: "none",
                  outModes: { default: "bounce" }
               }
            },
            interactivity: {
               events: { onHover: { enable: true, mode: "grab" } },
               modes: { grab: { distance: 100, links: { opacity: 0.6 } } }
            },
            fullscreen: {enable: false }

         });
      } else {
         console.error("tsParticles failed to load.");
      }
   </script>
</body>
</html>
""",
    height=400,
    width=300
)

st.markdown(
    """
<style>
    iframe {
        position: fixed;
        left: 0;
        right: 0;
        top: 0;
        bottom: 0;
        width: 100vw !important;
        height: 100vw !important;
        z-index: -1;
    }
</style>
""",
    unsafe_allow_html=True,
)

## Starfield Animation:-

import streamlit.components.v1 as components


# Read the HTML file
with open("starfield.html", "r") as f:
    starfield_html = f.read()

# Embed the HTML content with a specific height
components.html(starfield_html, height=800)

# Load custom CSS
st.markdown('<style>link rel="stylesheet" href="style.css"></style>', unsafe_allow_html=True)
