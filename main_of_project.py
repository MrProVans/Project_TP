from functions_of_project import *
from random import randint
print('Выберите место из предложенного списка, куда вы опоздали:')
s = [f'{i+1}.{location[i]}\n' for i in range(len(location))]
print(*s)
num = int(input('Вводите: ')) -1
rand = randint(1,len(excuse))
print()
print('Отмазка: \n')
print(f'Я не пришел {scloneniya[num]}, потому что {excuse[rand]}')