# Proyecto de Procesamiento de Archivos CSV

Este proyecto tiene como objetivo procesar archivos CSV, hacer particiones y luego importarlos a una base de datos MySQL.

## Pasos para usar el proyecto

### 1. Preparar el entorno virtual

Primero, necesitamos crear y activar el entorno virtual para gestionar las dependencias del proyecto.

1. **Crear el entorno virtual:**

    ```
    python -m venv venv
    ```

2. **Activar el entorno virtual:**

    - En Windows:

      ```
      .\venv\Scripts\activate
      ```

### 2. Instalar las dependencias

Una vez activado el entorno virtual, instala las dependencias necesarias usando `requirements.txt`:

```
pip install -r requirements.txt
```

### 3. Procesar el archivo CSV
Para procesar el archivo CSV y limitar la cantidad de datos que se van a cargar en la base de datos, utiliza PowerShell:
# Ya lo hace python !
```
Get-Content play_by_play.csv | Select-Object -Skip 1 | Select-Object -First 1000000 | Set-Content play_by_play_limited.csv

```

#### Este comando hace lo siguiente:

- Lee el archivo play_by_play.csv.
- Omite la primera fila (encabezado).
- Selecciona las primeras 1,000,000 filas.
- Guarda las filas seleccionadas en un nuevo archivo llamado play_by_play_limited.csv.

### 4. Importar el archivo procesado a MySQL
Después de generar el archivo limitado (play_by_play_limited.csv), debes importar los datos a la base de datos. Para hacerlo, navega hasta la carpeta donde se encuentra el archivo y ejecuta el siguiente comando MySQL:

```
mysqlimport --local -u root -p --fields-terminated-by=',' --lines-terminated-by='\n' nba play_by_play_limited.csv

```

Este comando Importa el archivo CSV a la base de datos nba.
El archivo CSV debe estar en el mismo directorio donde ejecutas el comando, con el nombre play_by_play_limited.csv.
Nota: Si el archivo CSV tiene un nombre diferente, asegúrate de ajustar el comando para que coincida con el nombre de archivo correcto.

## Estructura del Proyecto

```
slice_csv/
│
├── venv/               # Entorno virtual
├── csvs/               # Archivos CSV
├── templates/          # Archivos HTML y JS para la interfaz web
├── main.py             # Código Python
├── requirements.txt    # Dependencias del proyecto
└── .gitignore          # Archivos y carpetas a ignorar en Git

```

### Arrancar el servidor web:

```
uvicorn main:app --reload --port 8000

```
