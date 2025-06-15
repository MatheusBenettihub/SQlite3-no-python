import sqlite3
from main import DB_FILE, TABLE_NAME

connection= sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#DELETE - cuidado,sempre usar WHERE
cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE ID = "136"'
)

#UPDATE - também sempre usar WHERE
cursor.execute(f'UPDATE {TABLE_NAME} SET name = ? WHERE id = ?', ('Patrick', 140) #exemplo de segurança contra SQL INJECTION
)
cursor.execute(f'UPDATE {TABLE_NAME} SET weight = 80 WHERE id = 140') #sem segurança
connection.commit()

#Counsultas READ
cursor.execute(f'SELECT * FROM {TABLE_NAME} ORDER BY name DESC LIMIT 5 '
)
print(cursor.fetchall())


cursor.close()
connection.close()
