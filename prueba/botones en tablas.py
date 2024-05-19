from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget


class prueba(QMainWindow):

    def __init__(self):
        super().__init__()
        import datetime

    # Obtener la fecha actual
        fecha_actual = datetime.date.today()

        print("La fecha de hoy es:", fecha_actual)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Botones por fila")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Nombre", "Edad", "Acción"])

        layout.addWidget(self.tableWidget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.populate_table()

    def populate_table(self):
        data = [("Juan", 25), ("María", 30), ("Pedro", 40)]

        self.tableWidget.setRowCount(len(data))

        for i, (name, age) in enumerate(data):
            name_item = QTableWidgetItem(name)
            age_item = QTableWidgetItem(str(age))

            self.tableWidget.setItem(i, 0, name_item)
            self.tableWidget.setItem(i, 1, age_item)

            button = QPushButton("Eliminar")
            button.clicked.connect(lambda _, row=i: self.delete_row(row))  # Se conecta con la función delete_row y pasa el número de fila
            self.tableWidget.setCellWidget(i, 2, button)

    def delete_row(self, row):
        self.tableWidget.removeRow(row)


if __name__ == "__main__":
    app = QApplication([])
    window = prueba()
    window.show()
    app.exec()
