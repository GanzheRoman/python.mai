a = int(input())
b = int(input())
c = int(input())

if a+b>c and a+c>b and b+c>a:
    if a > b > c:
        if a**2 > (b**2 + c**2):
            print('треугольник тупоугольный')
        elif a**2 == (b**2 + c**2):
            print('треугольник прямоугольный')
        else:
            print('треугольник остроугольный')
    elif b > a > c:
        if b**2 > (a**2 + c**2):
            print('треугольник тупоугольный')
        elif b**2 == (a**2 + c**2):
            print('треугольник прямоугольный')
        else:
            print('треугольник остроугольный')
    else:
        if c**2 > (b**2 + a**2):
            print('треугольник тупоугольный')
        elif c**2 == (b**2 + a**2):
            print('треугольник прямоугольный')
        else:
            print('треугольник остроугольный')
else:
    print('треугольника с такими сторонами не существует')