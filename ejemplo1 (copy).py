import datetime 
import time
import pandas as pd 
import streamlit as st
from PIL import Image
#Titulos, headers etc
st.title('Titulo')
st.subheader('Subheader')
st.text('Texto: Hola Streamlit')
st.markdown('Esto es markdown h1 \n ##Esto es un h2 \n ###esto es h3')
st.success('Succes')
st.info('Información')
st.warning('warning')
st.error('Error')
st.exception("NameError('no esta definido')")
st.header("Obtener información de ayuda de python")
st.help(range)
st.header("Widgets:")
st.subheader('Checkbox')       