birthday = int(input())
birthyear = int(input())
if birthday == 29:
    if (birthyear % 4 == 0 and birthyear % 100 != 0) or birthyear % 400 == 0:
        print("Особо ценный программист")
    else:
        print('мошенник')
else:
    print('обычный программист')