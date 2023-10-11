def is_power(num, d = 2):
    try:
        if num == 1:
            return True
        else:
            return is_power(num/d,d)
    except RecursionError:
        return False
print(is_power(650,25))
