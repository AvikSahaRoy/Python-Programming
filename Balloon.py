def balloon(str):
    print(str[0], end='')
    for i in range(1,len(str)):
        if ( str[i-1] == str[i] ):
            print('*', end='')
        else:
            print(str[i], end='')
str = input("Enter a String: ")
obj = balloon(str)