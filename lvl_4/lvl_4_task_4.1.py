# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cnWyLMGN-pJ4pvHcR6_-x_S9p8KU_wci
"""

import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection
def close_connection(connection):
  if connection:
    connection.close()


connection = get_connection()
cursor = connection.cursor()
sqlquery = """CREATE TABLE Students (
Student_Id INTEGER NOT NULL PRIMARY KEY,
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL
);"""

cursor.execute(sqlquery)
connection.commit()
connection.close()

import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection
def close_connection(connection):
  if connection:
    connection.close()


connection = get_connection()
cursor = connection.cursor()
sqlquery = """INSERT INTO Students (Student_Id, Student_Name, School_Id )
VALUES
('201', 'Иван', 1),
('202', 'Петр', 2),
('203', 'Анастасия', 3),
('204', 'Игорь', 4);
"""


cursor.execute(sqlquery)
connection.commit()
connection.close()

import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection
def close_connection(connection):
  if connection:
    connection.close()

def get_students_name():
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sqlquery = """SELECT Students. Student_Id, Students.Student_Name, Students.School_Id, School.School_Name
    FROM Students
    JOIN School ON Students.School_Id = School.School_Id"""
    cursor.execute(sqlquery)
    record = cursor.fetchall()
    close_connection(connection)
    return record
  except (Exception, sqlite3.Error) as error:
    print("Ошибка в получении данных", error)

get_students_name()