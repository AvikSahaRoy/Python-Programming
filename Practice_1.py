n = "my name is avik"
# l = []
# for i in range(len(n)):
#     # if n[i] == " ":
#     #     n = n[i+1].upper()
#     l.append(n[i])
#     if l[i] == " ":
#         l = l[i].upper()
# print(l)



for i in range(len(n)):
    if n[i] == " ":
        # n = n[i+1].upper()
        n = n.replace(n[i+1], n[i+1].upper())
        # print(n[i+1])
print(n)



# n = "my name is avik"
# n = n[1].upper()
# print(n)
