import os
import pathlib
import shutil
import re



def print_file(file):

    f = open(file, 'r')
    lines = f.read()
    print(lines)
    f.close()


def read_file(file, oldpath, newpath) :
    new_content = []
    with open(file, 'r+') as f :
        line_content = f.readlines()
        for line in line_content :
            line = line.replace(oldpath, newpath)
            new_content.append(line)
    return new_content


def do_backup_file(file) :
    '''

    '''
    backup_path = re.split(r',|/|\\|\\\\', file)
    for element in backup_path :
        if element == '' :
            backup_path.remove(element)
    filename = backup_path[-1]
    filename= filename.split('.')
    filename[0] += '_EnsiRefractorBackup'
    filename = filename[0] + '.' + filename[1]
    backup_path[-1] = filename
    newpath = backup_path[0]
    for element in backup_path :
        if element == backup_path[0] :
            pass
        else :
            newpath += '/' + element
    print(file)
    print(newpath)
    shutil.copyfile(file, newpath)
    return newpath


def write_new_file(path, data) :
    try :
        with open(path, 'w+') as f :
            for lines in data :
                f.writelines(lines)
        return True
    except :
        return False

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
                print(line)
            change.append(line)
    f.close()
    with open(file_path, 'w+') as f2 :
        f2.writelines(change)
    f2.close()

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
    refracted_dir_parent = os.path.dirname(refracted_dir)
    backup_path = refracted_dir_parent + '_Refractor_Backup'
    if os.path.exists(backup_path) :
        shutil.rmtree(backup_path)
    shutil.copytree(refracted_dir,backup_path)

    return backup_path


def read_then_edit_gproject_in_dir(dir, oldpath, newpath) :
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
                        new_content = read_file(checkfile, oldpath, newpath)
                        try :
                            write_new_file(checkfile, new_content)
                            return True
                        except :
                            print('Error trying to write file: ', checkfile)
                            return False
                    else :
                        pass


def edit_gproject_standalone(file_path, oldpath, newpath) :

    print("edit standalone file")
    if os.path.exists(file_path):
        edit_file(file_path, oldpath, newpath)
    print_file(file_path)



class Modification:

    def __init__(self, directory, old_path, new_path):
        self.Directory = directory
        self.OldPath = old_path
        self.NewPath = new_path

    def get_modification_info(self):
        return self.Directory, self.OldPath, self.NewPath

    def add_to_log(self, log):
        log.append((self.Directory, self.OldPath, self.NewPath))
