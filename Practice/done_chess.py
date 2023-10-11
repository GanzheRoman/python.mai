first_pos_1 = int(input())
first_pos_2 = int(input())
sec_pos_1 = int(input())
sec_pos_2 = int(input())

#rook
if (first_pos_1 != sec_pos_1 and first_pos_2 == sec_pos_2) or (first_pos_1 == sec_pos_1 and first_pos_2 != sec_pos_2):
    print('Ладья может совершить такой ход')
else:
    print('Ладья не может совершить такой ход')

#Bishop
if (sec_pos_1 - first_pos_1) == (sec_pos_2 - first_pos_2) or (abs(sec_pos_1 - first_pos_1)) == abs((sec_pos_2 - first_pos_2)) :
    print('Слон может совершить такой ход')
else:
    print('Слон не может совершить такой ход')

#Knight
if ((abs(first_pos_1 - sec_pos_1)) == 2 and (abs(first_pos_2 - sec_pos_2) == 1)) or ((abs(first_pos_1 - sec_pos_1) == 1) and ((abs(first_pos_2 - sec_pos_2) == 2))):
    print('Конь может совершить такой ход')
else:
    print('Конь не может совершить такой ход')

