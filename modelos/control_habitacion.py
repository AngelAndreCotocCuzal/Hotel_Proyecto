from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.habitacion import Habitacion
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget

class ModeloHabitacion():
    def __init__(self) -> None:
        self.modeloHabitacion = Habitacion()

    def listarHabitacion(self, tabla):
        table = tabla
        cocina = self.modeloHabitacion.obtenertablaHabitacion()
        table.setRowCount(0)
        for row_number, row_data in enumerate(cocina):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            buttonEditar = QPushButton("Editar")
            buttonEditar.clicked.connect(lambda _, row=row_number: self.edit_row(row))  # Se conecta con la función delete_row y pasa el número de fila
            buttonEditar.setStyleSheet("background-color: rgba(229,170,39,255);"
                                 " color: rgba(255,255,255,255); font: 75 12pt 'Archivo';")
            table.setCellWidget(row_number, 5, buttonEditar)

            buttonEliminar = QPushButton("Eliminar")
            buttonEliminar.clicked.connect(lambda _, row=row_number: self.delete_row(row))  # Se conecta con la función delete_row y pasa el número de fila
            buttonEliminar.setStyleSheet("background-color: rgba(247,67,56,255);"
                                 " color: rgba(255,255,255,255); font: 75 12pt 'Archivo';")
            table.setCellWidget(row_number, 6, buttonEliminar)



    def delete_row(self, row):
        print(f"se elimina el boton: {row}")

    def edit_row(self, row):
        print(f"se edita el botn: {row}")


    def CrearHabitacion(self, Numero, Detalle, Categoria, Nivel, Estado):
        if Numero and Estado and Categoria and Detalle and Nivel:
            self.modeloHabitacion.insertarHabitacion(Numero, Detalle, Categoria, Nivel, Estado)


