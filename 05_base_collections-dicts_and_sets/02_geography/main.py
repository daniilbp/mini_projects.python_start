country_num = int(input('Количество стран: '))
total_cities_dict = {}

for num in range(country_num):
    print(num + 1, 'страна:', end = ' ')
    country = input('').split()

    cities_dict = {country[i_city]: country[0] for i_city in range(1, len(country))}
    total_cities_dict.update(cities_dict)

for num_city in range(len(cities_dict)):
    print()
    print(num_city + 1, '- й город:', end = ' ')
    city = input('')
    if total_cities_dict.get(city):
        print('Город', city, 'расположен в стране', total_cities_dict.get(city) + '.')
    else:
        print('По городу', city, 'данных нет.')
