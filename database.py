import mysql.connector

def conectar():

    conexion = mysql.connector.connect(

        host="localhost",

        user="root",

        password="",

        database="tutores"

    )

    return conexion