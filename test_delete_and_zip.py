import os
import zipfile

def compress_and_move_files(source_folder, destination_folder):
    zip_filename = os.path.join(destination_folder, 'archivos_comprimidos.zip')
    
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

source_folder = r'C:\Users\USER\Desktop\Test_archivos_prueba'  
destination_folder = r'C:\Users\USER\Desktop\Test_zip'  

compress_and_move_files(source_folder, destination_folder)

delete_oldest_file(destination_folder)

