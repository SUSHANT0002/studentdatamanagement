import sys

from cx_Freeze import *
includefiles = ['image.ico','base.ico']
excludes = []
packages = []
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

shortcut_table = [
    ("DesktopShortcut", #shortcut
     "DesktopFolder", #directory
     'SMS', #None
     "TARGETDIR", #component
     '[TARGETDIR]\SMS.exe', #target
     None, #argument
     None, #Description
     None, #hotkey
     None, #icon
     None, #icon index
     None, #showcmd
     'TARGETDIR', #wk dir
      )
]

msi_data = {'Shortcut':shortcut_table}

bdist_msi_options = {'data':msi_data}
setup(
    version='0.1',
    description='Student Management System Devloped By Sushant Mahadwad',
    author='Sushant Mahadwad',
    name = 'Student Management System',
    options={'build_exe':{'include_files': includefiles},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
              script='management.py',
              base=base,
              icon='image.ico'
        )
    ]
)