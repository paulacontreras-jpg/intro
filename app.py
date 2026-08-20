import streamlit as st
from PIL import Image

st.title("HOLA")
st.header("En este espacio voy a poner mi mood de hoy")
st.write("hoy me siento asi:")
image = Image.open('healing.jfif')
st.image(image, caption='hola')

texto= st.text_input("Escribe tu mood","Este es tu mood")
st.write('Tu mood es',texto)

st.subheader("Ahora pondre dos culumnas")

col1, col2 =stcolumns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Todos los dias me siento con el mismo mood")
  resp=st.checkbox('Me pasa igual')
  if resp:
    st.write('TWINS')

with col2:
  st.subheader("Esta es la segunda columna")
  modo =st.checkbox("Los gatos te ayudan a manejar tu mood?")
  if modo == 'visual':
    st.write('TWINS X2')
