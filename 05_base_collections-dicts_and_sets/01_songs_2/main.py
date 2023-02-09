violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

num_list = ['первой', 'второй', 'третьей', 'четвертой', 'пятой', 'шестой', 'седьмой', 'восьмой', 'девятой']

nums = int(input('Сколько песен выбрать? '))
total_time = 0

for i_nums in range(nums):
    print('Название', num_list[i_nums], 'песни:', end = ' ')
    song = input('')
    total_time += violator_songs.get(song, 0)

print('\nОбщее время звучания песен:', round(total_time, 2))
