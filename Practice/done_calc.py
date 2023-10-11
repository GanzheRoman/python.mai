dct = {'ноль':0,'один':1,'два':2,'три':3,'четыре':4,'пять':5,'шесть':6,'семь':7,'восемь':8,'девять':9,'десять':10,
       'одиннадцать':11,'двенадцать':12,'тринадцать':13,'четырнадцать':14,'пятнадцать':15,'шестнадцать':16,
       'семнадцать':17,'восемнадцать':18,'девятнадцать':19,'двадцать':20}

a = input()
b = input()
oper = input()

if oper == 'плюс':
    answer = dct.get(a) + dct.get(b)
    for i in range(len(dct)):
        if list(dct.values())[i] == answer:
            answer = list(dct.keys())[i]
            break
else:
    answer = dct.get(a) - dct.get(b)
    if answer < 0:
        for i in range(len(dct)):
            if list(dct.values())[i] == abs(answer):
                answer = f'минус {list(dct.keys())[i]}'
                break
    else:
        for i in range(len(dct)):
            if list(dct.values())[i] == answer:
                answer = list(dct.keys())[i]
                break

print(answer)
