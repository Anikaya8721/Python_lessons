# Напишите программу, которая принимает на вход вещественное число,
# и показывает сумму его чисел. Без работы с методами строк.
# in 6731      in 0.67        in 198.45
# out 17      out 13         out 27

# number = int(input())
# sum = 0
# while number > 0:
#     sum += number % 10
#     number //= 10
# print(sum)

# n = 198.45
# while n != int(n):
#     n *= 10
# print(n)
# s = 0
# while n > 0:
#     s += n % 10
#     n //= 10
# print(s)

# 2 вариант:
# num = input()
# sum_digits = 0
# power = len(num)-2  # здесь получаем степень
# num = float(num)  # здесь преобразовываем
# num*=int(10**power)  # делаем целочисленным
# while num:
#     sum_digits+=int(num%10)  #отсечение последней цифры
#     num//=10                 #уменьшение на 1 цифру
#     print(int(sum_digits))
# 3 вариант:
# print(sum(map(int, list(input("Введите дробное число: ").replace(".", "")))))