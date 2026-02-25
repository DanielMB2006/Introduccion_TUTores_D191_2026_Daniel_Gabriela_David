docente.py
import streamlit as st
from vistas.estilos import aplicar_estilos

def mostrar():

    aplicar_estilos()

    st.title("Panel Docente")

    st.write("")

    st.subheader("Tutorías agendadas")

    st.write("Matemáticas")

    st.write("Programación")

    st.write("Física")