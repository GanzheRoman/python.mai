num = int(input())
base = int(input())
var = '0123456789ABCDEF'
res = ''

while num > 0:
    mod_num = num % base
    res = var[mod_num] + res
    num //= base 
print(res)