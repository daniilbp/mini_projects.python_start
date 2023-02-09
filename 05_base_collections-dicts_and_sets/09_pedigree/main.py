N = int(input('Введите количество человек: '))
pair_dict = {}

for num in range(1, N):
    pair = input('{0}-я пара: '.format(num)).split()

    if pair[1] in pair_dict:
        pair_dict[pair[0]] = pair_dict[pair[1]] + 1

    else:
        pair_dict[pair[1]] = 0
        pair_dict[pair[0]] = pair_dict[pair[1]] + 1

print('\n«Высота» каждого члена семьи:')
for family_member in sorted(pair_dict.keys()):
    print(family_member, pair_dict[family_member])