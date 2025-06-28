import os  # Módulo para interactuar con el sistema de archivos
import shutil  # Módulo para mover archivos

# Ruta principal donde están los archivos a organizar
RUTA_BASE = 'ejemplo'  # Puede ser una ruta absoluta o relativa

# Diccionario que relaciona categorías con extensiones de archivo
CATEGORIAS = {
    'imagenes': ['.jpg', '.jpeg', '.png', '.gif'],
    'documentos': ['.pdf', '.docx', '.txt'],
    'videos': ['.mp4', '.mov', '.avi']
}

# Función que crea las subcarpetas si no existen
def crear_subcarpetas():
    for categoria in CATEGORIAS:
        ruta = os.path.join(RUTA_BASE, categoria)
        os.makedirs(ruta, exist_ok=True)  # Crea carpeta sin fallar si ya existe

# Función que recorre todos los archivos y los mueve a su categoría correspondiente
def organizar_archivos():
    for archivo in os.listdir(RUTA_BASE):  # Recorre cada archivo en la carpeta base
        ruta_archivo = os.path.join(RUTA_BASE, archivo) # Une la carpeta base con el nombre del archivo para obtener la ruta completa

        if os.path.isfile(ruta_archivo):  # Ignora carpetas, solo procesa archivos
            _, extension = os.path.splitext(archivo)  # Extrae la extensión (por ejemplo .jpg)

            for categoria, extensiones in CATEGORIAS.items():
                if extension.lower() in extensiones:
                    destino = os.path.join(RUTA_BASE, categoria, archivo)
                    shutil.move(ruta_archivo, destino)  # Mueve el archivo a su carpeta
                    print(f"Movido: {archivo} → {categoria}")
                    break  # Salta al siguiente archivo tras moverlo

# Punto de entrada principal del script
if __name__ == "__main__":
    crear_subcarpetas()
    organizar_archivos()
