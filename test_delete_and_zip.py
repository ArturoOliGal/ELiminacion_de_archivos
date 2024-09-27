import os
import zipfile
import shutil
import datetime as dt

hoy_mes = dt.date.today().month
print(hoy_mes)
hoy_dia = dt.date.today().day
print(hoy_dia)
quincena=0
if hoy_dia<16:
    quincena=1
else:
    quincena=2
def compress_and_move_files(source_folder, destination_folder):
    nombre_archivo=f"respaldo_{hoy_mes}_{quincena}.zip"
    zip_filename = os.path.join(destination_folder, nombre_archivo)
    
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, source_folder))
    
    print(f'Archivos comprimidos en {zip_filename}')
    
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)  
            print(f'Archivo {file} eliminado de la carpeta de origen.')

    print('Todos los archivos originales han sido eliminados de la carpeta de origen.')


def delete_oldest_file(folder):
    files = [os.path.join(folder, file) for file in os.listdir(folder) if os.path.isfile(os.path.join(folder, file))]
    
    if not files:
        print("No hay archivos para eliminar.")
        return

    oldest_file = min(files, key=os.path.getctime)
    os.remove(oldest_file)
    print(f'El archivo más antiguo {oldest_file} ha sido eliminado.')

source_folder = r'C:\Users\MERCA\Desktop\test_archivos'  
destination_folder = r'C:\Users\MERCA\Desktop\Test_zip'  

compress_and_move_files(source_folder, destination_folder)

delete_oldest_file(destination_folder)

