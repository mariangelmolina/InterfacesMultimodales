import streamlit as st
from PIL import Image

st.title("HOLA :) me llamo Mariangel")

st.header("apps yay")
st.write("aca voy a poner una foto")
image = Image.open('DSC00365.JPG')
st.image(image, caption='Interfaces multimodales')

texto = st.text_input('hi again', 'again')
st.write('el texto es:'texto)

st.subheader("ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("esta es la primer")
  st.write("las interfaces multimodales mejorar la UX")
  resp = st.checkbox("estoy de acuerdo")
  if resp:
    st.write('correcto!')

with col2:
  st.subheader("esta es la segunda")
  modo = st.radio("que modalidad es la principal en tu interfaz", ('visual', 'auditivo', 'tactil'))
  if modo == 'visual':
    st.write('la vista es fundamental')
  if modo == 'auditivo':
    st.write('la audicion es fundamental')
  if modo == 'tactil':
    st.write('el tacto es fundamental')

st.subheader("uso de botones")
if st.button('presiona el boton'):
  st.write('gracias por presionar')
else:
  st.write('no has presionado')



