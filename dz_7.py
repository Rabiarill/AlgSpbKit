array = [1, 2, 3, 4, 5, 6, 7]
arrayChet = []
arrayNeChet = []

for i in range(len(array)):
    if array[i] % 2 == 0:
        arrayChet.append(array[i])
    else:
        arrayNeChet.append(array[i])
print(arrayChet)
print(arrayNeChet)
