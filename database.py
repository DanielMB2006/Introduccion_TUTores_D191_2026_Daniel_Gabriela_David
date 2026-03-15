import mysql.connector


def conectar():

    conexion = mysql.connector.connect(

        host="shuttle.proxy.rlwy.net",
        user="root",
        password="PPnGRnTDgWNuxNutJLMZnRMHzPPGJhVU",
        database="railway",
        port=26574

    )

    return conexion