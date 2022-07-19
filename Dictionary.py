n = 'institute'
v = ['a', 'e', 'i', 'o', 'u']
dict = {}
for i in n:
    if i in v:
        keys = dict.keys()
        if i in keys:
            dict[i]+= 1
        else:
            dict[i] = 1
print(dict)