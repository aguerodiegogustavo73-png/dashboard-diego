import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard RyF", layout="wide")
st.title("🚀 Tablero Logístico de Diego")
st.write("Estado: Funcionando en la nube.")

archivo = st.file_uploader("Subí tu planilla de RyF aquí", type=["csv", "xlsx"])

if archivo:
    df = pd.read_csv(archivo) if archivo.name.endswith('csv') else pd.read_excel(archivo)
    st.dataframe(df)
    st.success("¡Datos cargados correctamente!")