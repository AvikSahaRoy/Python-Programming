neg=0
z=0
pos=0
a = int(input("Enter terms: "))
for i in range(0,a,1):
    num = int(input("Enter no: "))
    if(num<0):
        neg+=1
    elif(num>0):
        pos+=1
    elif(z==0):
        z+=1
print("Negative ",neg) 
print("Positive ",pos)
print("Zero ",z)