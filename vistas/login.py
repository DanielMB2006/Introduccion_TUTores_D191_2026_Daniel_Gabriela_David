import streamlit as st
from database import conectar
from vistas.estilos import aplicar_estilos



def mostrar():

    aplicar_estilos()
    

    # Centrar contenido
    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.title("Inicia Sesion")

        correo = st.text_input("Correo")

        password = st.text_input(
            "Contraseña",
            type="password"
        )

        st.write("")

        colA, colB = st.columns(2)

        # BOTON LOGIN
        with colA:

            if st.button("Ingresar"):

                conexion = conectar()
                cursor = conexion.cursor()

                sql = """
                SELECT * FROM usuarios
                WHERE correo=%s AND password=%s
                """

                datos = (correo, password)

                cursor.execute(sql, datos)

                usuario = cursor.fetchone()

                conexion.close()

                if usuario:

                    st.success("Bienvenido " + usuario[1])

                    st.session_state["usuario"] = usuario[1]
                    st.session_state["rol"] = usuario[4]

                    st.rerun()

                else:

                    st.error("Correo o contraseña incorrectos")


        # BOTON REGISTRO
        with colB:

            if st.button("Registrarse"):

                st.session_state["pagina"] = "registro"

                st.rerun()