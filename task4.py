# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 вам

from random import randint
from sympy import symbols
from math import prod
 
max_v=100
k = int(input('Введите натуральная степень k: '))
# коэфф. при старшей степени не должен быть равен 0
kfc=[randint(-max_v ,max_v) for i in range(k)]+[randint(1,max_v)]
x = symbols('x')
print (sum(map(prod,zip(kfc,[x**i for i in range(k+1)]))), '= 0')