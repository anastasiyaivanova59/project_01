# -*- coding: utf-8 -*-
"""lvl_2_task_2.2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13fT6IId0pdQYXpjNGz1JscI-htw4X-5W
"""

list_month = {
          1: "месяц 1 (январь)",
          2: "месяц 2 (февраль)",
          3: "месяц 3 (март)",
          4: "месяц 4 (апрель)",
          5: "месяц 5 (май)",
          6: "месяц 6 (июнь)",
          7: "месяц 7 (июль)",
          8: "месяц 8 (август)",
          9: "месяц 9 (сентябрь)",
          10: "месяц 10 (октябрь)",
          11: "месяц 11 (ноябрь)",
          12: "месяц 12 (декабрь)"}
              
x = int(input("Введи номер месяца:"))
def quarter_of(month):
  if x in range(1, 4):
    y = ("первого квартала")
  elif x in range(4, 7):
    y = ("второго квартала")
  elif x in range(7, 10):
    y = ("третьего квартала")
  elif x in range(10, 13):
    y = ("четвертого квартала")
  else:
    y = ("такого месяца нет")
  print(f"{list_month[x]} является частью {y}")
  
quarter_of(x)