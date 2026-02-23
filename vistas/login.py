import streamlit as st

def mostrar():

    st.title("Login")

    correo = st.text_input("Correo")

    contraseña = st.text_input(
        "Contraseña",
        type="password"
    )

    if st.button("Ingresar"):
        st.success("Intentando ingresar...")