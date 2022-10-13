import math


def requestTwoNubers():
    global firstNumber, secondNumber
    firstNumber = int(input("Введите первое число\n"))
    secondNumber = int(input("Введите второе число\n"))


def requestThreeNumbers():
    global a, b, c
    a = int(input("Введите а\n"))
    b = int(input("Введите b\n"))
    c = int(input("Введите c\n"))


def solveQuadraticEquation():
    if select == 5:
        requestThreeNumbers()
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


def decideOnAction():
    if select == 1:
        print(firstNumber + secondNumber)
    if select == 2:
        print(firstNumber * secondNumber)
    if select == 3:
        print(firstNumber / secondNumber)
    if select == 4:
        print(firstNumber - secondNumber)


while True:
    select = int(input("Выберите:\n1.Сложение\n2.Умножение\n3.Деление\n4.Вычитание\n5.Квадратное уравнение\n"))
    if select <= 4 and select >= 1:
        requestTwoNubers()
        decideOnAction()
    elif select == 5:
        solveQuadraticEquation()
