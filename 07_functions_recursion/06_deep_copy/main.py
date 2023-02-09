import copy

def do_site(num, dct=dict()):
    if len(dct) == num:
        return 1

    name_prod = input('Введите название продукта для нового сайта: ')

    site = {
        'html': {
            'head': {
                'title': 'Куплю/продам {0} недорого'.format(name_prod)
            },
            'body': {
                'h2': 'У нас самая низкая цена на {0}'.format(name_prod),
                'div': 'Купить',
                'p': 'Продать'
            }
        }
    }

    dct[name_prod] = copy.deepcopy(site)

    for key, value in dct.items():
        print(f'Сайт для {key}:\nsite = {value}\n')

    do_site(num)

numbers_sites = int(input('Сколько сайтов: '))

do_site(numbers_sites)
