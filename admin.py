admin.py
import streamlit as st
from vistas.estilos import aplicar_estilos

def mostrar():

    aplicar_estilos()

    st.title("Panel Administrador")

    st.write("")

    st.subheader("Usuarios")

    st.write("Juan")

    st.write("Maria")

    st.write("Carlos")

    st.write("")

    st.subheader("Tutorías")

    st.write("Matemáticas")

    st.write("Programación")

    if st.button("Eliminar"):

        st.error("Registro eliminado")