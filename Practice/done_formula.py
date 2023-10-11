x = float(input())
y = float(input())
z = float(input())

res = (x ** 2) * (y ** (1/2) + z ** (1/2)) * (1 / (((x**6)+(y ** (1/2)))**(1/2))) - ((3 * x) ** (1/2)) + (z ** 11)
print(f'{res:0.3f}')