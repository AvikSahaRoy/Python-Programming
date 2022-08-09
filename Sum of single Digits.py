# Input  - l = [1,2,10,1111]  sum = 1124
# Output - 8
l = [1,2,10,1111]
s = 0
sum = 0
for i in range(len(l)):
    s = s + l[i]
print(s)

while(s > 0 or sum > 9):
    if(s == 0):
        s = sum
        sum = 0
     
    sum += s % 10
    s /= 10

print(int(sum))
    
