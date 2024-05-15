from bd.conexion import conecciones

class RegistrarNivel:
    def __init__(self):
        self.conn = conecciones()

    def obteneridRegistro(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id) FROM factura")

        count = cursor.fetchone()[0]
        count = count + 1
        return count
    def obtenerRegistro(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT idNivelHabitacion, Nivel, Nombre FROM nivelhabitacion"""

            cursor.execute(sql)
            result = cursor.fetchall()
            return result
