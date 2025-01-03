import sys
from pathlib import Path
from colorama import Fore

my_path = Path(sys.argv[1])
 
def folder_structure(directory_path, indent=""):                         
    for el in directory_path.iterdir():
        if el.is_dir():
            print(indent + Fore.MAGENTA + f"Directory: {el.name}/")
            folder_structure(el, indent + "    ")
        else:
            print(indent + Fore.GREEN + f"File: {el.name}")

if not my_path.exists() or not my_path.is_dir():
    print(Fore.MAGENTA + "Invalid directory path.")
    sys.exit(1)

folder_structure(my_path)