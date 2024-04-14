# import module
import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import plotly_express as px
import time


#sitebar radio
test = st.sidebar.radio("Navigation", ['Home', 'Column', 'Tabs', 'Expander & Container', 'Status Element'])

# #Select BoX
# st.sidebar.selectbox("NavigationSB", ['NLP', 'DS', 'ML', 'Flask'])

# #Multi Select
# st.sidebar.multiselect("NavigationMS", ['NLP', 'ML', 'DS', 'DL'])

# #Sidebar INput Number
# st.sidebar.number_input("Pilih Nomor: ", 1,10 )

# #Sidebar Radio Number
# st.sidebar.radio(label="Navigation", options=[1,20,30])

# #Sidebar FIle UPloder
# st.sidebar.file_uploader("Upload File : ", type=['csv', 'pdf', 'img'])


if test == "Home":
        st.header("Vidio 1")
        st.video("https://www.youtube.com/watch?v=lVnSR3FS7h4&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=8")

        st.header("Vidio 2")
        st.video("https://www.youtube.com/watch?v=lVnSR3FS7h4&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=8")

        st.header("Vidio 3")
        st.video("https://www.youtube.com/watch?v=lVnSR3FS7h4&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=8")
    
if test == "Column":
        st.subheader("Hai, Kelas Awan Pintar")

        st.write("Kita akan belajar mengenai fungsi Colomn")

        col1, col2 = st.columns([3, 1])
        data = pd.read_csv("dataset/datagaji1.csv")

        col1.subheader("Menampilkan data berupa grafik")
        col1.line_chart(data)

        col2.subheader("Menampilkan data berupa tabel")
        col2.write(data)

if test == "Tabs":
        st.subheader("Hai, Kelas Awan Pintar")

        st.write("Kita akan belajar mengenai fungsi Tabs")

        tab1, tab2, tab3 =st.tabs(["Gambar 1", "Gambar 2", "Gambar 3"])
        gambar1 = Image.open("assets/profile.jpg")
        gambar2 = Image.open("assets/BIU.png")
        gambar3 = Image.open("assets/orbitfutureacademy_logo.jpeg")

        with tab1:
                st.header("Gambar 1")
                st.image(gambar1, width=200)
        with tab2:
                st.header("Gambar 2")
                st.image(gambar2, width=200)
        with tab3:
                st.header("Gambar 3")
                st.image(gambar3, width=200)
        st.write('----')

        tabs1, tabs2 = st.tabs(["Tabs 1", "Tabs 2"])
        data = pd.read_csv("dataset/datagaji1.csv")

        tabs1.subheader("Menampilkan Tab dengan grafik")
        tabs1.line_chart(data)

        tabs2.subheader("Menampilkan data dengan Table")
        tabs2.write(data)

if test == "Expander & Container":
        st.subheader("Hai, Kelas Awan Pintar")
        st.write("Kita akan belajar mengenai fungsi Expander & Container")
        progress = st.progress(0)
        for i in range(100):
                time.sleep(0.1)
                progress.progress(i+1)
        #halaman expander & container

        #pengambilan data

        data = pd.read_csv("dataset/datagaji1.csv")
        image = Image.open("assets/BIU.png")

        #Expander
        st.bar_chart(data)
        with st.expander("Ini Adalah Expander"):
                st.write("""
                Ini adalah contoh dari expander dan
                kita akan mencoba visualkan
                data gaji""")
                st.image(image)

        #Container
        with st.container():
                st.write("Ini Contoh Container")
                st.bar_chart(data)

        st.write("Ini Bukan didalam container")

if test == "Status Element":
        st.subheader("Hai, Kelas Awan Pintar")
        st.write("Kita akan belajar mengenai fungsi Status Element")

        #Contoh Fungsi Progress
        progress = st.progress(0)
        for i in range(100):
                time.sleep(0.1)
                progress.progress(i+1)
                
        #Contoh Fungsi Baloon
        st.balloons()

        #Contoh Fungsi Error, Success, Info, Exception, Warning
        st.error("Ini Fungsi Error")
        st.success("ini Fungsi Success")
        st.info("Ini Fungsi Info")
        st.exception(RuntimeError("Ini Adalah Error"))
        st.warning("Ini Fungsi Warning")