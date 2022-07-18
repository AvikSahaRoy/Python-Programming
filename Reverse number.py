# Reverse number 1234 to 4321 :- 
rev = 0
rem = 0
n = int(input("Enter no: "))
while(n>0):
    rem = n % 10  
    rev = (rev * 10) + rem    
    n = n // 10 
print("Reverse Number is: ",rev)