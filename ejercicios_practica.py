#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import sqlite3

# https://extendsclass.com/sqlite-browser.html


def create_schema():
    # Conectarnos a la base de datos
    # En caso de que no exista el archivo se genera
    # como una base de datos vacia
    conn = sqlite3.connect('secundaria.db')

    # Crear el cursor para poder ejecutar las querys
    c = conn.cursor()

    # Ejecutar una query
    c.execute("""
                DROP TABLE IF EXISTS estudiante;
            """)

    # Ejecutar una query
    c.execute("""
            CREATE TABLE estudiante(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [name] TEXT NOT NULL,
                [age] INTEGER NOT NULL,
                [grade] INTEGER,
                [tutor] TEXT
            );
            """)

    # Para salvar los cambios realizados en la DB debemos
    # ejecutar el commit, NO olvidarse de este paso!
    conn.commit()

    # Cerrar la conexión con la base de datos
    conn.close()


def fill(grupo):
    print('Completemos esta tablita!')
    # Llenar la tabla de la secundaria con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto incremental por lo que no deberá completarlo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia INSERT.
    # Observar que hay campos como "grade" y "tutor" que no son obligatorios
    # en el schema creado, puede obivar en algunos casos completar esos campos

    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    c.executemany("""
        INSERT INTO estudiante (name, age, grade, tutor)
        VALUES (?,?,?,?);""", grupo)
    
    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()


def fetch():
    print('Comprobemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # todas las filas con todas sus columnas
    # Utilizar fetchone para imprimir de una fila a la vez

    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    # Leer todas las filas y obtener todos los datos juntos
    c.execute('SELECT * FROM estudiante')
    data = c.fetchall()
    print(data)

    # Leer todas las filas y obtener los datos de a uno
    c.execute('SELECT * FROM estudiante')
    print('Recorrer los datos desde el cursor')
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)

    print('Recorrer los datos directamente de la query')
    for row in c.execute('SELECT * FROM estudiante'):
        print(row)

    # Cerrar la conexión con la base de datos
    conn.close()

def search_by_grade():
    print('Operación búsqueda!')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"

    # De la lista de esos estudiantes el SELECT solo debe traer
    # las siguientes columnas por fila encontrada:
    # id / name / age
    grado = int(input('Ingrese grado: ')) 
    if grado >= 1 and grado <= 6:

        conn = sqlite3.connect('secundaria.db')
        c = conn.cursor()

        for row in c.execute("SELECT id, name, age FROM estudiante WHERE grade=3"):
            print(row)

        conn.commit()
        conn.close()

    else: 
        print('grado incorrecto')
        pass
     

def insert(new):
    print('Nuevos ingresos!')
    # Utilizar la sentencia INSERT para ingresar nuevos estudiantes
    # a la secundaria
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    c.execute("""
        INSERT INTO estudiante (name, age)
        VALUES (?,?);""", new)
    
    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()

def modify(id, name):
    print('Modificando la tabla')
    # Utilizar la sentencia UPDATE para modificar aquella fila (estudiante)
    # cuyo id sea el "id" pasado como parámetro,
    # modificar su nombre por "name" pasado como parámetro

    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    rowcount = c.execute("UPDATE estudiante SET name =? WHERE id =?",
                         (name, id)).rowcount

    # Save
    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    create_schema()   # create and reset database (DB)
    
    i = 0
    grupo = []
    values = []

    while True and i < 10: 
       values = []     
       values.append(input('Ingrese nombre: '))
       values.append(int(input('Ingrese edad: ')))
       grado = int(input('Ingrese grado: '))
       
       if grado >= 1 and grado <= 6:
            values.append(grado)
       else: 
            values.append(0)

       values.append(input('Ingrese nombre de tutor: '))
       grupo.append(values)
    
       if (i > 5):
            fill(grupo)
            grupo = []

       else: 
            print('Debe ingresar al menos 5 estudiantes')
    
       i += 1
     
    fetch()

    search_by_grade()

    new_student = []
    new_student.append(input('Ingrese nuevo estudiante: '))
    new_student.append(int(input('Ingrese edad nuevo estudiante: ')))

    insert(new_student)

    name = input('Ingrese nuevo nombre a modificar: ')
    id = int(input('Ingrese id que modificara: '))
    modify(id, name)
