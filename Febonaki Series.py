def main():
    n = int(input("Enter a number: "))
    a = 0
    b = 1
    sum = 0
    count = 1
    while(count <= n):
        print(sum, end = " ")
        count += 1
        a = b
        b = sum
        sum = a + b
if __name__ == '__main__':
    main()