import streamlit as st
import pandas as pd
st.title("Data Survey Kepuasan")
# Membaca file Excel
df = pd.read_excel("data_simulasi_50_siswa_20_soal_baru")
st.write("Preview Data:")
st.dataframe(df)
