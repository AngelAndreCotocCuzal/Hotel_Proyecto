import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QTabWidget


class HotelApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hotel App")

        self.tab_widget = QTabWidget()  # TabWidget para manejar las habitaciones
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tab_widget)

        # Botón para agregar pestaña (planta) al TabWidget
        self.add_tab_btn = QPushButton("Agregar Planta")
        self.add_tab_btn.clicked.connect(self.agregar_planta)
        self.layout.addWidget(self.add_tab_btn)

        self.setLayout(self.layout)

    def agregar_planta(self):
        # Agrega una nueva pestaña (planta) al TabWidget
        planta_name = f"Planta {self.tab_widget.count() + 1}"
        planta_widget = QWidget()
        planta_layout = QVBoxLayout()
        planta_widget.setLayout(planta_layout)

        # Layout para los botones de habitaciones en la nueva pestaña
        planta_habitaciones_layout = QVBoxLayout()
        planta_layout.addLayout(planta_habitaciones_layout)

        # Botón para agregar habitación en la nueva pestaña
        add_btn = QPushButton("Agregar Habitación")
        add_btn.clicked.connect(lambda: self.agregar_habitacion(planta_habitaciones_layout))
        planta_layout.addWidget(add_btn)

        self.tab_widget.addTab(planta_widget, planta_name)

    def agregar_habitacion(self, layout):
        # Encuentra el layout de la última fila
        try:
            last_row_layout = layout.itemAt(layout.count() - 1).layout()
        except AttributeError:
            # Si no hay ninguna fila, crea una nueva
            last_row_layout = None

        if last_row_layout is None or last_row_layout.count() == 3:
            # Si la última fila está llena o no existe, crea una nueva fila
            new_row_layout = QHBoxLayout()
            layout.addLayout(new_row_layout)
            last_row_layout = new_row_layout

        num_habitacion = layout.count() + 1
        habitacion_btn = QPushButton(f"Habitación {num_habitacion}")
        habitacion_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        habitacion_btn.setFixedSize(100, 50)
        last_row_layout.addWidget(habitacion_btn)


def main():
    app = QApplication(sys.argv)
    window = HotelApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

