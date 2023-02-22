import sqlite3

import os # импортируем модуль для проверки (добавляем функционал ОС )
# создаем соединение с файлом 

def execute_sql_file(file_name):
    if os.path.isfile(file_name):  # проверяем существует ли текущий путь 
        read= open(file_name, "r") 
        cursor= connection.cursor() # поставили курсор 
        cursor.executescript(read.read()) # читаем файл со скриптом и выполняем скрипт 
        cursor.close()
        read.close()
    else:
        raise FileExistsError(f"файл {file_name} не найден")

connection  = sqlite3.connect("blog.db" , check_same_thread=False) #check_same_thread - параметр для игнорирования определения текущего треда 


# quaring = "INSERT INTO users ( name ,login, display_name , password , bithday) 
# VALUES('помидоры',2,'кг','2021-03-22')" #-- products-  таблица созданная в SQL,
#далее записываем все ключи которые будут использоваться внутри скобок () , VALUES( указываем данные для импорта в таблицу)
#cursor.execute(quaring) # выполняется запуск переменной (quaring)

# read_q = "SELECT * FROM products" 
# data = cursor.execute(read_q)
# connection.commit()
# print(data.fetchall())

def query(q, assoc=False):
    cursor = connection.cursor()
    data = cursor.execute(q)
    result_rows = data.fetchall()
    if result_rows and assoc:  # something like 'fetch_assoc'
        result = []
        for row in result_rows:
            assoc_row = {}
            for c in range(len(row)):
                assoc_row[cursor.description[c][0]] = row[c]
            result.append(assoc_row)
        return result
    connection.commit()
    return result_rows

def insert(q):
    cursor = connection.cursor()
    data = cursor.execute(q)
    id = cursor.lastrowid
    connection.commit()
    return id


# update_q = "UPDATE products ,quan = quan + 10 WHERE id= 2" #WHERE - условие для поиска
# cursor.execute(update_q)
# connection.commit()

# read_q = "SELECT * FROM products" # после SELECT надо перечислить поля которые хотим указать 
# data = cursor.execute(read_q)
# connection.commit()
# print(data.fetchall()) # распаковывает результат запроса в список


