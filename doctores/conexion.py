import mysql.connector


def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="J_C_C_R_python",
        port=3306
    )

    cursor = database.cursor(buffered=True)

    return[database, cursor]
