import streamlit as st
from PIL import Image

st.title("HOLA :) me llamo Mariangel")

st.header("apps yay")
st.write("aca voy a poner una foto")
image = Image.open('DSC00365.JPG')
st.image(image, caption='Interfaces multimodales')

