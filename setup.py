import sys
from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Directions.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages': ['webbrowser', 'pyperclip'],
    },    
}

setup(
    name = "Directions",
    options = options,
    version = "1.0.0",
    description = 'Opens Google Maps based on you clipboard or entries.',
    executables = [Executable("Directions.py", base=base)]
)