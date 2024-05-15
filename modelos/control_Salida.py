from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.nivel import RegistrarNivel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget


class ModeloRegistro:
    def __init__(self) -> None:
        self.modeloRegistro = RegistrarNivel()

    def listarRegistro(self, tabla):
        # Obtener datos de la base de datos
        registro = self.modeloRegistro.obtenerNivel()

        # Establecer el número de filas en la tabla
        tabla.setRowCount(len(registro))

        # Insertar los datos en la tabla
        for row_number, row_data in enumerate(registro):
            # Insertar datos en todas las columnas, incluida la primera columna
            for column_number, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                tabla.setItem(row_number, column_number, item)

            # Hacer la primera columna invisible
            tabla.setColumnHidden(0, True)

            # Crear botones de editar y eliminar
            buttonEditar = QPushButton("Editar")
            buttonEditar.clicked.connect(lambda _, row=row_number: self.subirNivel(tabla, row, row_data[
                0]))  # Pasar el id de la fila como argumento
            buttonEditar.setStyleSheet("background-color: rgba(229,170,39,255);"
                                       " color: rgba(255,255,255,255); font: 75 12pt 'Archivo';")
            tabla.setCellWidget(row_number, 3, buttonEditar)  # Ajustar el índice para el botón editar

            buttonEliminar = QPushButton("Eliminar")
            buttonEliminar.clicked.connect(lambda _, row=row_number: self.delete_row(row, tabla, row_data[
                0]))  # Pasar el id de la fila como argumento
            buttonEliminar.setStyleSheet("background-color: rgba(247,67,56,255);"
                                         " color: rgba(255,255,255,255); font: 75 12pt 'Archivo';")
            tabla.setCellWidget(row_number, 4, buttonEliminar)