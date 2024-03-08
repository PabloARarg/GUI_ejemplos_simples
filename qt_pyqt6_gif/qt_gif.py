import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QMovie
from PyQt6.uic import loadUi

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Carga la interfaz de usuario desde el archivo .ui
        loadUi("untitled.ui", self)  # Reemplaza "tudiseño.ui" con la ruta de tu archivo .ui
        
        # Crea un objeto QMovie y configura el GIF
        self.movie = QMovie("gif.gif")  # Reemplaza "tugif.gif" con la ruta de tu archivo GIF
        self.gifLabel.setMovie(self.movie)

        # Escala el GIF al tamaño de la QLabel
        self.gifLabel.setScaledContents(True)

        self.boton.clicked.connect(self.iniciar)
        self.boton_2.clicked.connect(self.parar)
        
    def iniciar(self):
        # Inicia la animación del GIF
        self.movie.start()
   
    def parar(self):
        self.movie.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec())
