a = int(input("Первая сторона равна: "))
b = int(input("Вторая сторона равна: "))
c = int(input("Третья сторона равна: "))
ab = a + b
ac = a + c
bc = b + c
if ab > c and ac > b and bc > a:
  print("Треугольник может существовать")
else:
  print("Треугольник не может существовать")