"""Setup file to create a exe"""

import os
from cx_Freeze import setup, Executable



# call setup  and add files / folder
setup(
    name = "MacGyver escape game",
    version = "1.00",
    options= {"build_exe": {"packages": ["pygame"],
                            "include_files": ["sounds", "images", "constants.py", "fonctions.py", "items.py","player.py","mapp.txt","mapp.py","player.py"]}},		
    description = "Projet 03 Labyrinth Game",
    executables = [Executable("main.py")],
)
