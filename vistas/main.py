import streamlit as st

from vistas import login
from vistas import registro
from vistas import estudiante
from vistas import docente
from vistas import admin


st.set_page_config(

page_title="Tutores 4.0",

layout="wide"

)


# LOGO

st.sidebar.image(

"imagenes/logo.png",

width=150

)


st.sidebar.title("Tutores 4.0")


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