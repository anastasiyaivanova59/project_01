#Пункт А
import random
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

k = 3
y = [] #список из 3 песен

while k != 0:
  x = random.choice(my_favorite_songs) #выбираем из заданного списка 3 рандомных песни
  k -= 1
  y.append(x)

print("3 случайных песни", y)

z = [y[0][1], y[1][1], y[2][1]] #список из длительности 3-х песен
print("список из длительности 3-х песен", z)

#total = 0
#for i in my_favorite_songs:
  #total += i[1]
#print("список из длительности 3-х песен", total)

total = round(sum(z), 2)
print("сумма времени:", total)

total = str(total)
total_list = total.split(".")
print("Список из минут и секунд: ", total_list)
min = total_list[0]
sec = total_list[1]
print("Длительность: ", min, " минут ", sec, "секунд")

all_sec = int(min) * 60 + int(sec)
print("Общая длительность в секундах: ", all_sec)

total_min = all_sec // 60
total_sec = all_sec % 60

print(f"Три песни звучат {total_min}.{total_sec} минут")

#Пункт D
import datetime
time = datetime.time(0, int(total_list[0]), int(total_list[1]))
print(time)
new_time = time.strftime('%M:%S')
print(new_time)

#Пункт B
import random
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

k = 3
y = [] #список из 3 песен

while k != 0:
  x = random.choice(list(my_favorite_songs_dict.values())) #выбираем из заданного списка 3 рандомных песни
  k -= 1
  y.append(x)

print("время 3-х случайных песен", y)

total = round(sum(y), 2)
print("сумма времени:", total)

total = str(total)
total_list = total.split(".")
print("Список из минут и секунд: ", total_list)
min = total_list[0]
sec = total_list[1]
print("Длительность: ", min, " минут ", sec, "секунд")

all_sec = int(min) * 60 + int(sec)
print("Общая длительность в секундах: ", all_sec)

total_min = all_sec // 60
total_sec = all_sec % 60

print(f"Три песни звучат {total_min}.{total_sec} минут")
