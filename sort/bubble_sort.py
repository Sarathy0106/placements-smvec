# BUBBLE SORT  
# LOGIC :  
# Compare adjacent elements and swap them if they are in the wrong order.Largest element will be at the end .

arr = [50,20,40,10]
for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)