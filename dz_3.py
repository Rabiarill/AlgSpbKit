array = [1,2,12,3,11,4,5,6,7,8,9]
k = int(input("Введите число элементов: "))
def findMax(array, k):
    for i in range(k):
        temp = max(array)
        array.remove(temp)
        print(temp)

