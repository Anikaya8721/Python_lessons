# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# def power(a, b):
#     if (b == 1):
#         return (a)
#         if (b != 1):
#             return (a * power(a, b - 1))
# a = int(input("Введите число: "))
# b = int(input("Введите его степень: "))
# print("Результат возведения в степень равен:", power(a, b) p)

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# 2 2
# 4

# def summ(a, b):
#     if a == 0:
#         return b
#     return summ(a-1, b+1)
# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# print("summ = ", a + b)