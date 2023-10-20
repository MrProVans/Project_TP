from functions_of_project import *
from random import choice

print('Выберите место из предложенного списка, куда вы опоздали:')
s = [f'{i+1}.{location[i]}\n' for i in range(len(location))]
print(*s)

num = input('Введите: ')
while not(num.isdigit()) or not(1 <= int(num) <= 15):
    num = input('Введите корректное значение: ')

rand = choice(excuse)

print('Отмазка: \n')
print(f'Я не пришел {scloneniya[int(num) - 1]}, потому что {rand}')