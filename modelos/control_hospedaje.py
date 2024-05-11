import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.hospedaje import RegistrarHospedaje
from modelos.control_habitacion import ModeloHabitacion
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget
from modelos.control_nivel import ModeloNivel


class ModeloHospedaje:
    def __init__(self) -> None:
        self.ModeloHabitacion = ModeloHabitacion()
        self.modeloCategoria = RegistrarHospedaje()
        self.ModeloNivel = ModeloNivel()

    def obtenerIdsHabitacionesOcupadas(self):
        habitaciones = self.modeloCategoria.obtenerIdsHabitacionesOcupadas()
        return habitaciones
    def habitacionesenuso(self):
        habitaciones = self.modeloCategoria.habitacionesenuso()
        return habitaciones
    def CrearHospedaje(self, nombre, dpi, anticipo, fechaE, fechaS, num):


        self.modeloCategoria.insertarHospedaje(nombre, dpi, anticipo, fechaE, fechaS, num)

    def datosporHabitacion(self, numeroHabitacion):
        datos = self.modeloCategoria.obtenerdatosporHabitacion(numeroHabitacion)
        return datos

    def opteneridpornumero(self, numeroHabitacion):
        datos = self.modeloCategoria.obteneridporHabitacion(numeroHabitacion)
        return datos
    def listarCategoria(self, tabla):

        # **************** Este Codigo omite la primera columna que le envien **************************
        table = tabla
        categoria = self.modeloCategoria.obtenerCategoria()
        table.setRowCount(0)

        ids = [row[0] for row in categoria]


        for row_number, row_data in enumerate(categoria):
            table.insertRow(row_number)
            for column_number, data in enumerate(
                    row_data[1:]):  # Empezar desde el segundo elemento para omitir la primera columna
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            buttonEditar = QPushButton("Editar")
            buttonEditar.clicked.connect(lambda _, row=row_number: self.subirCategoria(table, row, ids[row]))
            buttonEditar.setStyleSheet("background-color: rgba(229,170,39,255);"
                                       " color: rgba(255,255,255,255); font: 75 12pt 'Archivo';")
            table.setCellWidget(row_number, 2, buttonEditar)  # Ajustar el índice para el botón editar

            buttonEliminar = QPushButton("Eliminar")
            buttonEliminar.clicked.connect(lambda _, row=row_number: self.delete_row(row, table, ids[row]))
            buttonEliminar.setStyleSheet("background-color: rgba(247,67,56,255);"
                                         " color: rgba(255,255,255,255); font: 75 12pt 'Archivo';")
            table.setCellWidget(row_number, 3, buttonEliminar)

    def subirCategoria(self, tabla, row, id_nivel):

        nombre = tabla.item(row, 0).text()
        precio = float(tabla.item(row, 1).text())

        self.modeloCategoria.updateCategoria(nombre, precio, id_nivel)

        self.listarCategoria(tabla)

    def delete_row(self, row, tabla, id_categoria):
        # Preguntar al usuario si está seguro de eliminar la fila
        respuesta = QMessageBox.question(None, "Confirmación", "¿Estás seguro de eliminar esta categoría?",
                                         QMessageBox.Yes | QMessageBox.No)

        if respuesta == QMessageBox.Yes:
            # Si el usuario confirma que está seguro
            # Verificar si hay habitaciones asociadas a esta categoría
            habitaciones_asociadas = self.modeloCategoria.obtenerHabitacionesPorCategoria(id_categoria)

            if not habitaciones_asociadas:
                # Si no hay habitaciones asociadas, eliminar la categoría
                self.modeloCategoria.eliminarCategoria(id_categoria)

                # Si se elimina con éxito de la base de datos, eliminar la fila de la tabla
                tabla.removeRow(row)
                self.listarCategoria(tabla)
            else:
                # Si hay habitaciones asociadas, mostrar un mensaje de error y no permitir la eliminación
                QMessageBox.critical(None, "Error",
                                     "No se puede eliminar esta categoría porque hay habitaciones asociadas.")
        else:
            # Si el usuario cancela la acción, no hacer nada
            return



    def actualizar_paneles_y_botones(self, tabla):
        self.tab_recepcion = tabla
        # Obtener el número de niveles desde la base de datos
        numero_de_niveles = self.obtener_numero_de_niveles_desde_bd()

        # Limpiar pestañas
        self.tab_recepcion.clear()

        # Crear un diccionario para mapear los niveles a las habitaciones correspondientes
        habitaciones_por_nivel = {}

        # Obtener datos de las habitaciones
        habitaciones = self.ModeloHabitacion.obtenerDatosHabitacionInterfaz()

        # Obtener la lista de IDs de habitaciones asociadas al cliente
        lista_ids_habitaciones_cliente = self.habitacionesenuso()

        # Convertir la lista de IDs de habitaciones asociadas al cliente en una lista de números de habitación
        numeros_habitacion_cliente = [habitacion[1] for habitacion in lista_ids_habitaciones_cliente]

        # Agrupar las habitaciones por nivel
        for habitacion in habitaciones:
            nivel = habitacion[3]
            if nivel not in habitaciones_por_nivel:
                habitaciones_por_nivel[nivel] = []
            habitaciones_por_nivel[nivel].append(habitacion)

        # Crear pestañas y botones de habitación para cada nivel
        for nivel in range(1, numero_de_niveles + 1):
            # Crear una pestaña para el nivel actual
            tab = QWidget()
            layout = QVBoxLayout()

            # Obtener las habitaciones para el nivel actual
            habitaciones_nivel = habitaciones_por_nivel.get(f"Nivel {nivel}", [])

            # Crear botones de habitación para el nivel actual
            for habitacion in habitaciones_nivel:
                estado = habitacion[2]
                # Verificar si la habitación está asociada al cliente y actualizar el estado
                if habitacion[0] in [id_habitacion[0] for id_habitacion in
                                     lista_ids_habitaciones_cliente] and estado == "libre":
                    estado = "ocupado"  # Cambiar el estado a "ocupado"

                button = QPushButton(f"Habitación {habitacion[0]}\nTipo: {habitacion[1]}\nEstado: {estado}")
                # Conecta la señal clicked del botón a la función pg_CrearHospedamiento con el número de habitación correspondiente
                # button.clicked.connect(lambda _, num=habitacion[0]: self.pg_CrearHospedamiento(num))
                layout.addWidget(button)


    def obtener_numero_de_niveles_desde_bd(self):
        # Suponiendo que hay un método en ModeloNivel que devuelve el número de niveles
        # Reemplaza 'NoNivele()' con el método real si tiene un nombre diferente
        numero_niveles = self.ModeloNivel.NoNivele()
        return numero_niveles


