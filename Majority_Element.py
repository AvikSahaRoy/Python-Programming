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

# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def majorityElement(self, A):
#         l = []
#         l1 =[]
#         c = 0
#         for i in range(len(A)):
#             if A[i] not in l:
#                 l.append(A[i])
#         for i in range(len(l)):
#             for j in range(len(A)):
#                 if l[i] == A[j]:
#                     c += 1
#             l1.append(c)
#             c = 0
#         print(l1)
                    
        

# obj = Solution()
# i = [2, 1, 2]
# k = obj.majorityElement(i)
# print(k)



# for i in range(len(l)):
#     for j in range(len(nums)):
#         if l[i] == nums[j]:
#             c += 1
#     print(l[i],"-->>", c)
#     l1.append(l[i])
#     l1.append(c)
#     c = 0
#     l2.append(l1)
#     l1 =[]
# print(l2)

# l3 = []
# for i in range(len(l2)):
#     l3.append(l2[i][1])
# m = max(l3)
# for i in range(len(l2)):
#     if m == l2[i][1]:
#         print(l2[i][0])
