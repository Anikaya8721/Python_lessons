# Задайте список из N чисел, заполненный по формуле (1+1/n)**n
# и выведите на экран их сумму
#  in 6
# out [2.0, 2.25, 2.37, 2.441, 2.488, 2.552]
# 14.071
n = int(input())
list = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f'Последовательность: {list}\n Сумма: {round(sum(list), 3)}')
