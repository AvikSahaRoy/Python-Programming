def reverse(str):
    if str == '':
        return str
    else:
        return str[-1] + reverse(str[:-1])
str = 'Avik Saha'
print(reverse(str))