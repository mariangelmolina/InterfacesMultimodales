import streamlit as st
from PIL import Image
from gtts import gTTS
import os

# -----------------------------
# TÍTULO E IMAGEN
# -----------------------------

st.title("HOLA :) me llamo Mariangel")

st.header("apps yay")
st.write("aca voy a poner una foto")

image = Image.open('DSC00365.JPG')
st.image(image, caption='Interfaces multimodales')

# -----------------------------
# ENTRADA DE TEXTO
# -----------------------------

texto = st.text_input('hi again', 'again')
st.write('el texto es:', texto)

# -----------------------------
# COLUMNAS
# -----------------------------

st.subheader("ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("esta es la primer")
    st.write("las interfaces multimodales mejoran la UX")

    resp = st.checkbox("estoy de acuerdo")

    if resp:
        st.write('correcto!')

with col2:
    st.subheader("esta es la segunda")

    modo = st.radio(
        "que modalidad es la principal en tu interfaz",
        ('visual', 'auditivo', 'tactil')
    )

    if modo == 'visual':
        st.write('la vista es fundamental')

    elif modo == 'auditivo':
        st.write('la audicion es fundamental')

    elif modo == 'tactil':
        st.write('el tacto es fundamental')

# -----------------------------
# BOTÓN
# -----------------------------

st.subheader("uso de botones")

if st.button('presiona el boton'):
    st.write('gracias por presionar')
else:
    st.write('no has presionado')

# -----------------------------
# SELECTBOX
# -----------------------------

st.subheader("Selectbox")

in_mod = st.selectbox(
    "Selecciona la modalidad",
    ("Audio", "Visual", "Háptico")
)

if in_mod == "Audio":
    set_mod = "Reproducir audio"

elif in_mod == "Visual":
    set_mod = "Reproducir video"

elif in_mod == "Háptico":
    set_mod = "Activar vibración"

st.write("La acción es:", set_mod)

# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.subheader("Configura la modalidad")

    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva", "Háptica")
    )

    st.write("Modalidad seleccionada:", mod_radio)

# -----------------------------
# TEXT TO SPEECH
# -----------------------------

st.subheader("🔊 Conversión de Texto a Audio")

st.write(
    "Escribe cualquier texto y conviértelo a voz."
)

texto_audio = st.text_area(
    "Introduce el texto a escuchar:"
)

idioma = st.selectbox(
    "Selecciona el idioma del audio",
    ("Español", "English")
)

if idioma == "Español":
    lg = "es"
else:
    lg = "en"

if st.button("Convertir a Audio"):

    if texto_audio.strip() != "":

        tts = gTTS(
            text=texto_audio,
            lang=lg
        )

        nombre_archivo = "audio_generado.mp3"
        tts.save(nombre_archivo)

        st.success("✅ Audio generado correctamente")

        with open(nombre_archivo, "rb") as audio_file:
            audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")

    else:
        st.warning("⚠️ Por favor escribe un texto antes de convertirlo.")
