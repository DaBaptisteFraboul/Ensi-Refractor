import os
import shutil


def print_file(file):

    f = open(file, 'r')
    lines = f.read()
    print(lines)
    f.close()

def replace_element_in_content( content) :
    file_lines = content.readlines()
    print(len(file_lines))
    for line in file_lines :
        line = line.replace('set', 'prout')
        print(line)

def edit_file(file):

    with open(file, 'r+') as file :
        # edit file here
        '''
        Replace element with another
        '''
        replace_element_in_content(file)
        file.close()

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
    if path.find('C:/') == -1 :
        return True
    else :
        return False

