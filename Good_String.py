s = "leEeetcode"
# s = "abBAcC"
# s = "popPpulaBbr"
# s = "s"
l = []
for i in range(len(s)):
    if s[i] == s[i].upper() and s[i].lower() in l:
        l.pop()
    elif s[i] == s[i].lower() and s[i].upper() in l:
        l.pop()
    else:
        l.append(s[i])
print(l)