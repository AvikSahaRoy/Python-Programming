# Dictionary : ---------------------
d1 = {
    4: 'Avipsa',
    3: 'Soumo',
    1: 'Tanu',
    2: 'Asmita',
    5: 'Gopal',
    0: 'Avik'
}
print("Print Keys: ",d1.keys()) # dict_keys([4, 3, 1, 2, 5, 0])
print("Print Values: ",d1.values()) # dict_values(['Avipsa', 'Soumo', 'Tanu', 'Asmita', 'Gopal', 'Avik'])
print("Print Sorted Order: ",sorted(d1)) # [0, 1, 2, 3, 4, 5]
for i in sorted(d1):
    print(i,':',d1[i])


