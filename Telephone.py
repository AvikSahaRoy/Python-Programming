n = input("Enter your number: ")
a = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

new = []
new2 = []

for i in range(len(n)):
    if n[i] == "2":
        new.append(a[0])
    if n[i] == "3":
        new.append(a[1])
    if n[i] == "4":
        new.append(a[2])
    if n[i] == "5":
        new.append(a[3])
    if n[i] == "6":
        new.append(a[4])
    if n[i] == "7":
        new.append(a[5])
    if n[i] == "8":
        new.append(a[6])
    if n[i] == "9":
        new.append(a[7])

if len(n) == 1:
    print(new[0])
else:
    for i in range(len(new[0])):
        for j in range(len(new[1])):
            new2.append(new[0][i]+new[1][j])
    print(new2) 
