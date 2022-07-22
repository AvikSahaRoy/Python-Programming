# Fibonaci using recursion ---------------
# 0 1 1 2 3 5 8
a = 0
b = 1
sum = 0
count = 1
def fibo(n):
    global a,b,sum,count
    if count <= n:
        count += 1
        a = b
        b = sum
        sum = a + b
        fibo(n)
    return sum
n = int(input('Enter a position : '))
print('%dth position value is: '%n,fibo(n))






