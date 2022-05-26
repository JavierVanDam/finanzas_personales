import glob
import os
from shutil import  rmtree
import re

DIR_BASE = r'c:\Users\jvandam\Documents\finanzas_personales'
patronReArchivosMigraciones = re.compile(r'\d{4}_\w+\.py')
os.chdir(DIR_BASE)

carpetaVenv = 'venv'
carpetaFrontend = 'frontend_3'
listaMigrations = [x for x in glob.glob('**/migrations',recursive=True) if carpetaFrontend not in x and carpetaVenv not in x]


listaBorrar = []
for directorio in listaMigrations:
    for item in os.listdir(directorio):
        if item != '__init__.py':
            listaBorrar.append(f'{DIR_BASE}\{directorio}\{item}')

for item in listaBorrar:
    if item.endswith('__pycache__'):
        rmtree(item)
    elif patronReArchivosMigraciones.match(item.split('\\')[-1]):
        os.remove(item)


os.remove('db.sqlite3')
