import streamlit as st


def aplicar_estilos():

    st.markdown("""

    <style>


    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #6E6E6E;
    }


    /* Títulos */
    h1 {
        color: #0a7f3f;
        text-align: center;
    }

    h2 {
        color: #0a7f3f;
    }

    h3 {
        color: #0a7f3f;
    }


    /* Botones */
    .stButton > button {

        background-color: #0a7f3f;
        color: white;
        border-radius: 8px;
        height: 45px;
        width: 100%;
        font-size: 16px;
        border:none;

    }

    .stButton > button:hover {

        background-color: #0c9c4d;

    }


    /* Inputs */

    .stTextInput input {

        border-radius: 8px;
        border:1px solid #0a7f3f;
        height:40px;

    }


    /* Caja central */

    .block-container{

        padding-top: 3rem;
        max-width:700px;

    }


    </style>

    """, unsafe_allow_html=True)



def mostrar_logo():

    st.sidebar.image(

        "imagenes/logo.png",

        width=150

    )


def barra_lateral():

    mostrar_logo()

    st.sidebar.markdown("---")

    st.sidebar.write("Sistema de Tutorías")