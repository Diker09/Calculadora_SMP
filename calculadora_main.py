import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_calculadora import Ui_MainWindow


ESTILOS = """
QMainWindow, QWidget#centralwidget {
    background-color: #1e2128;
}

QLineEdit#display_operaciones {
    background-color: #14161b;
    color: #f5f6f8;
    border: none;
    border-radius: 14px;
    padding: 10px 18px;
    font-family: "Segoe UI", "Roboto", "DejaVu Sans", sans-serif;
    font-size: 38px;
    selection-background-color: #3d7eff;
}

/* Botones numéricos (estilo base, también usado por defecto) */
QPushButton {
    background-color: #2f3441;
    color: #f5f6f8;
    border: none;
    border-radius: 14px;
    font-family: "Segoe UI", "Roboto", "DejaVu Sans", sans-serif;
    font-size: 22px;
    font-weight: 600;
}
QPushButton:hover   { background-color: #3d4353; }
QPushButton:pressed { background-color: #23272f; }

/* Operadores (naranja) */
QPushButton#btn_suma, QPushButton#btn_resta,
QPushButton#btn_multiplicacion, QPushButton#btn_division {
    background-color: #ff9f1c;
    color: #1e2128;
}
QPushButton#btn_suma:hover, QPushButton#btn_resta:hover,
QPushButton#btn_multiplicacion:hover, QPushButton#btn_division:hover {
    background-color: #ffb547;
}
QPushButton#btn_suma:pressed, QPushButton#btn_resta:pressed,
QPushButton#btn_multiplicacion:pressed, QPushButton#btn_division:pressed {
    background-color: #d98400;
}

/* Igual (azul) */
QPushButton#btn_igual { background-color: #3d7eff; }
QPushButton#btn_igual:hover { background-color: #6096ff; }
QPushButton#btn_igual:pressed { background-color: #2a5fd1; }

/* Borrado total C (rojo) */
QPushButton#btn_clear { background-color: #d64550; }
QPushButton#btn_clear:hover { background-color: #e5626c; }
QPushButton#btn_clear:pressed { background-color: #a9323b; }
"""


class VentanaPrincipal(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)             
        self.setStyleSheet(ESTILOS)    

      
        self.primer_numero = None            # primer operando (float) o None
        self.operador = None                  # "+", "-", "*", "/" o None
        self.esperando_nuevo_numero = False   # True = el próximo dígito borra la pantalla

        self.conectar_señales()

   
    def conectar_señales(self):
        #Botones numéricos
        self.btn_0.clicked.connect(self.presionar_numero)
        self.btn_1.clicked.connect(self.presionar_numero)
        self.btn_2.clicked.connect(self.presionar_numero)
        self.btn_3.clicked.connect(self.presionar_numero)
        self.btn_4.clicked.connect(self.presionar_numero)
        self.btn_5.clicked.connect(self.presionar_numero)
        self.btn_6.clicked.connect(self.presionar_numero)
        self.btn_7.clicked.connect(self.presionar_numero)
        self.btn_8.clicked.connect(self.presionar_numero)
        self.btn_9.clicked.connect(self.presionar_numero)
        #Botones de operadores
        self.btn_suma.clicked.connect(self.presionar_operador)
        self.btn_resta.clicked.connect(self.presionar_operador)
        self.btn_multiplicacion.clicked.connect(self.presionar_operador)
        self.btn_division.clicked.connect(self.presionar_operador)
        #Botones de acción
        self.btn_igual.clicked.connect(self.calcular)
        self.btn_clear.clicked.connect(self.limpiar)

    def presionar_numero(self):
        boton_presionado = self.sender()      
        digito = boton_presionado.text()         
        pantalla_actual = self.display_operaciones.text()

        if self.esperando_nuevo_numero or pantalla_actual == "0":
            self.display_operaciones.setText(digito)
            self.esperando_nuevo_numero = False
        else:
            self.display_operaciones.setText(pantalla_actual + digito)

    def presionar_operador(self):
        boton_presionado = self.sender()
        simbolo = boton_presionado.text()         
        pantalla_actual = self.display_operaciones.text()

        if pantalla_actual == "Error":
            return  

       #Número negativo
        pantalla_vacia = pantalla_actual == "0" or self.esperando_nuevo_numero
        if simbolo == "-" and pantalla_vacia:
            self.display_operaciones.setText("-")
            self.esperando_nuevo_numero = False
            return
 
        if self.operador is not None and not self.esperando_nuevo_numero:
            self.calcular()

        try:
            self.primer_numero = float(self.display_operaciones.text())
        except ValueError:
            return  

        self.operador = simbolo
        self.esperando_nuevo_numero = True   

    def calcular(self):
        if self.operador is None:
            return  

        if self.esperando_nuevo_numero:
            return  
        pantalla_actual = self.display_operaciones.text()
        try:
            segundo_numero = float(pantalla_actual)
        except ValueError:
            return

        # Operaciones 
        if self.operador == "+":
            resultado = self.primer_numero + segundo_numero
        elif self.operador == "-":
            resultado = self.primer_numero - segundo_numero
        elif self.operador == "*":
            resultado = self.primer_numero * segundo_numero
        elif self.operador == "/":
            # División por cero
            if segundo_numero == 0:
                self.display_operaciones.setText("Error")
                self.primer_numero = None
                self.operador = None
                self.esperando_nuevo_numero = True
                return
            resultado = self.primer_numero / segundo_numero

        # Quitar decimales innecesarios 
        if resultado == int(resultado):
            resultado = int(resultado)

        self.display_operaciones.setText(str(resultado))

        #Guardar el resultado como primer número para la siguiente operación
        self.primer_numero = resultado
        self.operador = None
        self.esperando_nuevo_numero = True

   # Clear
    def limpiar(self):
        self.display_operaciones.setText("0")
        self.primer_numero = None
        self.operador = None
        self.esperando_nuevo_numero = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
