arr = [10.80,30,90,30]
pivot = arr[0]
left = []
right = []
for i in range(1, len(arr)):
    if arr[i] < pivot:
        left.append(arr[i])
    else:
        right.append(arr[i])
sorted_arr = left + [pivot] + right
print(sorted_arr)