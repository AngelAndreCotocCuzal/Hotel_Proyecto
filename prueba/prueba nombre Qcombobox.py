import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QComboBox, QWidget

class CrearHabitacionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crear Habitación")

        layout = QVBoxLayout()
        self.combo_habitacion = QComboBox()
        self.combo_habitacion.addItem("Selecciona habitación")  # Agregar mensaje inicial
        self.combo_habitacion.addItems(["Nivel 1", "Nivel 2", "Nivel 3"])  # Opciones reales
        self.combo_habitacion.view().setMinimumWidth(150)  # Ancho mínimo para mostrar el mensaje completo
        self.combo_habitacion.setCurrentIndex(0)  # Establecer el mensaje inicial como seleccionado
        self.combo_habitacion.currentIndexChanged.connect(self.habitacion_seleccionada)
        layout.addWidget(self.combo_habitacion)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def habitacion_seleccionada(self, index):
        if index == 0:
            # No hacer nada si se selecciona el mensaje inicial
            return
        seleccion = self.combo_habitacion.currentText()
        print("Nivel seleccionado:", seleccion)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CrearHabitacionWindow()
    window.show()
    sys.exit(app.exec_())

