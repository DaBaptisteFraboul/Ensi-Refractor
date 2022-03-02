import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow
import PyQt5.QtGui, PyQt5.QtCore
import sys
import edit_lib

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()


        self.UiComponents()
        self.events()



    def UiComponents(self):

        self.setGeometry(20, 20, 560, 512)
        self.setWindowTitle('ENSI Path Refractor')

        self.DirectoryLabel = PyQt5.QtWidgets.QLabel(self)
        self.DirectoryLabel.setText('Directory or file to refract')
        self.DirectoryLabel.adjustSize()
        self.DirectoryLabel.move(20, 10)

        self.button1 = PyQt5.QtWidgets.QPushButton(self)
        self.button1.setText('Browse...')
        self.button1.adjustSize()
        self.button1.move(480, 44)

        self.File_input = PyQt5.QtWidgets.QLineEdit(self)
        self.File_input.move(20, 40)
        self.File_input.displayText()
        self.File_input.setFixedWidth(450)

        self.OldPathLabel = PyQt5.QtWidgets.QLabel(self)
        self.OldPathLabel.setText('Old path to change')
        self.OldPathLabel.adjustSize()
        self.OldPathLabel.move(20, 80)

        self.OldPathInput = PyQt5.QtWidgets.QLineEdit(self)
        self.OldPathInput.move(20,100)
        self.OldPathInput.setFixedWidth(450)

        self.OldPathButton = PyQt5.QtWidgets.QPushButton(self)
        self.OldPathButton.setText('Browse...')
        self.OldPathButton.adjustSize()
        self.OldPathButton.move(480,105)

        self.NewPathLabel = PyQt5.QtWidgets.QLabel(self)
        self.NewPathLabel.setText('New path to replace with')
        self.NewPathLabel.adjustSize()
        self.NewPathLabel.move(20, 140)

        self.NewPathInput = PyQt5.QtWidgets.QLineEdit(self)
        self.NewPathInput.move(20,160)
        self.NewPathInput.setFixedWidth(450)

        self.NewPathButton = PyQt5.QtWidgets.QPushButton(self)
        self.NewPathButton.setText('Browse...')
        self.NewPathButton.adjustSize()
        self.NewPathButton.move(480,164)

        self.CheckMark = PyQt5.QtWidgets.QCheckBox(self)
        self.CheckMark.setChecked(True)
        self.CheckMark.move(20,200)
        self.CheckMark.setText('Do Backup folder')
        self.CheckMark.setLayoutDirection(PyQt5.QtCore.Qt.RightToLeft)

        self.RefractButton = PyQt5.QtWidgets.QPushButton(self)
        self.RefractButton.setFixedSize(200,150)
        self.RefractButton.setText('Refract Paths')
        self.RefractButton.move(125,205)

    def connections(self):
        pass

    def events(self):
        self.button1.clicked.connect(self.browse_and_set_path)

    def browse_and_set_path(self):
        self.dialog = PyQt5.QtWidgets.QFileDialog(self)
        self.dialog.setFileMode(PyQt5.QtWidgets.QFileDialog.Directory)
        self.path1 = self.dialog.getOpenFileName()[0]
        print(self.path1)
        self.File_input.setText(self.path1)

def browse_file_path(widget, win):
    browser = PyQt5.QtWidgets.QFileDialog(win)
    path1 = browser.getOpenFileName()
    widget.setText(path1[0])

"""def window():
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
    button1.clicked.connect(print("Bonjour"))
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
window()"""

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
