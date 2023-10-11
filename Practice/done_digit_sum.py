def compute_digits_sum(num):
    if num == 0:
        return 0
    else:
        return num % 10 + compute_digits_sum(num//10)

print(compute_digits_sum(11235))