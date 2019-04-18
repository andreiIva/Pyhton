print('Задание № 3')
password = 18
age = int(input("Введите Ваш возраст: "))
if age == password:
    print('Доступ разрешен')
else:
    print('Извинте, пользование данным ресурсом только с 18 лет')

print('Задание № 2')
a = input()
b = input()
#a, b = b, a

c = a
a = b
b = c
print(a, b)
print(b, a)

print('Задание №1')
number = int(input())
while number != 0:
    digit = number % 10
    print(digit)
    number = number // 10




    
    
