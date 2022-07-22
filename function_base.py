import sqlite3 as sql

# создание базы и таблиц
def create_table():
    connection = sql.connect('VKinder.db')
    with connection:
        cur = connection.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS `info_User` ('idserial' PRIMARY KEY,'city' TEXT,'status' TEXT,'age' TEXT)")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS `searching_results`"
            " ('idserial' PRIMARY KEY, 'link' TEXT,'foto1' TEXT,'foto2' TEXT,'foto3' TEXT)")

        cur.close()

# Заполнение таблицы "Информация о пользователе"
def zapolnenie_table1(id, city, relation, bdate):
    connection = sql.connect('VKinder.db')
    with connection:
        cur = connection.cursor()
        cur.execute(f"INSERT INTO 'info_User' VALUES ('{id}','{city}','{relation}','{bdate}')")
        connection.commit()
        cur.close()

# Заполнение таблицы "Результаты поиска"
def zapolnenie_table2(id_users, link, foto1, foto2, foto3):
    connection = sql.connect('VKinder.db')
    with connection:
        cur = connection.cursor()
        cur.execute(
            f"INSERT INTO 'searching_results' VALUES ('{id_users}','{link}','{foto1}','{foto2}','{foto3}')")
    connection.commit()
    cur.close()

# удаление информации из таблицы "Информация о пользователе"
def delete_table1():
    connection = sql.connect('VKinder.db')
    with connection:
        cur = connection.cursor()
        cur.execute(f"DELETE FROM 'info_User'")
        connection.commit()
        cur.close()

# удаление информации из таблицы "Результаты поиска"
def delete_table2():
    connection = sql.connect('VKinder.db')
    with connection:
        cur = connection.cursor()
        cur.execute(f"DELETE FROM 'searching_results'")
        connection.commit()
        cur.close()