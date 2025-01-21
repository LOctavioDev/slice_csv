mysqlimport --local -u root -p --fields-terminated-by=',' --lines-terminated-by='\n' nba play_by_play.csv

Get-Content play_by_play.csv | Select-Object -Skip 1 | Select-Object -First 1000000 | Set-Content play_by_play_limited.csv



# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual (en Windows)
.\venv\Scripts\activate

# Instalar las dependencias
pip install -r requirements.txt
