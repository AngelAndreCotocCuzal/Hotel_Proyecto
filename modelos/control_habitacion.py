from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.habitacion import Habitacion
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget

class ModeloHabitacion():
    def __init__(self) -> None:
        self.modeloHabitacion = Habitacion()


    def listarHabitacion(self, tabla):
        table = tabla
        cocina = self.modeloHabitacion.\
            obtenertablaHabitacion()
        table.setRowCount(0)
        for row_number, row_data in enumerate(cocina):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                button = QPushButton("Editar")
                button.clicked.connect(lambda _, row=row_number: self.delete_row(row))  # Se conecta con la función delete_row y pasa el número de fila
                table.setCellWidget(row_number, 5, button)

    def delete_row(self, row):
        print(f"se edita el boton: {row}")

    def CrearHabitacion(self, Numero, Estado, Categoria, Detalle, Nivel):
        if Numero and Estado and Categoria and Detalle and Nivel:
            self.modeloHabitacion.insertarHabitacion(Numero, Estado, Categoria, Detalle, Nivel)

    def NoNivele(self):
        numeroH = self.modeloHabitacion.obtener_idPisoHabitacion() - 1
        return numeroH
