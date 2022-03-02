import os
import pathlib
import shutil


def print_file(file):

    f = open(file, 'r')
    lines = f.read()
    print(lines)
    f.close()

"""


"""
def replace_element_in_content( content , oldpath, newpath):
    file_lines = content.readlines()
    print(len(file_lines))
    for line in file_lines :
        if line.find(oldpath) != -1 :
            line = line.replace(oldpath, newpath)

    print(file_lines)
    return file_lines

def edit_file(file_path, oldpath, newpath):
    change = []
    with open(file_path, 'r+') as f :
        file_lines = f.readlines()
        print(len(file_lines))
        for line in file_lines:
            if line.find(oldpath) != -1:
                line = line.replace(oldpath, newpath)
            change.append(line)
    f.close()
    with open(file_path, 'w+') as f2 :
        f2.writelines(change)

def is_directory(path):
    if path.find('.') == -1 :
        return False
    else :
        return True


def not_on_C_disk(path):
    '''
    Safeguard to prevent modification on file system, people shouldn't work on disk system
    (assuming C:/ is system disk)
    '''
    if path.find('C:') == -1 :
        return True
    else :
        return False


def is_gproject(path):
    if path.find('.gproject') != -1 :
        return True
    else :
        return False


def Do_backup(refracted_dir):
    backup_path = refracted_dir + '/Refractor_Backup'
    if os.path.exists(backup_path) :
        shutil.rmtree(backup_path)
    shutil.copytree(refracted_dir,backup_path)


def edit_gproject_in_dir(dir, oldpath, newpath) :
    '''
    Use for directory refracting
    '''

    print("edit_project_in_dir")

    if os.path.exists(dir) :

        for path, subdirs, files in os.walk(dir) :
            for name in files:
                checkfile = pathlib.PurePath(path, name)
                if str(checkfile).find('Refractor_Backup') != -1:
                    pass
                else :
                    if checkfile.suffix == '.gproject' :
                        edit_file(checkfile, oldpath, newpath)
                        print_file(checkfile)


def edit_gproject_standalone(file_path, oldpath, newpath) :

    print("edit standalone file")
    if os.path.exists(file_path) :
        edit_file(file_path, oldpath, newpath)
    print_file(file_path)



class Modification:
    def __init__(self, Directory, OldPath, NewPath):
        self.Directory = Directory
        self.OldPath = OldPath
        self.NewPath = NewPath

    def get_modification_infos(self):
        return self.Directory, self.OldPath, self.NewPath

    def add_to_log(self, log):
        log.append((self.Directory, self.OldPath, self.NewPath))