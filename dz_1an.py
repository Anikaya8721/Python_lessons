# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет
# n = int(input())
# if 0 < n <= 5: #0< чтоб при указании 0 не было что это будни
#     print('Oh,no! Workday(')
# elif n == 7 or n == 6:
#     print('WOW! Weekend!!')
# else:
#     print('I am not understand u')


# 2. Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

# print('x y w z')
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#            for z in range(2): 
#                 if not(w and z or not y or (not x == (not w))):
#                     print(x, y, w, z)
                    
# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# print('Введите коорданиты: ')
# x = int(input('x= '))
# y = int(input('y= '))
# if x > 0 and y > 0:
#     print('1 четверть')
# elif x < 0 and y > 0:
#     print('2 четверть')
# elif x < 0 and y < 0:
#     print('3 четверть')
# elif x > 0 and y < 0:
#     print('4 четверть')
# else:
#     print('Неверный ввод координат, попробуйте снова')

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*
# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти
# num = int(input('Введите номер четверти: '))
# if num == 1:
#     print('x > 0, y > 0')
# elif num == 2:
#     print('x < 0, y > 0')
# elif num == 3:
#     print('x < 0, y < 0')
# elif num == 4:
#     print('x > 0, y < 0')
# else:
#     print('Ошибка, попробуйте снова')



# . Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1 
# out 5.099

# print('Введите координаты: ')
# X1 = int(input())
# X2 = int(input())
# Y1 = int(input())
# Y2 = int(input())
# print(f'{((X2-X1)**2+(Y2-Y1)**2)**0.5:0.4}')