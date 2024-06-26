# Import Library
import streamlit as st
from PIL import Image
import os

st.subheader("Halaman Image")
st.write(
            """
            Di dalam Halaman Image akan mempelajari bagaimana caranya Upload file dan Membaca File dengan _type_ Gambar _(png, jpeg, jpg)_.
            
            Dalam tutorial ini sebenernya sudah pernah kita bahas 
            di [video](https://www.youtube.com/watch?v=lVnSR3FS7h4&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=8) 
            dan ini adalah materi lanjutannya
            """
        )

#Method/Fungsi
def load_image(image_file):
    img = Image.open(image_file)
    return img


image_file = st.file_uploader("Uplaod Image", type=['png', 'jpeg', 'jpg'])
if image_file is not None:
    st.write(type(image_file))
    file_detail = {"Filename":image_file.name, 
                   "FileType":image_file.type,
                   "FileSize":image_file.size}
    st.write(file_detail)

    st.image(load_image(image_file))