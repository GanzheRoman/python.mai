sample = input()
user_txt = input()

sample += ' '
user_txt += ' '

word = ''
same = 0
sample_mass = []
user_txt_mass = []
for i in sample:
    if i == ' ':
        sample_mass.append(word)
        word = ''
    else:
        word += i

for i in user_txt:
    if i == ' ':
        user_txt_mass.append(word)
        word = ''
    else:
        word += i

for i in set(user_txt_mass):
    if i in set(sample_mass):
        same += 1

unique = f'{int(((len(set(user_txt_mass)) - same)/ len(set(user_txt_mass))) * 100)}%'
print(same, unique, sep = '\n')