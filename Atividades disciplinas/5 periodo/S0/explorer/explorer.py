import os
import platform
#from pwd import getpwuid
from datetime import datetime
from stat import *

import shlex
import winreg

def get_default_windows_app(suffix):
    try:
        class_root = winreg.QueryValue(winreg.HKEY_CLASSES_ROOT, suffix)
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r'{}\shell\open\command'.format(class_root)) as key:
            command = winreg.QueryValueEx(key, '')[0]
            return shlex.split(command)[0]
    except Exception as e:
        return "Nenhum"


is_dir = lambda path: os.path.splitext(path)[-1] == ""

def get_file_info(file_path):
    """ 
    Retorna as seguintes informações do arquivo:

    1.Nome
    2.Tamanho
    3.Data de criação
    4.Última alteração
    5.Qual aplicativo reconhece o arquivo
    6.proprietário

    """

    file_base_name = os.path.basename(file_path)
    file_name, file_ext = os.path.splitext(file_base_name)

    st = os.stat(file_path)

    file_creation_time = st.st_ctime
    file_modification_time = st.st_mtime
    file_size_bytes = st.st_size 

    if platform.system() == "Windows":
        file_creation_date = os.path.getctime(file_path)





    return {
        "Nome arquivo" : file_name + file_ext,
        "Tamanho" : file_size_bytes,
        "Data de criação" : datetime.fromtimestamp(file_creation_time).strftime("%d/%m/%Y"),
        "Última alteração" : datetime.fromtimestamp(file_modification_time).strftime("%d/%m/%Y"),
        "Aplicação" : os.path.basename(get_default_windows_app(file_ext)) if file_ext != "" else "Explorer",
        "Proprietário" : "Nenhum"
    }


def get_files_and_subfolders(folder_path):
    subfolder_list = []
    files_list = []

    for path in os.listdir(folder_path):
        file_base_name = os.path.basename(path)
        if is_dir(file_base_name):
            subfolder_list.append(file_base_name)
        else:
            files_list.append(file_base_name)

    
    return subfolder_list, files_list