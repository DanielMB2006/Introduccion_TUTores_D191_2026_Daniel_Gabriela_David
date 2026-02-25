import streamlit as st
from vistas.estilos import aplicar_estilos

def mostrar():

    aplicar_estilos()

    st.title("Panel Estudiante")

    st.write("")

    st.subheader("Tutorías disponibles")

    st.write("Matemáticas")
    st.write("Programación")
    st.write("Física")

    st.write("")

    if st.button("Reservar"):

        st.success("Tutoría reservada")


    st.write("")


    st.subheader("Mis reservas")

    st.write("Matemáticas")

    if st.button("Cancelar"):

        st.warning("Tutoría cancelada")