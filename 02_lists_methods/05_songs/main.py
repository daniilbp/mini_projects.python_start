violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

N = int(input('Сколько песен выбрать? '))
my_playlist = []
time_songs = 0

for nm_song in range(1, N + 1):
    print('Название', nm_song, '- й песни:', end = ' ')
    song = input()
    my_playlist.append(song)

for i_song in my_playlist:
    for i_part in violator_songs:
        if i_song in i_part:
            time_songs += i_part[1]

print('\nОбщее время звучания песен:', round(time_songs, 2), 'минуты')
