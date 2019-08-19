import os
import sys
from click import clear

from explorer import get_file_info, get_files_and_subfolders


COMMANDS_INFO = "1 - Open [file_name]  2 - cd [folder_name] 3 - back  4 - exit\n \
Open : open an file based on his name \n \
cd : Change to the path of selected folder \n \
back :  back one folder \n \
exit : Quit from application"  



def show_files(subfolder_list, files_list):
    print("------------------------------------------------------------------------------------------")
    print("| Nome arquivo | Tamanho | Data de criação | Última alteração | Aplicação | Proprietário |")
    print("------------------------------------------------------------------------------------------")

    for subfolder_name in sorted(subfolder_list):
        show_line(subfolder_name)

    for file_name in sorted(files_list):
        show_line(file_name)

def show_line(file_name):
    file_info = get_file_info(file_name)

    for key, value in file_info.items():
        value = str(value)
        key_len = len(key)
        value_len = len(value)
        if key_len < value_len:
            value = value[:len(key) - 3] + "..."
        elif key_len > value_len:
            value = value + " "*(key_len - value_len)

        print("| {0} ".format(value), end = "")

    
    print("!\n------------------------------------------------------------------------------------------")

        

def update_screen(path):
    clear
    os.chdir(path)
    subfolder_list, files_list = get_files_and_subfolders("./")

    print(COMMANDS_INFO)
    show_files(subfolder_list, files_list)


    commad, args  = input("Input : ").split(" ")
    commad = commad.lower()

    if commad == "open":
        pass
    elif commad == "cd":
        update_screen(args)
    elif commad == "back":
        update_screen("../")
    else:
        raise Exception("command not found")




if __name__ == "__main__":
    args = sys.argv

    if len(args) == 1:
        update_screen("./")
    elif len(args) == 2:
        path = args[1]
        update_screen(path)
