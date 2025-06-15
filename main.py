import sqlite3      
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'custumers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Cria tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Verifica se a tabela está vazia
cursor.execute(f'SELECT COUNT(*) FROM {TABLE_NAME}')
count = cursor.fetchone()[0]

# Insere dados só se estiver vazia
if count == 0:
    columns = (
        f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (:name, :weight)'
    )
    cursor.execute(columns, {'name': 'Matheus', 'weight': 82})
    cursor.executemany(columns, (
        {'name': 'Henrique', 'weight': 78},
        {'name': 'Pri', 'weight': 62},
        {'name': 'Antonio', 'weight': 65},
        {'name': 'Patricia', 'weight': 49},
    ))
    connection.commit()

cursor.close()
connection.close()
