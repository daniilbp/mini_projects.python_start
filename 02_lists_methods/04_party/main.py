def party(guests):
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    action = input('Гость пришёл или ушёл? ')

    while action != 'Пора спать':

        name_guests = input('Имя гостя: ')

        if action == 'пришёл':
            if len(guests) < 6:
                print('Привет,', name_guests + '!')
                guests.append(name_guests)
                party(guests)
            else:
                print('Прости,', name_guests + ', но мест нет.')
                party(guests)
        if action == 'ушёл':
            print('Пока,', name_guests + '!')
            guests.remove(name_guests)
            party(guests)

    print('\nВечеринка закончилась, все легли спать.')

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

party(guests)
