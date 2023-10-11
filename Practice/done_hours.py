minute = int(input())
hours = minute // 60 % 24 
minutes = minute % 60 
print(f'{hours:02}:{minutes:02}')