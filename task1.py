# Вычислить число c заданной точностью d. 
# Пример:
# при d = 0.001,π = 3.141           


d = 20000000

pi = 4 * (sum(1/x for x in range(1, d + 1, 4)) +
            sum(-1/x for x in range(3, d + 1, 4)))

print(format(pi, '.100'))