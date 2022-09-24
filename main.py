import math

select = int(input("Выберите:\n1.Сложение\n2.Умножение\n3.Деление\n4.Вычитание\n5.Квадратное уравнение\n"))
while select > 5 or select < 1:
    select = int(input())

if select <= 4 and select >= 1:
    firstNumber = int(input("Введите первое число\n"))
    secondNumber = int(input("Введите второе число\n"))
    if select == 1:
        print(firstNumber + secondNumber)
    if select == 2:
        print(firstNumber * secondNumber)
    if select == 3:
        print(firstNumber / secondNumber)
    if select == 4:
        print(firstNumber - secondNumber)
    if select == 5:
        a = int(input("Введите а\n"))
        b = int(input("Введите b\n"))
        c = int(input("Введите c\n"))
        D = b ** 2 - 4 * a * c
        if D > 0:
            ans_1 = (-b + math.sqrt(D)) / (2 * a)
            ans_2 = (-b - math.sqrt(D)) / (2 * a)
            print(f"Первый корень  = {ans_1}\nВторой корень = {ans_2}")
        if D == 0:
            ans = (-b) / 2 * a
            print(f"Единственный корень = {ans}")
        if D < 0:
            print("Корней нет")

