from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.nivel import RegistrarNivel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget


class ModeloNivel:
    def __init__(self) -> None:
        self.modeloNivel = RegistrarNivel()

    def listarNivel(self, tabla):

        # **************** Este Codigo omite la primera columna que le envien **************************
        table = tabla
        cocina = self.modeloNivel.obtenerNivel()
        table.setRowCount(0)

        ids = [row[0] for row in cocina]


        for row_number, row_data in enumerate(cocina):
            table.insertRow(row_number)
            for column_number, data in enumerate(
                    row_data[1:]):  # Empezar desde el segundo elemento para omitir la primera columna
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            buttonEditar = QPushButton("Editar")
            buttonEditar.clicked.connect(lambda _, row=row_number: self.subirNivel(table, row, ids[row]))
            buttonEditar.setStyleSheet("background-color: rgba(229,170,39,255);"
                                       " color: rgba(255,255,255,255); font: 75 12pt 'Archivo';")
            table.setCellWidget(row_number, 2, buttonEditar)  # Ajustar el índice para el botón editar

            buttonEliminar = QPushButton("Eliminar")
            buttonEliminar.clicked.connect(lambda _, row=row_number: self.delete_row(row, table, ids[row]))
            buttonEliminar.setStyleSheet("background-color: rgba(247,67,56,255);"
                                         " color: rgba(255,255,255,255); font: 75 12pt 'Archivo';")
            table.setCellWidget(row_number, 3, buttonEliminar)

    def subirNivel(self, tabla, row, id_nivel):

        nivel = tabla.item(row, 0).text()
        nombre = tabla.item(row, 1).text()

        self.modeloNivel.updateNivel(nivel, nombre, id_nivel)

        self.listarNivel(tabla)



    def delete_row(self, row, tabla, id_categoria):
        # Preguntar al usuario si está seguro de eliminar la fila
        respuesta = QMessageBox.question(None, "Confirmación", "¿Estás seguro de eliminar este Nivel?",
                                         QMessageBox.Yes | QMessageBox.No)

        if respuesta == QMessageBox.Yes:
            # Si el usuario confirma que está seguro
            # Verificar si hay habitaciones asociadas a esta categoría
            habitaciones_asociadas = self.modeloNivel.obtenerHabitacionesPorNivel(id_categoria)

            if not habitaciones_asociadas:
                # Si no hay habitaciones asociadas, eliminar la categoría
                self.modeloNivel.eliminarNivel(id_categoria)

                # Si se elimina con éxito de la base de datos, eliminar la fila de la tabla
                tabla.removeRow(row)
                self.listarNivel(tabla)
            else:
                # Si hay habitaciones asociadas, mostrar un mensaje de error y no permitir la eliminación
                QMessageBox.critical(None, "Error",
                                     "No se puede eliminar esta categoría porque hay habitaciones asociadas.")
        else:
            # Si el usuario cancela la acción, no hacer nada
            return

    # *** Este metodo es para optener cuantos niveles hay esto para la seccion de chekout *****
    def NoNivele(self):
        numeroH = self.modeloNivel.obtener_idPisoHabitacion() - 1
        return numeroH

    def CrearNivel(self, Nombre, Numero):
        if not Nombre or not Numero:
            print("Datos vacios")
        else:
            self.modeloNivel.insertarNivel(Nombre, Numero)
