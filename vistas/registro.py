import streamlit as st
from vistas.estilos import aplicar_estilos

def mostrar():

    aplicar_estilos()

    st.markdown(
    '<div class="titulo">Registro Usuario</div>',
    unsafe_allow_html=True)

    st.write("")

    nombre = st.text_input("Nombre")

    codigo = st.text_input("Código")

    correo = st.text_input("Correo")

    password = st.text_input(
        "Contraseña",
        type="password"
    )

    tipo = st.selectbox(

    "Tipo usuario",

    [
    "Estudiante",
    "Docente"
    ]

    )

    st.write("")

    if st.button("Registrar"):

        st.success("Usuario registrado")