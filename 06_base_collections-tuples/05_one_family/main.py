families = {
    1: {
        ('Сидоров', 'Никита'): 35,
        ('Сидорова', 'Алина'): 34,
        ('Сидоров', 'Павел'): 10
    },
    2: {
        ('Федоров', 'Михаил'): 55,
        ('Федоров', 'Дмитрий'): 34,
        ('Федорова', 'Светлана'): 52
    },
    3: {
        ('Афиногенов', 'Григорий'): 26,
        ('Афиногенова', 'Людмила'): 26,
        ('Афиногенов', 'Святозар'): 5
    }
}

family_name = input('Введите фамилию: ')
print()

for num_family, names in families.items():
    for key in names:
        if (len(family_name) <= len(key[0]) and key[0].startswith(family_name)) or \
                (len(family_name) > len(key[0]) and key[0].startswith(family_name[:len(family_name) - 1])):
            print(key[0], key[1], names[key])
