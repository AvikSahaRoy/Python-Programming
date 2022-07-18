# Find the factorial of 5 
def fact():
    g=1
    f = int(input("Enter the number: "))
    for i in range(1,f+1,1):
        g = g*i
    print("Factorial of {} is {}".format(f,g))
    return g
fact()