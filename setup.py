import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "shutil", "pathlib", "fnmatch"], "includes": ["tkinter", "watchdog.observers", "watchdog.events", "datetime"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Organizador Download",
    version="0.1",
    description="Organiza a pasta download",
    options={"build_exe": build_exe_options},
    executables=[Executable("Organizador_Download.py", base=base)]
)