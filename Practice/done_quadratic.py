def solve_quadratic_equation(a,b,c):
    dis = b**2 - (4 * a * c)
    sqrt_dis = dis ** (1/2)
    if dis > 0:
        print((2,tuple(sorted(((-b + (sqrt_dis))/(2*a),(-b - sqrt_dis)/(2*a))))))
    elif dis == 0:
        return (1,(int((-b)/(2*a))))
    else:
        return (0,())

solve_quadratic_equation(1,0,-4)