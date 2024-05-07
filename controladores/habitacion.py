from bd.conexion import conecciones


class Habitacion():
    def __init__(self) -> None:
        self.conn = conecciones()  # Llama a la función para obtener la conexión

    def obtener_idHabitacion(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id) FROM habitaciones")

        count = cursor.fetchone()[0]
        if count is None:
            count = 1
        else:
            count += 1
        return count

    def obtener_idPisoHabitacion(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(idNivelHabitacion) FROM nivelhabitacion")

        count = cursor.fetchone()[0]
        if count is None:
            count = 1
        else:
            count += 1
        return count

    def obtener_habitacion(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM habitaciones"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    def obtener_NivelHabitacion(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM nivelhabitacion"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def insertarHabitacion(self, Numero, Detalle, Categoria, Nivel, Estado):
        id = self.obtener_idHabitacion()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO habitaciones (`id`, `NoHabitacion`, `Detalle`, 
            `CategoriaHabitacion_idCategoriaHabitacion`, 
            `NivelHabitacion_idNivelHabitacion`, `EstadoHabitacion_id1`) VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (id, Numero, Detalle, Categoria, Nivel, Estado))
            self.conn.commit()

    def insertarNivelHabitacion(self, Nombre, Nivel):
        id = self.obtener_idPisoHabitacion()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO nivelhabitacion (`idNivelHabitacion`, `Nombre`, `Nivel`) VALUES (%s,%s,%s)"""
            cursor.execute(sql, (id, Nombre, Nivel))
            self.conn.commit()

    def ActualizarHabitacion(self, Id, Numero, Detalle, Categoria, Nivel, Estado):
        with self.conn.cursor() as cursor:
            sql = """UPDATE habitaciones SET NoHabitacion = %s, Detalle = %s,
            CategoriaHabitacion_idCategoriaHabitacion = %s,
            NivelHabitacion_idNivelHabitacion = %s,
            EstadoHabitacion_id1 = %s WHERE id = %s"""
            cursor.execute(sql, (Numero, Detalle, Categoria, Nivel, Estado, Id))
            self.conn.commit()

    def obtenerHabitacion(self, cod):
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM habitaciones WHERE id = '" + cod + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def eliminarHabitacion(self, id):
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM habitaciones WHERE id = '" + id + "'"
            cursor.execute(sql)
            self.conn.commit()

    def obtenertablaHabitacion(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT h.NoHabitacion, c.Nombre, c.Precio, h.Detalle, n.Nombre FROM habitaciones h 
            inner join categoriahabitacion c on h.CategoriaHabitacion_idCategoriaHabitacion = c.idCategoriaHabitacion
            inner join nivelhabitacion n on h.NivelHabitacion_idNivelHabitacion = n.idNivelHabitacion"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def obtenerTablaNivel(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM nivelhabitacion"""

            cursor.execute(sql)
            result = cursor.fetchall()
            return result