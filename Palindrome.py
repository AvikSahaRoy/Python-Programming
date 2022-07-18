# Check String is Palindrome or Not Palindrome --------->>>

a = 'madam'
if a == a[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# ------------------------------------------------------

s = "avik"
str = ""
for i in s:
    str = i + str
print(str)

# ---------------------------------------------
# Check Number is Palindrome or Not Palindrome --------->>>

n = 1221
temp = n
rev = 0
while(n>0):
    mod = n%10
    rev = rev * 10 + mod
    n = n//10
print(rev)
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")    
