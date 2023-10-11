def computer_trace(mass) -> float:
    i = 0
    j = 0
    trace = 0
    for elem in mass:
        trace += mass[i][j]
        i += 1
        j += 1
    print(trace)

computer_trace([[1, 3.2, 12], [3, -7.1, 15],[1,1,100]])

