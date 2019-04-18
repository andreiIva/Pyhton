print('Задание №3')
print('Решение квадратного уравнения ax² + bx + c = 0')
import math
b = int(input('Введите числовой коэффициент b:'))
a = int(input('Введите числовой коэффициент a:'))
c = int(input('Введите числовой коэффициент c:'))
D = (b ** 2) - 4 * a * c

print(D)
if D < 0:
    print('Корней нет!')
elif D == 0:
    x = (-b + math.sqrt(D))/(2*a)
    print(x)
elif D > 0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print(x1, x2)


print('Задание №2')


a = int(input("Введите значение переменной а = "))
b = int(input("Введите значение переменной b = "))
a = a + b
b = a - b
a = a - b
print("Мы поменяли значения переменных, теперь a = ", a, ", b = ", b)

print('Задание №1')


number = int(input('Введите число :'))
max_digit = 0

while number != 0:
    digit = number % 10
    if max_digit < digit:
        max_digit = digit
    number //= 10

print('Максимальная цифра числа',  ':',max_digit)