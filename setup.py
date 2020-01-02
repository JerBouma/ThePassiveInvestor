from cx_Freeze import setup, Executable
import requests
import os
import sys

os.environ['REQUESTS_CA_BUNDLE'] = os.path.join(os.getcwd(), "cacert.pem")

build_exe_options = {"excludes": ['sqlite3'],
                     "packages": ["os", "numpy"], "includes": ["numpy"],
                     'include_files' : [(requests.certs.where(), 'cacert.pem')]}
                         
setup(
    name="ThePassiveInvestor", 
    version="0.1", 
    description="Passive Investing for the Average Joe",
    options = {"build_exe": build_exe_options},
    executables=[Executable(script  = "program.py",
                            icon    = "Images/icon ICO.ico",
                            base    = ("Win32GUI" if sys.platform == "win32" else None))])