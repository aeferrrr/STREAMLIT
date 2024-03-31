# import module
import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# Title
st.title("Kelas Awan Pintar")

# Header
st.header("Ayo Belajar Bagaimana Cara Buat widgets di streamlit [sumber](https://docs.streamlit.io/library/api-reference/widgets)")



# 1. Button

if(st.button("Kelas Awan Pintar")):
    st.text("Welcome To Playlist Belajar Streamlit")

# 2. Checkbox

if st.checkbox("Show/Hidden"):
    st.text(("Saya Arief, Saya Belajar Streamlit"))

# 3. radio button

status =  st.radio("Pilih Playlist: ", ("NLP", "ML", "DS", "Streamlit"))
#menampilkan
st.write("Sahabat Kelas Awan Pintar yang Bersemangat Belajar",status)

# 4. Selectbox

domain = st.selectbox("Sahabat Kelas Awan Pintar yang Bersemangat Belajar:",
                      ['NLP', 'Streamlit', 'Flask', 'DL', 'DS', 'ML'] )

st.write("Sekarang Saya Sedang Belajar:", domain)

# 5. Multiselect

domain = st.multiselect("Sahabat Kelas Awan Pintar yang Bersemangat Belajar:",
                      ['NLP', 'Streamlit', 'Flask', 'DL', 'DS', 'ML'] )

st.write("Sekarang Saya Sedang Belajar:", len(domain), 'Playlist')

# 6. Slider & Select-slider

level = st.slider("Pilih: ", 1,101)
st.text('Dipilih:{}'.format(level))

hari = st.select_slider("Pilih Nama Hari: ",
                        options=['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
st.write('Hari Kesukaanku: ', hari)

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)

# 7. Input Text 
nama = st.text_input('Masukan Nama Anda: ', '')
st.write('Nama Kamu Adalah: ',nama)

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

# 8. Input Number 

nosuk = st.number_input("Masukan Nomor Kesukaan: ", 1,10)

st.write("Nomor yang kamu pilih", nosuk)

# 9. Text area

kalimat = st.text_area("Masukan Kalimat Kesukaan", "")

st.write("Kalimat Kamu : ", kalimat)

# 10. Date input

st.date_input("Silahkan Input Date")

# 11. Time input

st.time_input("Masukan Waktu Anda")

# 12. File Uploader

st.file_uploader("Upload File Anda", type=['csv', 'pdf', 'txt'])

# 13. Color picker

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)
