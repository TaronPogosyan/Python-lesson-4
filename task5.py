# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов. 
# 2*x² + 4*x + 5 3*x² +10*x + 6 Вывод: 5*x² + 14*x + 11 

with open('pol_01.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('pol_02.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('pol_01.txt','r') as file:
    pol_01 = file.readline()
    list_pol_01 = pol_01.split()


with open('pol_02.txt','r') as file:
    pol_02 = file.readline()
    list_pol_02 = pol_02.split()

print(f'{list_pol_01} + {list_pol_02}')
sum_poly = list_pol_01 + list_pol_02

with open('sum_pol.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_pol_01} + {list_pol_02}')