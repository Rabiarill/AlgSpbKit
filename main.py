from random import randint

sumOfPositive = 0
sumOfNegative = 0
for i in range(50):
    a = randint(-1_000_000, 1_000_000)
    if a > 0:
        sumOfPositive += a
    else:
        sumOfNegative += a
print(f"Сумма позитивных чисел = {sumOfPositive}\n Сумма негативных чисел = {sumOfNegative}")
