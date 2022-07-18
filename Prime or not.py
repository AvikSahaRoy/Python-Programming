def main():
    count = 0
    n = int(input("Enter a number: "))
    for i in range(2,n):
        if(n%i == 0):
            count+= 1
            print("Not Prime")
            break
    if(count == 0):
        print("Prime")
if __name__ == '__main__':
    main()