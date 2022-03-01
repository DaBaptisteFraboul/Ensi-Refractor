import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import edit_lib

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(20,20,560,512)
        self.setWindowTitle('ENSI Path Refractor')
        self.UiComponents()
        self.show()


    def UiComponents(self):
        pass



def browse_file_path(widget, win):
    browser = PyQt5.QtWidgets.QFileDialog(win)
    path1 = browser.getOpenFileName()
    widget.setText(path1[0])

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(20,20,560,512)
    win.setWindowTitle('ENSI Path Refractor')
    DirectoryLabel = PyQt5.QtWidgets.QLabel(win)
    DirectoryLabel.setText('Directory or file to refract')
    DirectoryLabel.adjustSize()
    DirectoryLabel.move(20,10)
    OldPathLabel = PyQt5.QtWidgets.QLabel(win)
    OldPathLabel.setText('Old path to change')
    OldPathLabel.adjustSize()
    OldPathLabel.move(20,80)
    dialog = PyQt5.QtWidgets.QFileDialog(win)
    dialog.setFileMode(PyQt5.QtWidgets.QFileDialog.Directory)
    path1 = dialog.getOpenFileName()
    button1 = PyQt5.QtWidgets.QPushButton(win)
    button1.setText('Browse...')
    button1.adjustSize()
    button1.move(480, 44)
    print(path1)
    File_input = PyQt5.QtWidgets.QLineEdit(win)
    File_input.move(20,40)
    File_input.displayText()
    File_input.setFixedWidth(450)
    File_input.setText(path1[0])

    win.show()
    sys.exit(app.exec_())

window()

