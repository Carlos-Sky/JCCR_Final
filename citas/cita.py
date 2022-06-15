from sqlite3 import connect
import doctores.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Cita:

    def __init__(self, doctor_id, titulo="", descripcion=""):
        self.doctor_id = doctor_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        sql = "INSERT INTO citas VALUES(null,%s,%s,%s, NOW())"
        cita = (self.doctor_id, self.titulo, self.descripcion)
        cursor.execute(sql, cita)
        database.commit()
        return [cursor.rowcount, self]

    def listar(self):
        sql = f"SELECT * FROM citas  WHERE doctor_id = {self.doctor_id}"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def editar(self):
        sql = f"SELECT * FROM citas  WHERE doctor_id = {self.doctor_id}"
        cursor.execute(sql)
        database.commit()

    def eliminar(self, titulo):
        sql = f"DELETE FROM citas WHERE doctor_id = {self.doctor_id} AND titulo LIKE '%{titulo}%´"
        cursor.execute(sql)
        database.commit()

        return[cursor.roncount, self]
