import streamlit as st
import pandas as pd
from vistas.estilos import aplicar_estilos
from database import conectar


def mostrar():

    aplicar_estilos()

    st.title("Panel Docente")


# ==========================
# OBTENER TUTORIAS DOCENTE
# ==========================

    conexion = conectar()


    query = """

    SELECT

    id,
    estudiante,
    materia,
    fecha,
    estado

    FROM tutorias

    WHERE docente=%s

    """


    df = pd.read_sql(

        query,
        conexion,
        params=(st.session_state["usuario"],)

    )


    conexion.close()


# ==========================
# TABLA
# ==========================

    st.subheader("Mis Tutorías")


    if len(df) == 0:

        st.info("No tienes tutorías asignadas")

        return


    st.dataframe(df)


# ==========================
# GESTIONAR TUTORIA
# ==========================

    st.subheader("Gestionar Tutoría")


    lista = []

    for i in df["id"]:

        lista.append(str(i))


    id_tutoria = st.selectbox(

        "Seleccione Tutoría",
        lista

    )


# ==========================
# BOTONES
# ==========================

    col1,col2,col3 = st.columns(3)


# ACEPTAR

    if col1.button("Aceptar"):


        conexion = conectar()

        cursor = conexion.cursor()


        cursor.execute(

        """

        UPDATE tutorias

        SET estado='Aceptada'

        WHERE id=%s

        """,

        (id_tutoria,)

        )


        conexion.commit()

        conexion.close()


        st.success("Tutoría aceptada")

        st.rerun()



# RECHAZAR

    if col2.button("Rechazar"):


        conexion = conectar()

        cursor = conexion.cursor()


        cursor.execute(

        """

        UPDATE tutorias

        SET estado='Rechazada'

        WHERE id=%s

        """,

        (id_tutoria,)

        )


        conexion.commit()

        conexion.close()


        st.success("Tutoría rechazada")

        st.rerun()



# FINALIZAR

    if col3.button("Finalizar"):


        conexion = conectar()

        cursor = conexion.cursor()


        cursor.execute(

        """

        UPDATE tutorias

        SET estado='Finalizada'

        WHERE id=%s

        """,

        (id_tutoria,)

        )


        conexion.commit()

        conexion.close()


        st.success("Tutoría finalizada")

        st.rerun()