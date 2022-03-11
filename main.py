import shutil
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
        self.setGeometry(20, 20, 512, 512)
        self.setWindowTitle('ENSI Path Refractor')
        self.setFixedSize(580,512)
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
        self.RefractButton.setFixedSize(200,200)
        self.RefractButton.setText('Refract Paths')
        self.RefractButton.move(156,256)
        self.RefractButton.setStyleSheet("background-color: #cc021d")

        self.KeepBackupPopUp = PyQt5.QtWidgets.QMessageBox(self)
        self.KeepBackupPopUp.setText("Do you want to delete backup")
        self.KeepBackupPopUp.setWindowTitle('Refraction done')
        self.KeepBackupPopUp.setIcon(PyQt5.QtWidgets.QMessageBox.Question)
        self.KeepBackupPopUp.setStandardButtons(PyQt5.QtWidgets.QMessageBox.Yes | PyQt5.QtWidgets.QMessageBox.No)


    def connections(self):
        pass

    def events(self):
        self.button1.clicked.connect(lambda : self.file_input_browse_clicked(self.File_input))
        self.OldPathButton.clicked.connect(lambda : self.file_input_browse_clicked(self.OldPathInput))
        self.NewPathButton.clicked.connect(lambda : self.file_input_browse_clicked(self.NewPathInput))
        self.RefractButton.clicked.connect(self.Do_refraction)

    def Do_refraction(self) :


        file_path = self.File_input.text()
        old_path = self.OldPathInput.text()
        new_path = self.NewPathInput.text()

        if os.path.exists(file_path) and edit_lib.not_on_C_disk(file_path):
            if self.File_input.text().find('.gproject') != -1:
                new_content = edit_lib.read_file(file_path,old_path,new_path)
                backup_path = edit_lib.do_backup_file(file_path)
                no_problem = edit_lib.write_new_file(file_path, new_content)

                if no_problem :
                    user_answer = self.KeepBackupPopUp.exec_()
                    print(user_answer)
                    if user_answer == 65536:
                        print('keeping backup')
                        return
                    if user_answer == 16384 :
                        print('deleting backup')
                        os.remove(backup_path)
                else :
                    print('Something went wrong')
                    try :
                        shutil.copy(backup_path, file_path)
                        os.remove(backup_path)
                    except :
                        print('something wen wrong with delete')
            if self.File_input.text().find('.gproject') == -1:
                backup_path = edit_lib.Do_backup(file_path)
                no_problem = edit_lib.read_then_edit_gproject_in_dir(file_path, old_path, new_path)
                if no_problem :
                    user_answer = self.KeepBackupPopUp.exec_()
                    print(user_answer)
                    if user_answer == 65536:
                        print('keeping backup')
                        return
                    if user_answer == 16384:
                        print('deleting backup')
                        shutil.rmtree(backup_path)
                else :
                    print('Something went wrong')
                    try:
                        shutil.copy(backup_path, file_path)
                        shutil.rmtree(backup_path)
                    except:
                        print('something wen wrong with delete')
        else :
            print(r'File or directory doesn\'t exist')




    def file_input_browse_clicked(self, input):
        if self.FolderCheck1.checkState() :
            response = PyQt5.QtWidgets.QFileDialog.getExistingDirectory(parent=self, caption='Select directory to refract',
                                                                         directory=r'D:\\')
        else :
            response = PyQt5.QtWidgets.QFileDialog.getOpenFileName(parent=self, caption='Select Guerilla file to refract',
                                                                   directory=r'D:\\',
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




if __name__ == '__main__' :
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

