m, n = map(int,input().split(' '))
matrix = []

for i in range(m):
    a = list(input().split())[:n]
    matrix.append(a)
print(*matrix, sep = '\n')
