import streamlit as st
import cv2
import numpy as np
import pytesseract

st.title("Reconocimiento Óptico de Caracteres - Cámara")

img_file_buffer = st.camera_input("Toma una foto")

with st.sidebar:
    st.subheader("Opciones de Imagen")
    filtro = st.radio("Aplicar Filtro", ('Sin Filtro', 'Con Filtro'))

if img_file_buffer is not None:
    # Decodificar la imagen tomada por la cámara a formato OpenCV
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Inversión de colores opcional para mejorar contraste en algunos textos
    if filtro == 'Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)

    # Conversión de BGR a RGB para pytesseract
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    
    # Extracción e impresión de texto
    text = pytesseract.image_to_string(img_rgb)
    
    st.subheader("Texto Detectado:")
    if text.strip():
        st.write(text)
    else:
        st.warning("No se detectó ningún texto en la imagen.")
