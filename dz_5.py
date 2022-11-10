array = [1, 2, 1000, 9000, 3, 5, 9, 5500]
avg = sum(array) / len(array)
for i in range(len(array)):
    if array[i]>avg:
        print(array[i])