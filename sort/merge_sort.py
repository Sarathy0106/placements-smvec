# MERGE SORT  
# LOGIC :  
# Divide the array into two halves, sort them separately, and then merge them.

arr = [38,27,43,3]
left = [27,38]
right = [3,43]
result = []
i = j = 0
while i < len(left) and j < len(right):
    if left[i] < right[j]:
        result.append(left[i])
        i += 1
    else:
        result.append(right[j])
        j += 1
print(result)