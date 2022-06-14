# n = input('Enter your name: ')
# for i in range(5):
#     print(n[i], end="")

# --------------------------------------

# n = 'institute'
# v = ['a', 'e', 'i', 'o', 'u']
# dict = {}
# for i in n:
#     if i in v:
#         keys = dict.keys()
#         if i in keys:
#             dict[i]+= 1
#         else:
#             dict[i] = 1
# print(dict)

# -------------------------------------------

# n = int(input('Enter a number: '))
# sum = 0
# for i in range(n+1):
#     sum = sum + i
# print(sum)

# ------------------------------------------

# l = [34, 89, 54, 20, 50, 76, 10, 45, 90]
# l.sort()
# print(l[2])

number=[34, 89, 54, 20, 50, 76, 10, 45, 90]
for i in range(len(number)):
  for j in range(i+1, len(number)):
    if number[i] > number[j]:
      number[i], number[j] = number[j], number[i]
print("Third smallest number is: ", number[2])

# l = [34, 89, 54, 20, 50, 76, 10, 45, 90]
# MAX = 100000
# t = MAX
# for i in range(len(l)):
#     if l[i] < t:
#         t = l[i]
# print(t)

# -----------------------------------------------

# def balloon(str):
#     if len(str) > 1:
#         print(str[0], end='')
#         for i in range(len(str)-1):
#             if ( str[i] in str[i+1] ):
#                 print('*', end='')
#             else:
#                 print(str[i+1], end='')
#     else:
#         print('empty string')
# str = input("Enter a String: ")
# obj = balloon(str)

# ---------------------------------------------------

# def balloon(str):
#     print(str[0], end='')
#     for i in range(1,len(str)):
#         if ( str[i-1] == str[i] ):
#             print('*', end='')
#         else:
#             print(str[i], end='')
# str = input("Enter a String: ")
# obj = balloon(str)

# -----------------------------------------------

# n = '10100011111000'
# c = 0
# l = []
# for i in range(1,len(n)):
#     if ( n[i-1] == n[i] and n[i] == '0'):
#         c += 1
#     else:
#         l.append(c)
#         c = 0
# print(max(l)+1)