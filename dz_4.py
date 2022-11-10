array = [1,2,12,3,11,4,5,6,7,8,9]
k = int(input("Введите число элементов: "))
def findMin(array, k):
    for i in range(k):
        temp = min(array)
        array.remove(temp)
        print(temp)