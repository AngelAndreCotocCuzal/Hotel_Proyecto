from PyQt5.uic import loadUiType
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QTabWidget
from PyQt5.QtCore import Qt
from modelos.control_cocina import ModeloCocina
from modelos.control_usuario import ModeloUsuario
from modelos.control_TipoUsuario import ModeloTipoUsuario
from modelos.control_huesped import ModeloHuesped
from modelos.control_habitacion import ModeloHabitacion
from modelos.control_nivel import ModeloNivel
import bcrypt

Ui_MainWindow, QMainWindow = loadUiType('view/interfaz.ui')


class Main_menuPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self, user, main_login) -> None:
        self.ModeloCocina = ModeloCocina()
        self.ModeloUsuario = ModeloUsuario()
        self.ModeloTipoUsuario = ModeloTipoUsuario()
        self.ModeloHuesped = ModeloHuesped()
        self.ModeloHabitacion = ModeloHabitacion()
        self.ModeloNivel = ModeloNivel()
        # self.model = Modelo_pro()
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.cambiar_nombres_de_pestanas()
        
        # -------------------------- Conectar Botones con Pagina  ---------------------------
        self.btn_habitacion.clicked.connect(self.mostrar_pagina_recepcion)
        self.btn_cocina.clicked.connect(self.mostrar_pagina_cocina)
        self.btn_registro.clicked.connect(self.mostrar_pagina_registro)
        self.btn_usuario.clicked.connect(self.mostrar_pagina_usuario)
        self.btn_hab.clicked.connect(self.mostrar_pagina_habitacion)
        self.btn_nivel.clicked.connect(self.mostrar_pagina_nivel)
        # -------------------------- Botones Cocina ------------------------------------------

        self.btn_listar.clicked.connect(lambda: self.ModeloCocina.listarAlimento(self.tabla_cocina))
        self.btn_eliminar_c.clicked.connect(lambda: self.ModeloCocina.eliminarAlimento(self.tabla_cocina))
        self.btn_actualizar_c.clicked.connect(lambda: self.ModeloCocina.actualizarAlimento(self.tabla_cocina))
        self.btn_agregar_c.clicked.connect(lambda: self.ModeloCocina.CrearAlimento(self.lnl_producto.text(),
                                                                                        self.lnl_entrada.text(),
                                                                                        self.lnl_vencimiento.text(), 
                                                                                        self.tabla_cocina))

        # --------------------------------- Botones Usuario ----------------------------------

        self.btn_register_6.clicked.connect(self.registrar)
        self.btn_register_6.clicked.connect(self.limpiar_labels_register)
        self.btn_listar_u.clicked.connect(lambda: self.ModeloUsuario.listarUsuario(self.tabla_usuario))
        self.btn_eliminar_u.clicked.connect(lambda: self.ModeloUsuario.eliminarUsuario(self.tabla_usuario))
        self.btn_actualizar_u.clicked.connect(lambda: self.ModeloUsuario.actualizarUsuario(self.tabla_usuario))
        self.btn_tipoUsuario.clicked.connect(self.mostrar_pagina_tipoUsuario)
        
        # ----------------------------------- Botones Tipo Usuario ----------------------------
        
        self.btn_volver.clicked.connect(self.mostrar_pagina_usuario)
        self.btn_listar_Tipo.clicked.connect(lambda: self.ModeloTipoUsuario.listarTipoUsuario(self.tabla_tipo_usuario))
        self.btn_eliminarTipo.clicked.connect(lambda: self.ModeloTipoUsuario.eliminarTipoUsuario(self.tabla_tipo_usuario))
        self.btn_actualizarTipo.clicked.connect(lambda: self.ModeloTipoUsuario.actualizarTipoUsuario(self.tabla_tipo_usuario))
        self.btn_crear_tipo.clicked.connect(lambda: self.ModeloTipoUsuario.CrearTipoUsuario(self.lnx_tipoUsusario.text(),
                                                                                            self.tabla_tipo_usuario))
    
        # ------------------------------------------- Botones huesped ------------------------------
        self.btn_listarH.clicked.connect(lambda: self.ModeloHuesped.listarHuesped(self.tablaHuesped))
        self.btn_eliminarH.clicked.connect(lambda: self.ModeloHuesped.eliminarHueped(self.tablaHuesped))
        self.btn_actualizarH.clicked.connect(lambda: self.ModeloHuesped.actuaizarHuesped(self.tablaHuesped))
        self.btn_ingresarH.clicked.connect(lambda: self.ModeloHuesped.CrearHuesped(self.lnl_nombreH.text(),
                                                                                    self.lnl_dpiH.text(),
                                                                                    float(self.lnl_anticipo.text()),
                                                                                    self.lnl_entradaH.text(),
                                                                                    self.lnl_salidaH.text(),
                                                                                            self.tablaHuesped))

        # -------------------------------------------------- Botones Habbitacion --------------------
        self.agre_piso.clicked.connect(self.agregar_planta)
        self.btn_hab.clicked.connect(lambda: self.ModeloHabitacion.listarHabitacion(self.tablaHabitacion))

        # --------------------------------------------- Botones de Nivel -----------------------------
        self.btn_nivel.clicked.connect(lambda: self.ModeloNivel.listarNivel(self.tablaNivel))


    # Codigo de pestañas
    def cambiar_nombres_de_pestanas(self):
        # Aquí asumimos que tienes una función que obtiene el número de pestañas desde la base de datos
        numero_de_pestanas_desde_bd = self.obtener_numero_de_pestanas_desde_bd()

        # Obtener el número actual de pestañas
        numero_de_pestanas_actuales = self.tab_recepcion.count()

        # Si hay más pestañas en la BD que las actuales, agregamos pestañas adicionales
        if numero_de_pestanas_desde_bd > numero_de_pestanas_actuales:
            for i in range(numero_de_pestanas_actuales, numero_de_pestanas_desde_bd):
                # Agregar una nueva pestaña
                nueva_pestana = QWidget()
                self.tab_recepcion.addTab(nueva_pestana, f"Piso {i+1}")

        # Cambiar los nombres de las pestañas
        for i in range(numero_de_pestanas_desde_bd):
            self.tab_recepcion.setTabText(i, f"Piso {i+1}")

    def obtener_numero_de_pestanas_desde_bd(self):
        numeroh = self.ModeloNivel.NoNivele()
        return numeroh

    # -------------------------------- Metodos de Habitaciones -------------------------------------
    def agregar_planta(self):
        # Determina el nombre de la nueva planta
        planta_name = f"Piso {self.tab_recepcion.count() + 1}"
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

        self.tab_recepcion.addTab(planta_widget, planta_name)

        # Cambia el nombre de la nueva pestaña
        self.tab_recepcion.setTabText(self.tab_recepcion.count() - 1, planta_name)

    def mostrar_pagina_recepcion(self):
        self.stackedWidget.setCurrentWidget(self.pg_recepcion)
    
    def mostrar_pagina_cocina(self):
        # Cambiamos a la página de la cocina
        self.stackedWidget.setCurrentWidget(self.pg_cocina)
        
    def mostrar_pagina_registro(self):
        self.stackedWidget.setCurrentWidget(self.pg_registro)
        
    def mostrar_pagina_usuario(self):
        self.stackedWidget.setCurrentWidget(self.pg_usuario)
        
    def mostrar_pagina_tipoUsuario(self):
        self.stackedWidget.setCurrentWidget(self.page_tipoUsuario)

    def mostrar_pagina_habitacion(self):
        self.stackedWidget.setCurrentWidget(self.pg_habitacion)
        self.tablaHabitacion.setColumnWidth(0,50)
        self.tablaHabitacion.setColumnWidth(1,100)
        self.tablaHabitacion.setColumnWidth(2,70)
        self.tablaHabitacion.setColumnWidth(3,255)
        self.tablaHabitacion.setColumnWidth(4,100)
        self.tablaHabitacion.setColumnWidth(5,80)
        self.tablaHabitacion.setColumnWidth(6,80)


    def mostrar_pagina_nivel(self):
        self.stackedWidget.setCurrentWidget(self.pg_nivel)
        self.tablaNivel.setColumnWidth(0,50)
        self.tablaNivel.setColumnWidth(1,450)
        self.tablaNivel.setColumnWidth(2,80)
        self.tablaNivel.setColumnWidth(3,80)
        self.tablaNivel.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)

    def registrar(self):
        nombre = self.lnx_1nombre_2.text()
        user = self.lnx_usuario_2.text()
        cargo = self.cb_min_2.currentText()
        pw = self.lnx_password_3.text()
        pw_confirm = self.lnx_confirm_password_2.text()

        if pw == pw_confirm:
            pw = str(pw)

            salt = bcrypt.gensalt()

            # Encripta la contraseña del usuario
            hashed_password = bcrypt.hashpw(pw.encode('utf-8'), salt)
            if cargo == "Gerente":
                self.ModeloUsuario.CrearUsuario(nombre, user, hashed_password, 1, self.tabla_usuario)
            elif cargo == "Empleado":
                self.ModeloUsuario.CrearUsuario(nombre, user, hashed_password, 2, self.tabla_usuario)
            # Insertar la contraseña segura como una cadena de texto en la base de datos


        else:
            print("las contraseñas no coinciden")

    def limpiar_labels_register(self):
        self.lnx_1nombre_2.clear()
        self.lnx_confirm_password_2.clear()
        self.lnx_password_3.clear()
        self.lnx_usuario_2.clear()


        