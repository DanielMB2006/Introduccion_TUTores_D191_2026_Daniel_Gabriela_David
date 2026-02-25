import streamlit as st

def aplicar_estilos():

    st.markdown("""
    <style>

    body {
        background-color: white;
    }

    .titulo{
        color:#2e7d32;
        text-align:center;
        font-size:35px;
        font-weight:bold;
    }

    .subtitulo{
        text-align:center;
        color:#1b5e20;
        font-size:18px;
    }

    .stButton > button{

        background-color:#2e7d32;
        color:white;

        border-radius:8px;
        height:40px;
        width:100%;
    }

    .stButton > button:hover{

        background-color:#1b5e20;

    }

    </style>

    """, unsafe_allow_html=True)
