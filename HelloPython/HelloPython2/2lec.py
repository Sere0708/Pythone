# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# 1.  6782 -> 23
# 2.  0,56 -> 11



# num = int(input("Введите целое: "))
# sum = 0
# while (num != 0):
    # sum = sum + num % 10
    # num = num // 10
# print("Сумма цифр числа равна: ", sum)





# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. Факториал
# 5! = 120


# n = int(input())
 
# factorial = 1
# while n > 1:
    # factorial *= n
    # n -= 1
 
# print(factorial)



# 3. Задана последовательность натуральных чисел, завершающаяся числом 0. Требуется определить значение второго по величине элемента в этой последовательности, то есть элемента, который будет наибольшим, если из последовательности удалить наибольший элемент.
# Пример:
# 1
# 7
# 9
# 0
# Вывод:
# 7


# max1 = max2 = 0
# a = int(input())
# while a != 0:
    # if max1 < a:
        # max1, max2 = a, max1
    # a = int(input())
# print (max2)




