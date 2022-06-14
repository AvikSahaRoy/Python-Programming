# class Student:
#     def __init__(self, name, roll, marks):
#         self.name = name
#         self.roll = roll
#         self.marks = marks
#     def Showdata(self):
#         print("Student name: ",self.name)
#         print("Roll: ", self.roll)

#     def Showmarks(self):
#         print("Marks: ", self.marks)

# n = input("Enter the Student name: ")
# r = int(input("Enter the Student Roll no: "))
# m = int(input("Enter the Student Marks: "))
# obj = Student(n, r, m)
# obj.Showdata()
# obj.Showmarks()



# n = input("Enter the brackets: ")
# b = ['(', ')', '[', ']', '{', '}']
# l = []
# for i in range(len(n)):
#     if n[i] in b:
#         l.append(n[i])
    # if n[i] == '(' and n[i+1] == ')':
    #     print('true')

    # # else:
    # #     print('false')

    # elif n[i] == '[' and n[i+1] == ']':
    #     print('true')
    # # else:
    # #     print('false')

    # elif n[i] == '{' and n[i+1] == '}':
    #     print('true')
                
    # else:
    #     print('false')


# class Solution:
#     def __init__(self):
#         self.s = input("Enter your bracket: ")
#     def isValid(self):
#         # b = ['(', ')', '[', ']', '{', '}']
#         b = ['(', '[', '{']
#         l = []
#         for i in range(len(self.s)):
#             if self.s[i] in b:
#                 l.append(self.s[i])
#                 if '(' in l and ')' in self.s:
#                     l.remove('(')
#                 if '[' in l and ']' in self.s:
#                     l.remove('[')
#                 if '{' in l and '}' in self.s:
#                     l.remove('{')
#         print(l)
#         if len(l) == 0:
#             return True
#         else:
#             return False
    
        
# obj = Solution()
# print(obj.isValid())


class Solution:
    def __init__(self):
        pass
    def isValid(self, s):

        b = ['(', '[', '{']
        b1 = [')', ']', '}']
        l = []
        l1 = []
        for i in range(len(s)):
            if s[i] in b:
                l.append(s[i])
            else:
                if s[i] in b1:
                    l1.append(s[i])

        # print(l)
        # print(l1)

            if '(' in l and ')' in l1:
                l.remove('(')
                l1.remove(')')
            if '[' in l and ']' in l1:
                l.remove('[')
                l1.remove(']')
            if '{' in l and '}' in l1:
                l.remove('{')
                l1.remove('}')

        if len(l) == 0 and len(l1) == 0:
            print("true")
        else:
            print("false")
    
obj = Solution()
s = input("Enter your bracket: ")
flag = 0

for i in s:
    if i not in ['(', '[', '{', ')', ']', '}']:
        flag = 1
if len(s)>=1 and len(s)<=1000 and flag==0:
    obj.isValid(s)
else:
    print("Invalid")
