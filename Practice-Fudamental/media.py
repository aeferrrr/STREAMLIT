# import module
import streamlit as st
from PIL import Image


# Title
st.title("Kelas Awan Pintar")

# Header
st.header("Ayu Belajar Bagaimana Cara untuk menampilkan Media elements di streamlit [sumber](https://docs.streamlit.io/library/api-reference/media)")

# 1. Image

gambar1 = Image.open('assets/BIU.png')
gambar2 = Image.open('assets/profile.jpg')
gambar3 = Image.open('assets/orbitfutureacademy_logo.jpeg')

st.image(gambar1, caption="Ini Logo Kampus Ku")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Gambar 1")
   st.image(gambar1)

with col2:
   st.header("Gambar 2")
   st.image(gambar2)

with col3:
   st.header("Gambar 3")
   st.image(gambar3)




# 2. Audio

audio = open('assets/audio1.oga', 'rb')
audio1 = audio.read()

st.audio(audio1)

# 3. Video

vidio = open('assets/star.mp4', 'rb')
vidio1 = vidio.read()

st.video(vidio1)

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Vidio 1")
   st.video("https://www.youtube.com/watch?v=lVnSR3FS7h4&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=8")

with col2:
   st.header("Vidio 2")
   st.video("https://www.youtube.com/watch?v=lVnSR3FS7h4&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=8")

with col3:
   st.header("Vidio 3")
   st.video("https://www.youtube.com/watch?v=lVnSR3FS7h4&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=8")
   