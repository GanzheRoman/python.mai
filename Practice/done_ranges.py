beg_1 = int(input())
end_1 = int(input())
beg_2 = int(input())
end_2 = int(input())

if (end_1 - beg_2) > 0:
    if (end_1 - end_2) <= 0:
        print(f"Длина пересечения отрезков {end_1 - beg_2}")
    else:
        print(f"Длина пересечения отрезков {end_2 - beg_2}")
elif (end_1 - beg_2) == 0:
    print(f'Отрезки пересекаются в точке {end_1}')
else:
    print('Отрезки не пересекаются')