# Lista de Tareas

Una aplicación simple para gestionar y organizar tareas.

## Requisitos

Antes de comenzar, es necesario tener instalado lo siguiente: 
- **Python 3.10 o superior** ---> [Ver guia de instalación] (https://elpythonista.com/como-instalar-python)
- **Pip** ----> [Ver guia de instalación] (https://recursospython.com/guias-y-manuales/instalacion-y-utilizacion-de-pip-en-windows-linux-y-os-x/) 
- **Git** ----> [Ver guia de instalación] (https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git)

## Instalación

Sigue estos pasos para instalar la aplicación en tu máquina local:

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/LorenBregant/tp2_lista_de_tareas.git
   cd tp2_lista_de_tareas/

2. **Crea y activa un entorno virtual (opcional, pero recomendado)**:
    
- **En Windows**:
  ```
   python -m venv env
   env\Scripts\activate
  ```
- **En macOS/Linux**:
  ```
   python3 -m venv env
   source env/bin/activate
   ```
    
3. **Instala las dependencias desde el archivo requirements.txt**:
    ```
   pip install -r requirements.txt
    ```
4. **Genera la interfaz gráfica**:
    ```
   pyside6-uic src/interfaz/tareas.ui -o src/interfaz/ui_tareas.py
    ```

## Uso

Una vez que la instalación esté completa, puedes ejecutar la aplicación con el siguiente comando:
    ```
    python src/main.py
    ```