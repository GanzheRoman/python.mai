txt = input()
txt += " "
word = ''
dct = {}
count = 1
unique = 0
for i in txt:
    if i != ' ':
        word += i
    else:
        if word in dct:
            dct[word] += 1
            word = ''
        else:
            dct[word] = 1
            word = ''
            unique +=1
print(f'В вашем тексте {unique} различных слов')
for i in range(len(dct)):
    print(f'Слово {list(dct.keys())[i]} встретилось в вашем тексте {list(dct.values())[i]} раз')