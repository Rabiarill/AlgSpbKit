def minOfThree(a,b,c):
    max = a
    if b>max:
        max = b
    if c>max:
        max = c
    return max

def countOfDigit(a):
    count = 0
    while a>0:
        a//=10
        count += 1
    return count

def sumOfDigit(n):
    sum = 0
    while n>0:
        sum += n%10
        n //= 10
    return sum


def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)