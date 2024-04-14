#import module
import streamlit as st
import pandas as pd
import numpy as np

#contoh data array
a = np.array([1,2,3,4,5])
b = np.array([(1.2, 1, 2.2), (4.2, 2, 1.2)], dtype=float)

#data series
u = pd.Series([1,2,3,4,5,6,7])

#ambil data dari github
dataset = pd.read_csv("https://raw.githubusercontent.com/jumadi-cloud/Fundamental-Python/main/Dataset/datagaji1.csv")

#dictionary
profile = {
    'nama' : 'Fadhil',
    'umur' : '20',
    'Pemograman' : ['Python', 'PHP', 'Streamlit'],
    'Favorit' : {
        'Makanan' : 'Indomie',
        'Hobi' : 'Mendengarkan Musik'
    }
}

#menampilkan data

#dataframe
st.text("Ini Data Frame")
st.dataframe(b)
st.dataframe(u)
st.dataframe(dataset)

#table
st.text("Ini data Tabel")
st.table(a)
st.table(dataset)

#json
st.text("Ini JSON")
st.json(profile)

#matrix
st.text("Ini Matrix")
st.metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
    delta_color="off")