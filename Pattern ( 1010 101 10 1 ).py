# Print 
# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1 
row = int(input("Enter the number of rows: "))  
for i in range (row):
    for j in range (1,i+1):
        if((i+j)%2 == 0):
            print("1", end=' ')
        else:
            print('0',end=' ')
    print()