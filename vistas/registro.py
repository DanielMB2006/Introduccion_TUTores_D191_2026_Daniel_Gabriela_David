import streamlit as st
from database import conectar
from vistas.estilos import aplicar_estilos



def mostrar():

    # Aplicar diseño
    aplicar_estilos()
    

    # Centrar formulario
    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.title("Registro de Usuario")

        nombre = st.text_input("Nombre")

        correo = st.text_input("Correo")

        password = st.text_input(
            "Contraseña",
            type="password"
        )

        rol = st.selectbox(
            "Rol",
            ["Estudiante","Docente"]
        )

        st.write("")

        colA, colB = st.columns(2)

        # BOTON REGISTRAR
        with colA:

            if st.button("Registrar"):

                if nombre=="" or correo=="" or password=="":

                    st.warning("Complete todos los campos")

                else:

                    conexion = conectar()

                    cursor = conexion.cursor()

                    sql = """
                    INSERT INTO usuarios
                    (nombre,correo,password,rol)
                    VALUES(%s,%s,%s,%s)
                    """

                    datos = (
                        nombre,
                        correo,
                        password,
                        rol
                    )

                    cursor.execute(sql,datos)

                    conexion.commit()

                    conexion.close()

                    st.success("Usuario registrado correctamente")


        # BOTON VOLVER
        with colB:

            if st.button("Volver al Login"):

                st.session_state["pagina"] = "login"

                st.rerun()