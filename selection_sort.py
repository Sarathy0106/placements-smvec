# SELECTION SORT  
# LOGIC :  
# Find the minimum element in the remaining unsorted array and swap it with the correct  position.

arr = [50,20,40,10]
for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print(arr)
 