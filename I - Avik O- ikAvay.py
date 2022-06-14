# I - priyanka
# O - iyanka pr ay

n = "Avik"
v = ['a', 'e', 'i', 'o', 'u']
for i in range(len(n)):
    if n[i] in v:
        print(n[i:] + n[:i] + "ay")
        break