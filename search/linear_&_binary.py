#1
arr = []
size = int(input())

for i in range(size):
    value = int(input())
    arr.append(value)

key = int(input())

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        found = True
        break
    elif key < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

if found:
    print("Card Valid")
else:
    print("Card Invalid")

#2
arr = []
size = int(input())
for i in range(size):
    value = int(input())
    arr.append(value)

key = int(input())
found = False

for i in range(len(arr)):
    if arr[i] == key:
        found = True
        break

if found:
    print("Login Successful")
else:
    print("Login Failed")
    
#3
arr = []
size = int(input())

for i in range(size):
    value = int(input())
    arr.append(value)

key = int(input())

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        found = True
        break
    elif key < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

if found:
    print("Student Registered")
else:
    print("Student Not Registered")


#4
arr = []
size = int(input())

for i in range(size):
    value = int(input())
    arr.append(value)

key = int(input())
found = False

for i in range(len(arr)):
    if arr[i] == key:
        found = True
        break

if found:
    print("Passenger Found")
else:
    print("Passenger Not Found")

#5
arr = []
size = int(input())

for i in range(size):
    value = int(input())
    arr.append(value)

key = int(input())

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        found = True
        break
    elif key < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

if found:
    print("Product Available")
else:
    print("Product Not Available")

#6
arr = []
size = int(input())

for i in range(size):
    value = int(input())
    arr.append(value)

key = int(input())

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        found = True
        break
    elif key < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

if found:
    print("Patient Record Found")
else:
    print("Patient Record Not Found")

#7
arr = []
size = int(input())

for i in range(size):
    value = int(input())
    arr.append(value)

key = int(input())
found = False

for i in range(len(arr)):
    if arr[i] == key:
        found = True
        break

if found:
    print("Player Selected")
else:
    print("Player Not Selected")

#8
arr = []
size = int(input())

for i in range(size):
    value = int(input())
    arr.append(value)

key = int(input())

low = 0
high = len(arr) - 1
pos = -1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        pos = mid
        break
    elif key < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

if pos != -1:
    print("Asset Found at Position", pos)
else:
    print("Asset Not Found")
