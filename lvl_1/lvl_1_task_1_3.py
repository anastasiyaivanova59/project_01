# -*- coding: utf-8 -*-
"""lvl_1 task 1.3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WyBjFdNp1RezYxqFagVGA-wU3hXwJypd
"""

mouth_dict = {
    1: "Вы ввели январь, 31 день", 
    2: "Вы ввели февраль, 28 дней", 
    3: "Вы ввели март, 31 день", 
    4: "Вы ввели апрель, 30 дней", 
    5: "Вы ввели май, 31 день", 
    6: "Вы ввели июнь, 30 дней", 
    7: "Вы ввели июль, 31 день", 
    8: "Вы ввели август, 31 день", 
    9: "Вы ввели сентябрь, 30 дней", 
    10: "Вы ввели октябрь, 31 день", 
    11: "Вы ввели ноябрь, 30 дней", 
    12: "Вы ввели декабрь, 31 день"
    }

try:
  key = input("Введи номер месяца:")
  print(mouth_dict[int(key)])
except KeyError:
  print("Такого месяца нет")