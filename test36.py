n = input()
max = 0
for i in range(len(n)):  
    if int(n[i]) > max:
        max = int(n[i])
print(max)