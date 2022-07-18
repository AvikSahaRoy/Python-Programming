nums = [4,4,4,4,4,4,4,2,2,1,1,1,1,1,2,2,3,3,3,3,3,3]
l = []
c = 0
l1 = []
l2 = []
for i in range(len(nums)):
    if nums[i] not in l:
        l.append(nums[i])
print(l)

for i in range(len(l)):
    for j in range(len(nums)):
        if l[i] == nums[j]:
            c += 1
    l1.append(c)
    c = 0
print(l1)

m = max(l1)
i = l1.index(m)
print(l[i])
