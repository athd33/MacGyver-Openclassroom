"""MacGyver installation file."""

from cx_Freeze import setup, Executable

setup(
    name = "MacGyver Escape Game",
    version = "0.1",
    description = "Installation of the MacGyver game",
    executables = [Executable("main.py")],
)