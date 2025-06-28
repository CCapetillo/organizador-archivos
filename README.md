# 📁 Organizador de Archivos por Tipo

Este proyecto es un script en Python que automatiza la organización de archivos dentro de una carpeta base. Clasifica los archivos por su extensión y los mueve a subcarpetas como `imagenes`, `documentos`, `videos` o `otros`, manteniendo un registro detallado de cada acción en un archivo `log.txt`.

---

## 🔧 Características principales

- ✅ Clasifica archivos por tipo (extensión) en subcarpetas automáticas
- 🗃️ Mueve archivos no reconocidos a una carpeta `otros/`
- 📝 Crea un archivo de registro `log.txt` con todas las acciones realizadas
- 💻 Compatible con cualquier sistema operativo que ejecute Python 3

---

## 🚀 ¿Para qué sirve?

Este script es útil cuando necesitas ordenar carpetas con archivos mixtos (descargas, recursos compartidos, etc.) de forma automática. También sirve como proyecto introductorio para practicar automatización de tareas con Python y manipulación de archivos.

---

## 🛠️ Requisitos

- Python 3.x instalado
- Sistema operativo con acceso a terminal (Windows, macOS o Linux)

---

## ▶️ Cómo usarlo

1. Clona este repositorio o descarga el archivo `organizador.py`:

    ```bash
    git clone https://github.com/tuusuario/organizador-archivos.git
    ```

2. Coloca los archivos que deseas organizar en una carpeta llamada `ejemplo/` (puedes cambiar el nombre editando la variable `RUTA_BASE` en el script).

3. Ejecuta el script:

    ```bash
    python organizador.py
    ```

4. El script clasificará los archivos en subcarpetas y generará un archivo `log.txt` con el detalle de los movimientos.

---

## 📁 Estructura del proyecto (después de ejecutarlo)

organizador_archivos/
├── organizador.py
├── README.md
└── ejemplo/
    ├── archivo1.jpg
    ├── archivo2.pdf
    ├── otros/            ← (creada automáticamente)
    ├── imagenes/         ← (creada automáticamente)
    ├── documentos/       ← (creada automáticamente)
    ├── log.txt           ← (generado automáticamente)


---

## 📜 Ejemplo de salida en `log.txt`

[2025-06-28 01:52:13] Movido: archivo1.jpg → imagenes
[2025-06-28 01:52:13] Movido: archivo2.pdf → documentos
[2025-06-28 01:52:13] Movido: archivo3.mp3 → otros (sin categoría)

---

## ✨ Posibles mejoras futuras

- Soporte para más extensiones y tipos de archivo
- Añadir interfaz de línea de comandos (`argparse`)
- Registro de errores en un archivo separado
- Integración con scripts en Bash o ejecución programada (`crontab`)

---

## 🧑‍💻 Autor

Este proyecto fue desarrollado como parte de mi formación técnica en automatización y DevOps.

**Christopher Capetillo**

---

## 📄 Licencia

Este proyecto es de uso libre para fines educativos o personales.
