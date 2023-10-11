num = int(input())
first = num // 100000
sec = num // 10000 % 10
third = num // 1000 % 10
rever = (third * 100) + (sec * 10) + first
var = num % 1000
print(int(var == rever))
