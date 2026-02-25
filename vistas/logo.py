import streamlit as st

def mostrar_logo():

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.image(
            "imagenes/logo.png",
            width=200
        )