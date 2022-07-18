# Input 1 - 7
# Input 2 - [1, 2, 3, 4, 5, 6, 7]
# Input 3 - 2
# Output - [3, 4, 5, 6, 7, 1, 2]

l = [1, 2, 3, 4, 5, 6, 7]
s = 2
for i in range(s):
    l.append(l[i])
for j in range(s):
    l.remove(l[0])
print(l)