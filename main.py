
import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle('Window')
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)
        self.button = QPushButton(self)
        self.button.setText('переход к yandex')
        self.button.move(300, 10)
        self.button.show()

class Web_Page(QWebEngineView):
    def __init__(self):
        super(Web_Page, self).__init__()
        self.setWindowTitle('WebPage')

class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()

    def show_window_1(self):
        self.w1 = Window1()
        self.w1.button.clicked.connect(self.show_window_2)
        self.w1.button.clicked.connect(self.w1.close)
        self.w1.show()

    def show_window_2(self):
        self.w2 = Web_Page()
        self.w2.load(QUrl("https://yandex.ru"))
        self.w2.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Main_Window()
    w.show_window_1()
    sys.exit(app.exec_())
