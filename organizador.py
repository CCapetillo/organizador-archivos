import os  # Módulo estándar para interactuar con el sistema de archivos (crear carpetas, leer rutas, etc.)
import shutil  # Módulo para copiar y mover archivos entre carpetas
from datetime import datetime  # Permite trabajar con fechas y horas para registrar eventos en el log


# Ruta base donde se encuentran los archivos a organizar
RUTA_BASE = 'ejemplo'  # Es una ruta relativa; puede cambiarse por absoluta si se desea

# Diccionario que asocia categorías (carpetas destino) con listas de extensiones válidas
CATEGORIAS = {
    'imagenes': ['.jpg', '.jpeg', '.png', '.gif'],
    'documentos': ['.pdf', '.docx', '.txt'],
    'videos': ['.mp4', '.mov', '.avi']
}


# Ruta al archivo de log dentro de la carpeta base
LOG_FILE = os.path.join(RUTA_BASE, 'log.txt')  # Aquí se registrarán todas las acciones realizadas


# Crea las subcarpetas de categorías y una adicional llamada 'otros', necesarias para organizar los archivos.
def crear_subcarpetas():
    for categoria in CATEGORIAS:
        ruta = os.path.join(RUTA_BASE, categoria)  # Crea la carpeta para cada categoría si no existe
        os.makedirs(ruta, exist_ok=True)
    os.makedirs(os.path.join(RUTA_BASE, 'otros'), exist_ok=True)  # Crea la carpeta especial para archivos que no encajan en ninguna categoría conocida


# Escribe un mensaje en el archivo log.txt con la fecha y hora actual. Sirve para mantener un registro de todas las acciones ejecutadas.
def escribir_log(mensaje):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Formato legible de hora
    with open(LOG_FILE, 'a', encoding='utf-8') as f:  # Modo 'a' para agregar al final sin borrar lo anterior
        f.write(f"[{timestamp}] {mensaje}\n")  # Se escribe el mensaje con marca de tiempo


# Recorre todos los archivos en la carpeta base, detecta su extensión, los clasifica y los mueve a su subcarpeta correspondiente. Si no encuentra coincidencia, los mueve a 'otros/' y todo queda registrado en log.txt.
def organizar_archivos():
    for archivo in os.listdir(RUTA_BASE):  # Lista el contenido de la carpeta base
        ruta_archivo = os.path.join(RUTA_BASE, archivo)  # Crea ruta completa al archivo

        # Verifica que sea un archivo (no una carpeta) y que no sea el archivo log
        if os.path.isfile(ruta_archivo) and archivo != 'log.txt':
            _, extension = os.path.splitext(archivo)  # Extrae la extensión, ejemplo: '.jpg'
            extension = extension.lower()  # Convierte a minúscula para evitar errores con mayúsculas
            encontrado = False  # Bandera que indica si se encontró una categoría para el archivo

            for categoria, extensiones in CATEGORIAS.items():
                if extension in extensiones:
                    destino = os.path.join(RUTA_BASE, categoria, archivo)  # Ruta destino según categoría
                    shutil.move(ruta_archivo, destino)  # Mueve el archivo
                    escribir_log(f"Movido: {archivo} → {categoria}")  # Registra acción en el log
                    print(f"Movido: {archivo} → {categoria}")  # Muestra en consola
                    encontrado = True
                    break  # Termina la búsqueda de categorías para ese archivo

            if not encontrado:
                # Si no coincide con ninguna categoría, se mueve a 'otros'
                destino = os.path.join(RUTA_BASE, 'otros', archivo)
                shutil.move(ruta_archivo, destino)
                escribir_log(f"Movido: {archivo} → otros (sin categoría)")
                print(f"Movido: {archivo} → otros")


# Punto de entrada principal: si el script se ejecuta directamente (no importado desde otro archivo)
if __name__ == "__main__":
    crear_subcarpetas()  # Prepara todas las carpetas necesarias
    organizar_archivos()  # Ejecuta el proceso de clasificación y registro
