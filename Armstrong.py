# class Armstrong:
#     n = int(input("Enter a number: "))
#     n1 = n
#     n2 = n
#     c = 0
#     while(n1 != 0):
#         d = n1%10
#         n1 = n1//10
#         c += 1
#     cc = c
#     sum = 0
#     for i in range(cc):
#         d = n2%10
#         n2 = n2//10
#         p = d**cc
#         sum = sum + p
#     if sum == n:
#         print('True')
#     else:
#         print('False')

# ----------------------------------

# Using Class -
class ArmStrong:
    def __init__(self,n):
        self.n1=n
        self.count=0
    def getLength(self,n):
        while self.n1!=0:
            self.n1=self.n1//10
            self.count+=1
        self.n1=n
        return self.count
    def checkArm(self,n,count):
        final=0
        while self.n1!=0:
            rem=self.n1%10
            temp=rem**count
            final=final+temp
            self.n1=self.n1//10
        if final==n:
            return True
        else:
            return False
n=int(input("Enter Any Number: "))
obj=ArmStrong(n)
c=obj.getLength(n)
print(obj.checkArm(n,c))

