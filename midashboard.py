import streamlit as st
import pandas as pd
from google import genai

st.set_page_config(page_title="Dashboard Diego", layout="wide")
st.title("📊 Dashboard de Diego con IA")

api_key_real = "AIzaSyDgCUXbVw90T2FXkADSHM5a9lzc3avgfJg"

archivo = st.file_uploader("Sube tu archivo de Diego", type=["csv", "xlsx"])

if archivo:
    # Este bloque lee el archivo con más cuidado
    try:
        df = pd.read_csv(archivo) if archivo.name.endswith('.csv') else pd.read_excel(archivo)
        df = df.fillna(0) # Esto cambia celdas vacías por ceros para que no falle
        st.write("### Datos cargados correctamente ✅", df.head())
        
        if st.button("🤖 Analizar con Gemini"):
            client = genai.Client(api_key=api_key_real)
            # Solo enviamos un resumen numérico para no saturar a la IA
            resumen = f"Analiza estos datos de Diego: {df.describe().to_string()}"
            response = client.models.generate_content(model="gemini-2.0-flash", contents=resumen)
            st.info(response.text)
            
        st.bar_chart(df.select_dtypes(include=['number']))
        
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")