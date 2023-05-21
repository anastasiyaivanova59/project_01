# -*- coding: utf-8 -*-
"""lvl_2_task_2.1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19GluD-OR97VUVCMpR8E876KTNLYUbe0k
"""

#Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.


# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

list = [[4, 6, 2, 1, 9, 63, -134, 566], [-52, 56, 30, 29, -54, 0, -110], [42, 54, 65, 87, 0], [5]]


def minimum(arr):
  n = len(arr)
  for i in range(n-1):
    for j in range (n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr[0]
  
     
def maximum(arr):
  n = len(arr)
  for i in range(n-1):
    for j in range (n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr[-1]

for i in list:
  minimum(i)
  maximum(i)
  print(f"max = {maximum(i)}, min = {minimum(i)}")

def maximum(arr):
  max_div = arr[0]
  for i in arr:
    if i > max_div:
      max_div = i
  return max_div

def minimum(arr):
  min_div = arr[0]
  for i in arr:
    if i < min_div:
      min_div = i
  return min_div

for index_list in list:
  print(f"max = {maximum(index_list)}, min = {minimum(index_list)}")