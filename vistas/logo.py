import streamlit as st
import os

def mostrar_logo():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(base_dir, "..", "imagenes", "logo.PNG")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(logo_path, width=200)