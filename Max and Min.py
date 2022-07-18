list = [5,100,2,9,3,1,12]
max = list[0]
min = list[0]
for i in range(1,len(list)):
    if list[i] > max:
        max = list[i]
    elif list[i] < min:
        min = list[i]
print(max, min)