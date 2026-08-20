import streamlit as st
from PIL import image
st.title("HOLA")
st.header("En este espacio voy a poner mi mood de hoy")
st.write("hoy me siento asi:")
image = image.open("#healing.jfif")
st.image(image,captions="sisoy")
