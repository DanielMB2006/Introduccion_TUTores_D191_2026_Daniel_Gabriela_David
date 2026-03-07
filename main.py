import streamlit as st

# Importar vistas
from vistas import login
from vistas import registro
from vistas import estudiante
from vistas import docente
from vistas import admin

from vistas.estilos import aplicar_estilos
from vistas.estilos import barra_lateral


# ------------------------
# Configuración página
# ------------------------

st.set_page_config(

    page_title="Sistema de Tutorías",
    layout="centered"

)


# ------------------------
# Estilos
# ------------------------

aplicar_estilos()
barra_lateral()


# ------------------------
# Variables sesión
# ------------------------

if "rol" not in st.session_state:
    st.session_state["rol"] = None

if "usuario" not in st.session_state:
    st.session_state["usuario"] = ""

if "pagina" not in st.session_state:
    st.session_state["pagina"] = "login"


# ------------------------
# SIN LOGIN
# ------------------------

if st.session_state["rol"] == None:


    if st.session_state["pagina"] == "login":

        login.mostrar()


    elif st.session_state["pagina"] == "registro":

        registro.mostrar()



# ------------------------
# ESTUDIANTE
# ------------------------

elif st.session_state["rol"] == "Estudiante":

    st.sidebar.title("Panel Estudiante")

    st.sidebar.write(
        "Usuario:",
        st.session_state["usuario"]
    )

    st.sidebar.write("")

    if st.sidebar.button("Cerrar sesión"):

        st.session_state["rol"] = None
        st.session_state["usuario"] = ""
        st.session_state["pagina"] = "login"

        st.rerun()


    estudiante.mostrar()



# ------------------------
# DOCENTE
# ------------------------

elif st.session_state["rol"] == "Docente":

    st.sidebar.title("Panel Docente")

    st.sidebar.write(
        "Usuario:",
        st.session_state["usuario"]
    )

    st.sidebar.write("")

    if st.sidebar.button("Cerrar sesión"):

        st.session_state["rol"] = None
        st.session_state["usuario"] = ""
        st.session_state["pagina"] = "login"

        st.rerun()


    docente.mostrar()



# ------------------------
# ADMIN
# ------------------------

elif st.session_state["rol"] == "Admin":

    st.sidebar.title("Panel Admin")

    st.sidebar.write(
        "Usuario:",
        st.session_state["usuario"]
    )

    st.sidebar.write("")

    if st.sidebar.button("Cerrar sesión"):

        st.session_state["rol"] = None
        st.session_state["usuario"] = ""
        st.session_state["pagina"] = "login"

        st.rerun()


    admin.mostrar()