# Напишите программу, которая принимает на вход число n и выдаёт
# набор произведений чисел от 1 до n в виде списка
# 1-1*1, 2-1*2, 3-1*2*3, 4-1*2*3*4 b и т.д.
# in  3         in  6
# out 1-2-6     out 1-2-6-24-120-720

# def  factorial (number):
#     count  = 1
#     for i in range (1, number  + 1):
#         count  *= i
#     return count

# n = int(input('Enter the number: '))
# print (f'Set of products of numbers from 1 to  {n} = ', end = '')
# for i in range (1, n  +  1):
#     if  i == n: 
#         print(f'{factorial (i)}')
#     else:
#         print(f'{factorial (i)}', end = ', ')