import streamlit as st
from PIL import Image

st.title("HOLA")
st.header("En este espacio voy a poner mi mood de hoy")
st.write("hoy me siento asi:")
image = Image.open('healing.jfif')
st.image(image, caption='hola')

texto= st.text_input("Escribe tu mood","Este es tu mood")
st.write('Tu mood es',texto)
