from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget
from PyQt5.QtGui import QPolygon
import sys


class Example(QWidget):

    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height
        self.init_gui()


    def init_gui(self):
        desktop = QApplication.desktop()
        left = (desktop.width() - self.__width) // 2
        top  = (desktop.height()- self.__height) // 2

        self.setGeometry(left, top, self.__width, self.__height)
        self.setWindowTitle("效果")
        self.show()

    @property
    def getWidth(self):
        print(self.__width)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example(400,200)
    ex.getWidth
    sys.exit(app.exec())