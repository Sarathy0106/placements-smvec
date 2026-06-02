def linear():
    arr = []
    size = int(input())
    target = int(input())

    for i in range(size):
        value = int(input())
    for i in range(len(arr)):
        if target==arr[i]:
            return i

index = linear()
print(index)