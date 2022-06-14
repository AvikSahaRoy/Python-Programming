 # A = [22, 38, 45, 50, 59, 75]
# B = [10, 15, 20, 28,  30, 35, 40, 48]
# C = []
# i = 0
# j = 0
# while (i<len(A) and j<len(B)):
#     if A[i] <= B[j]:
#         C.append(A[i])
#         i += 1
#     else:
#         C.append(B[j])
#         j += 1
# while(i<len(A)):
#     C.append(A[i])
#     i += 1
# while(j<len(B)):
#     C.append(B[j])
#     j += 1
# print("First list is:  ",A)
# print("Second list is: ",B)
# print("Marge list is:  ",C)

# ------------------------------------------

# A = [22, 38, 45, 50, 59, 75, 10, 15, 20, 28, 30, 35]
# C = []
# mid = (0+len(A))//2
# # print(mid)
# i = 0
# j = mid
# while (i<=mid and j<len(A)):
#     if A[i] <= A[j]:
#         C.append(A[i])
#         i += 1
#     else:
#         C.append(A[j])
#         j += 1
# while(i<mid):
#     C.append(A[i])
#     i += 1
# while(j<len(A)):
#     C.append(A[j])
#     j += 1
# print("First list is:  ",A)
# print("Marge list is:  ",C)

# ------------------------------------------

def Merge(A, l, m, h):
    C = []      # new list
    i = l       # first index
    j = m + 1   # mid point
    while (i<=m and j<=h):
        if A[i] <= A[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(A[j])
            j += 1
    while(i<=m):
        C.append(A[i])
        i += 1
    while(j<=h):
        C.append(A[j])
        j += 1

    i = l 
    k = 0 
    while i<=h:
        A[i]=C[k]
        i+=1
        k+=1 

def Merge_Sort(L, l, h):
    if l < h:
        mid = (l+h)//2
        Merge_Sort(L, l, mid)
        Merge_Sort(L, mid+1, h)
        Merge(L, l, mid, h)
        
L = [10, 8, 30, 60, 50, 4]
print("Original Array: ", L)
# L = [22, 38, 45, 50, 59, 75, 10, 15, 20, 28, 30, 35]
l = 0
h = len(L) - 1
Merge_Sort(L, l, h)
print("Sorted array:   ",L)

