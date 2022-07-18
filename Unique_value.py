# Given two integer arrays nums1 and nums2, return an array of their intersection. Each 
# element in the result must be unique and you may return the result in any order.

# nums1 = [1,2,2,1]
# nums2 = [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

l = []
for i in range(len(nums1)):
    if nums1[i] in nums2:
        if nums1[i] not in l:
            l.append(nums1[i]) 
print(l)