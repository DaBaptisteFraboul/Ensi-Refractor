import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import edit_lib

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(20,20,512,512)
    win.setWindowTitle('ENSI Path Refractor')
    win.show()
    sys.exit(app.exec_())

window()