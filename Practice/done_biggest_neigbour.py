mass = input().split(' ')

for i in range(len(mass)):
    mass[i] = int(mass[i])

count = 0
for i in range(1, len(mass)-1):
    if mass[i] > mass[i+1] and mass[i] > mass[i-1]:
        count+=1
print(count)