from PyQt5.uic import loadUiType
from PyQt5 import QtCore
from modelos.control_hospedaje import ModeloHospedaje
from modelos.control_habitacion import ModeloHabitacion
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog


# Cargar la interfaz de usuario de CrearNivel.ui
Ui_CrearNivel, _ = loadUiType('view/CrearHospedamiento.ui')


class CrearHospedamiento(QMainWindow, Ui_CrearNivel):
    def __init__(self, numeroH, tabla, *args, **kwargs):
        self.numeroHabitacion = numeroH
        self.table = tabla
        self.Modelo = ModeloHospedaje()
        self.ModeloHabitacion = ModeloHabitacion()
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.mostrardatos()

        self.btn_guardar.clicked.connect(self.guardarCat)
        self.btn_cerrar.clicked.connect(self.close_event)

    def mostrardatos(self):
        # Obtener datos de la habitación
        datos_habitaciones = self.Modelo.datosporHabitacion(self.numeroHabitacion)

        # Verificar si se encontraron datos para la habitación
        if datos_habitaciones:
            habitacion_data = datos_habitaciones[0]  # Tomamos solo la primera fila de resultado

            # Configurar los labels con los datos correspondientes
            self.lnl_numeroHabitacion.setText(f"No. Habitación: {habitacion_data[0]}")
            self.lbl_categoria.setText(f"Categoría: {habitacion_data[1]}")
            self.lbl_detalle.setText(f"Detalle: {habitacion_data[2]}")
            self.lbl_condicion.setText(f"Condicion: {habitacion_data[3]}")
            self.lbl_precio.setText(f"Precio: {habitacion_data[4]}")

            self.lnl_precio.setText(str(habitacion_data[4]))

            # Bloquear los labels para que no se puedan editar
            self.lnl_numeroHabitacion.setEnabled(False)
            self.lbl_categoria.setEnabled(False)
            self.lbl_detalle.setEnabled(False)
            self.lbl_condicion.setEnabled(False)
            self.lbl_precio.setEnabled(False)
            self.lnl_precio.setEnabled(False)
        else:
            # Si no se encontraron datos, se puede mostrar un mensaje o realizar alguna otra acción
            print("No se encontraron datos para la habitación:", self.numeroHabitacion)

    def guardarCat(self):


        nombre = self.lnl_nombreH.text()
        dpi = self.lnl_dpiH.text()
        adelanto_text = self.lnl_adelanto.text()
        fechaE = self.lnl_fechaEntrada.text()
        fechaS = self.lnl_FechaSalida.text()

        # Obtener el texto del QLineEdit
        texto = self.lnl_numeroHabitacion.text()

        # Dividir la cadena en partes usando ': ' como separador y tomar la segunda parte
        partes = texto.split(': ')
        if len(partes) == 2:  # Verificar que se dividió correctamente en dos partes
            numero = partes[1]  # El número de habitación está en la segunda parte
            num = int(numero)  # Convertir el número a entero

        else:
            print("El formato del texto no es válido.")

        # Verificar si el campo de adelanto está vacío o no
        if adelanto_text:
            # Convertir el adelanto a un número flotante si el campo no está vacío
            try:
                anticipo = float(adelanto_text)
            except ValueError:
                print("El adelanto debe ser un número válido")
                return
        else:
            # Mostrar un mensaje de error si el campo de adelanto está vacío
            print("El campo de adelanto está vacío")
            return

        if not nombre or not dpi or not fechaE or not fechaS:
            print("Faltan campos por llenar")
        else:
            self.Modelo.CrearHospedaje(nombre, dpi, anticipo, fechaE, fechaS, num)
            self.close_event()
        self.ModeloHabitacion.updateEstadoHabitacion(2, num)

    def close_event(self):
        self.close()

