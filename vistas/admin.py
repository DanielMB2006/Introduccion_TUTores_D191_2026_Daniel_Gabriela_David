import streamlit as st
import pandas as pd
from database import conectar
from vistas.estilos import aplicar_estilos


def mostrar():

    aplicar_estilos()

    st.title("Panel Administrador")

    opcion = st.selectbox(

        "Seleccione módulo",

        [

        "Usuarios",
        "Tutorias"

        ]

    )


# =========================
# USUARIOS
# =========================

    if opcion == "Usuarios":

        crud_usuarios()


# =========================
# TUTORIAS
# =========================

    if opcion == "Tutorias":

        crud_tutorias()



# ===================================
# CRUD USUARIOS
# ===================================

def crud_usuarios():

    opcion = st.selectbox(

        "Acción",

        [

        "Ver",
        "Crear",
        "Editar",
        "Eliminar"

        ]

    )


# ---------- VER USUARIOS

    if opcion == "Ver":

        conexion = conectar()

        query = """

        SELECT id,nombre,correo,rol

        FROM usuarios

        """

        df = pd.read_sql(query,conexion)

        conexion.close()


        st.subheader("Usuarios")

        st.dataframe(df)



# ---------- CREAR USUARIO

    if opcion == "Crear":

        st.subheader("Crear Usuario")


        nombre = st.text_input("Nombre")

        correo = st.text_input("Correo")

        password = st.text_input(

            "Password",
            type="password"

        )


        rol = st.selectbox(

            "Rol",

            [

            "Estudiante",
            "Docente",
            "Admin"

            ]

        )


        if st.button("Guardar Usuario"):


            conexion = conectar()

            cursor = conexion.cursor()


            cursor.execute(

            """

            INSERT INTO usuarios

            (nombre,correo,password,rol)

            VALUES(%s,%s,%s,%s)

            """,

            (

            nombre,
            correo,
            password,
            rol

            )

            )


            conexion.commit()

            conexion.close()


            st.success("Usuario creado")



# ---------- EDITAR USUARIO

    if opcion == "Editar":

        conexion = conectar()

        cursor = conexion.cursor()


        cursor.execute(

        "SELECT id,nombre FROM usuarios"

        )


        usuarios = cursor.fetchall()


        lista=[]

        for u in usuarios:

            lista.append(

            str(u[0])+"-"+u[1]

            )


        seleccionado = st.selectbox(

            "Usuario",
            lista

        )


        id_usuario = seleccionado.split("-")[0]


        cursor.execute(

        """

        SELECT nombre,correo,rol

        FROM usuarios

        WHERE id=%s

        """,

        (id_usuario,)

        )


        datos = cursor.fetchone()


        nombre = st.text_input(

            "Nombre",
            datos[0]

        )


        correo = st.text_input(

            "Correo",
            datos[1]

        )


        rol = st.selectbox(

            "Rol",

            [

            "Estudiante",
            "Docente",
            "Admin"

            ],

            index=

            [

            "Estudiante",
            "Docente",
            "Admin"

            ].index(datos[2])

        )


        if st.button("Actualizar Usuario"):


            cursor.execute(

            """

            UPDATE usuarios

            SET nombre=%s,
            correo=%s,
            rol=%s

            WHERE id=%s

            """,

            (

            nombre,
            correo,
            rol,
            id_usuario

            )

            )


            conexion.commit()

            conexion.close()


            st.success("Usuario actualizado")



# ---------- ELIMINAR USUARIO

    if opcion == "Eliminar":

        conexion = conectar()

        cursor = conexion.cursor()


        cursor.execute(

        "SELECT id,nombre FROM usuarios"

        )


        usuarios = cursor.fetchall()


        lista=[]


        for u in usuarios:

            lista.append(

            str(u[0])+"-"+u[1]

            )


        seleccionado = st.selectbox(

            "Usuario",
            lista

        )


        if st.button("Eliminar Usuario"):


            id_usuario = seleccionado.split("-")[0]


            cursor.execute(

            """

            DELETE FROM usuarios

            WHERE id=%s

            """,

            (id_usuario,)

            )


            conexion.commit()

            conexion.close()


            st.success("Usuario eliminado")



# ===================================
# CRUD TUTORIAS
# ===================================

def crud_tutorias():

    opcion = st.selectbox(

        "Acción Tutorías",

        [

        "Ver",
        "Editar",
        "Eliminar"

        ]

    )


# ---------- VER TUTORIAS

    if opcion == "Ver":

        conexion = conectar()

        query = """

        SELECT

        id,
        estudiante,
        docente,
        materia,
        fecha,
        estado

        FROM tutorias

        """

        df = pd.read_sql(query,conexion)

        conexion.close()


        st.subheader("Tutorías")

        st.dataframe(df)



# ---------- EDITAR TUTORIA

    if opcion == "Editar":

        conexion = conectar()

        cursor = conexion.cursor()


        cursor.execute(

        "SELECT id,materia FROM tutorias"

        )


        tutorias = cursor.fetchall()


        lista=[]

        for t in tutorias:

            lista.append(

            str(t[0])+"-"+t[1]

            )


        seleccion = st.selectbox(

            "Tutoria",
            lista

        )


        id_tutoria = seleccion.split("-")[0]


        cursor.execute(

        """

        SELECT

        estudiante,
        docente,
        materia,
        fecha,
        estado

        FROM tutorias

        WHERE id=%s

        """,

        (id_tutoria,)

        )


        datos = cursor.fetchone()


        estudiante = st.text_input(

            "Estudiante",
            datos[0]

        )


        docente = st.text_input(

            "Docente",
            datos[1]

        )


        materia = st.text_input(

            "Materia",
            datos[2]

        )


        fecha = st.date_input(

            "Fecha",
            datos[3]

        )


        estado = st.selectbox(

            "Estado",

            [

            "Pendiente",
            "Aceptada",
            "Cancelada",
            "Finalizada"

            ],

            index=

            [

            "Pendiente",
            "Aceptada",
            "Cancelada",
            "Finalizada"

            ].index(datos[4])

        )


        if st.button("Actualizar Tutoria"):


            cursor.execute(

            """

            UPDATE tutorias

            SET

            estudiante=%s,
            docente=%s,
            materia=%s,
            fecha=%s,
            estado=%s

            WHERE id=%s

            """,

            (

            estudiante,
            docente,
            materia,
            fecha,
            estado,
            id_tutoria

            )

            )


            conexion.commit()

            conexion.close()


            st.success("Tutoria actualizada")



# ---------- ELIMINAR TUTORIA

    if opcion == "Eliminar":

        conexion = conectar()

        cursor = conexion.cursor()


        cursor.execute(

        "SELECT id,materia FROM tutorias"

        )


        tutorias = cursor.fetchall()


        lista=[]

        for t in tutorias:

            lista.append(

            str(t[0])+"-"+t[1]

            )


        seleccion = st.selectbox(

            "Tutoria",
            lista

        )


        if st.button("Eliminar Tutoria"):


            id_tutoria = seleccion.split("-")[0]


            cursor.execute(

            """

            DELETE FROM tutorias

            WHERE id=%s

            """,

            (id_tutoria,)

            )


            conexion.commit()

            conexion.close()


            st.success("Tutoria eliminada")