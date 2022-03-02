import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow
import PyQt5.QtGui, PyQt5.QtCore
import sys
import edit_lib
import os

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.variables()

        self.UiComponents()
        self.events()



    def UiComponents(self):
        #icon = PyQt5.QtGui.QIcon('')
        #self.setWindowIcon(icon)
        self.setGeometry(20, 20, 560, 512)
        self.setWindowTitle('ENSI Path Refractor')

        self.DirectoryLabel = PyQt5.QtWidgets.QLabel(self)
        self.DirectoryLabel.setText('Directory or file to refract')
        self.DirectoryLabel.adjustSize()
        self.DirectoryLabel.move(20, 10)

        self.button1 = PyQt5.QtWidgets.QPushButton(self)
        self.button1.setText('Browse...')
        self.button1.adjustSize()
        self.button1.move(475, 44)


        self.FolderCheck1 = PyQt5.QtWidgets.QCheckBox(self)
        self.FolderCheck1.move(475, 70)
        self.FolderCheck1.setChecked(True)
        self.FolderCheck1.setText('Browse folder')
        self.FolderCheck1.adjustSize()

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
        self.OldPathButton.move(475,105)

        self.FolderCheck2 = PyQt5.QtWidgets.QCheckBox(self)
        self.FolderCheck2.move(475, 105+26)
        self.FolderCheck2.setChecked(True)
        self.FolderCheck2.setText('Browse folder')
        self.FolderCheck2.adjustSize()
        self.FolderCheck2.clicked.connect(self.click_on_browse_check)

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
        self.NewPathButton.move(475,164)

        self.FolderCheck3 = PyQt5.QtWidgets.QCheckBox(self)
        self.FolderCheck3.move(475, 164 + 26)
        self.FolderCheck3.setChecked(True)
        self.FolderCheck3.setText('Browse folder')
        self.FolderCheck3.adjustSize()
        self.FolderCheck3.clicked.connect(self.click_on_browse_check)

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
        self.button1.clicked.connect(lambda : self.file_input_browse_clicked(self.File_input))
        self.OldPathButton.clicked.connect(lambda : self.file_input_browse_clicked(self.OldPathInput))
        self.NewPathButton.clicked.connect(lambda : self.file_input_browse_clicked(self.NewPathInput))
        self.RefractButton.clicked.connect(self.Do_refraction)

    def Do_refraction(self):
        '''
        Refraction when Refract button pushed
        :return:
        '''
        if self.CheckMark.checkState() :
            backup = True
        else :
            backup = False
        if self.File_input.text().find('.gproject') != -1 :
            refract_folder = False
        else :
            refract_folder = True

        file_path = self.File_input.text()
        old = self.OldPathInput.text()
        new = self.NewPathInput.text()
        if edit_lib.not_on_C_disk(file_path) :
            print("NOT ON C")
            print(self.CheckMark.checkState())
            print(backup)
            if backup :
                print("Backup")
                if refract_folder :
                    print("Backup under folder")
                    edit_lib.Do_backup(self.File_input.text())
                    edit_lib.edit_gproject_in_dir(file_path, old, new)
                else :
                    print('backup log directly under file')
                    edit_lib.Do_backup(os.path.dirname(self.File_input.text()))
                    edit_lib.edit_gproject_standalone(file_path, old, new)
            elif backup == False :
                print(self.File_input.text().find('.gproject') != -1)
                if refract_folder :
                    "edit project in dir without backup"
                    edit_lib.edit_gproject_in_dir(file_path, old, new)

                else :
                    "edit standalone project wihtout backup"
                    edit_lib.edit_gproject_standalone(file_path, old, new)

        else:
            print('Warning I dont Run On C:/ Disk')
            return


    def file_input_browse_clicked(self, input):
        if self.FolderCheck1.checkState() :
            response = PyQt5.QtWidgets.QFileDialog.getExistingDirectory(parent=self, caption='Select directory to refract',
                                                                         directory=r'D:\\')
        else :
            response = PyQt5.QtWidgets.QFileDialog.getOpenFileName(parent=self, caption='Select Guerilla file to refract', directory=r'D:\\',
                                                                   filter=('Guerilla File (*.gproject)'))
        if bool(response) == False or response == ("",""):
            print('Empty')
        else :
            try :
                input.setText(response)
            except :
                input.setText(response[0])

    def variables(self):
        self.log = []
        self.are_paths_folders = True

    def click_on_browse_check(self):
        if self.are_paths_folders == False :
            self.set_to_folder_path()
        else :
            self.set_to_file_path()

    def set_to_file_path(self):
        self.are_paths_folders = False
        self.FolderCheck3.setChecked(False)
        self.FolderCheck2.setChecked(False)

    def set_to_folder_path(self):
        self.are_paths_folders = True
        self.FolderCheck3.setChecked(True)
        self.FolderCheck2.setChecked(True)

    def print_path(self):
        text = self.File_input.text()
        edit_lib.look_gproject_in_dir(text)



    '''def browse_and_set_path(self):
        try :
            response = PyQt5.QtWidgets.QFileDialog.getOpenFileName(parent=self,caption='Open Gfile',directory = r'D:\\', filter=('Guerilla File (*.gproject)'))
            print(response)
            response2 =  PyQt5.QtWidgets.QFileDialog.getExistingDirectory(parent=self,caption='Open Directory',directory = r'D:\\')
            print(response2)
        except :
            print('error')
            pass'''



if __name__ == '__main__' :
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
