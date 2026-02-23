import streamlit as st

from vistas import login
from vistas import registro
from vistas import estudiante
from vistas import docente
from vistas import admin

st.title("Sistema Tutores 4.0")

menu = st.sidebar.selectbox(
    "Menú",
    [
        "Login",
        "Registro",
        "Estudiante",
        "Docente",
        "Administrador"
    ]
)

if menu == "Login":
    login.mostrar()

if menu == "Registro":
    registro.mostrar()

if menu == "Estudiante":
    estudiante.mostrar()

if menu == "Docente":
    docente.mostrar()

if menu == "Administrador":
    admin.mostrar()