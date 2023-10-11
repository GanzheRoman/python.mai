a = int(input())
b = int(input())
mult = a*b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print(f'НОД введенных чисел: {a + b}')
lcm = int(mult/(a+b))
print(f'НОК введенных чисел: {lcm}')