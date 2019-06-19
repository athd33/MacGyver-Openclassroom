import sys
from cx_Freeze import setup, Executable

setup(name="macgyver.py",
      version="0.1",
      description="MacGyver game",
      options = {'build_exe': {'include_files':["./src/"]}}, 
executables=[Executable( "main.py")])
