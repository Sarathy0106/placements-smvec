#1,2,3
arr = []
size = int(input())
found = False
for i in range(size):
    value = int(input())
    arr.append(value)

target = int(input())

for i in range(len(arr)):
    if target == arr[i]:
        print("Number found at index",i)
        break
    if not found:
        print("Number does not exist")

#4
arr = []
size = int(input())
count = 0

for i in range(size):
    value = int(input())
    arr.append(value)

key = int(input())
for i in range(len(arr)):
    if arr[i] == key:
        count+=1

print(count)

#5
arr = []
size = int(input())

for i in range(size):
    value = int(input())
    arr.append(value)

key = int(input())
for i in range(len(arr)):
    if arr[i]==key:
        print(i)
        break

#6
arr = []
size = int(input())

for i in range(size):
    value = int(input())
    arr.append(value)

key = int(input())
for i in range(len(arr)):
    if arr[i]==key:
        print(i)
        break


#7
arr = []
size = int(input())
max = 0

for i in range(size):
    value = int(input())
    arr.append(value)

for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
print(max)
            #### OR #####
print(max(arr))



#8
arr = []
size = int(input())
min = float('inf')
for i in range(size):
    value = int(input())
    arr.append(value)
for i in range(len(arr)):
    if arr[i] < min:
        min = arr[i]
print(min)
            ##### OR #####
print(min(arr))

#9
arr = []
even = []
size = int(input())
for i in range(size):
    value = int(input())
    arr.append(value)
for i in range(len(arr)):
    if arr[i]%2 == 0:
        even.append(arr[i])
print("The found even number are",even)    

#10   
arr = []
size = int(input())
for i in range(size):
    value = int(input())
    arr.append(value)
print(arr.index(max(arr)))