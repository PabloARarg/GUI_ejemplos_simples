from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.uic import loadUi
import sys

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Carga la interfaz de usuario desde el archivo .ui
        loadUi("untitled.ui", self)  # Reemplaza "tudiseño.ui" con la ruta de tu archivo .ui

        # Cargamos la imagen desde un archivo (por ejemplo, image.jpg)
        self.pixmap = QPixmap("img.png")
        self.pixmap_2 = QPixmap("img_2.png")
        
        # Escalamos la imagen para que se ajuste al tamaño de la etiqueta
        self.pixmap = self.pixmap.scaled(self.imgLabel.size())
        self.pixmap_2 = self.pixmap_2.scaled(self.imgLabel.size())
        
        # Establecemos la imagen en la etiqueta
        self.imgLabel.setPixmap(self.pixmap)

        self.boton.clicked.connect(self.iniciar)
        self.boton_2.clicked.connect(self.parar)
        
    def iniciar(self):
        # Inicia la animación del GIF
        self.imgLabel.setPixmap(self.pixmap_2)
   
    def parar(self):
        self.imgLabel.setPixmap(self.pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec())
