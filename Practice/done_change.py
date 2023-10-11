num = int(input())
even = (num // 100000 % 10 * 100) + (num // 1000 % 10 * 10) + (num // 10 % 10)
odd = (num % 10 * 100) + (num % 1000 // 100 * 10) + (num % 100000 // 10000)
print(f'{odd:3}#{even:03}#{even*odd}')