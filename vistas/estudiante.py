import streamlit as st
import pandas as pd
from database import conectar


def mostrar():

    st.title("Panel Estudiante")


    # =========================
    # SOLICITAR TUTORIA
    # =========================

    st.subheader("Solicitar Tutoría")


    materia = st.text_input("Materia")


    # -------------------------
    # Obtener docentes
    # -------------------------

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute(

    """

    SELECT nombre

    FROM usuarios

    WHERE rol='docente'

    """

    )

    docentes = cursor.fetchall()

    conexion.close()


    lista_docentes = []

    for d in docentes:

        lista_docentes.append(d[0])


    # Selector de docentes

    docente = st.selectbox(

        "Docente",

        lista_docentes

    )


    fecha = st.date_input("Fecha")


    # -------------------------
    # Botón solicitar
    # -------------------------

    if st.button("Solicitar Tutoría"):


        if materia == "":

            st.warning("Ingrese la materia")


        else:

            conexion = conectar()

            cursor = conexion.cursor()


            sql = """

            INSERT INTO tutorias

            (estudiante,docente,materia,fecha,estado)

            VALUES(%s,%s,%s,%s,%s)

            """


            datos = (

            st.session_state["usuario"],

            docente,

            materia,

            fecha,

            "Pendiente"

            )


            cursor.execute(sql,datos)

            conexion.commit()

            conexion.close()


            st.success("Tutoría solicitada")

            st.rerun()



    # =========================
    # MIS TUTORIAS
    # =========================

    st.subheader("Mis Tutorías")


    conexion = conectar()


    query = """

    SELECT

    id,
    docente,
    materia,
    fecha,
    estado

    FROM tutorias

    WHERE estudiante=%s

    """


    df = pd.read_sql(

        query,

        conexion,

        params=(st.session_state["usuario"],)

    )


    conexion.close()


    if len(df) == 0:

        st.info("No tienes tutorías")


    else:

        st.dataframe(df)