import streamlit as st
from vistas.estilos import aplicar_estilos

def mostrar():

    aplicar_estilos()

    st.markdown(
    '<div class="titulo">Sistema Tutores 4.0</div>',
    unsafe_allow_html=True)

    st.markdown(
    '<div class="subtitulo">Inicio de Sesión</div>',
    unsafe_allow_html=True)

    st.write("")

    correo = st.text_input("Correo")

    password = st.text_input(
        "Contraseña",
        type="password"
    )

    rol = st.selectbox(

    "Rol",

    [
    "Estudiante",
    "Docente",
    "Administrador"
    ]

    )

    st.write("")

    if st.button("Ingresar"):

        st.success("Ingreso correcto")