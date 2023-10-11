password = input()

status = True
while status:
    if len(password) < 10:
        status = False
    if status == False:
        print("Вы ввели недопустимый пароль")
        break
    if not password.islower() and not password.isupper():
        pass
    else:
        status = False
    if status == False:
        print("Вы ввели недопустимый пароль")
        break
    var = 0
    for i in password:
        if i.isdigit():
            var +=1
            break
        else:
            continue
    if var == 0:
        status = False
    if status == False:
        print("Вы ввели недопустимый пароль")
        break
    var = 0
    for i in password:
        if ord(i) in range(65,91) or ord(i) in range(97,123):
            var +=1
            break
        else:
            continue
    if var == 0:
        status = False
    if status == False:
        print("Вы ввели недопустимый пароль")
        break
    if " " in password:
        status = False
    if status == False:
        print("Вы ввели недопустимый пароль")
        break
    count = 0
    for i in password:
        if count > 1:
            status = False
        else:
            count = 0
            for j in password:
                if i == j:
                    count +=1
    print('Вы ввели допустимый пароль')
    break
    
    
    
