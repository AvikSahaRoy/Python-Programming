e = 0
o = 0
a = int(input("Enter terms: "))
for i in range(0,a,1):
    n = int(input("Enter no: "))
    if(n%2 == 0):
        e+=1
    elif(n%2 != 0):
        o+=1
print("Even: ",e)
print("Odd: ",o)