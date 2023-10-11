first_min = 100000000
sec_min = 100000000
first_max = -1000000000
sec_max = -100000000

while True:
    num = int(input())
    if num == 0:
        break
    else:
        if num > first_max:
            first_max, sec_max = num, first_max
        elif first_max > num and num > sec_max:
            sec_max = num
        if num < first_min:
            first_min, sec_min = num, first_min
        elif first_min < num and num < sec_min:
            sec_min = num
    
print(sec_min, sec_max, sep = '\n')