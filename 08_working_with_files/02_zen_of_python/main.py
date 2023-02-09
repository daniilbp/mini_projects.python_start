def turn_around():
    with open('zen.txt', 'r') as file_from:
        lst_file_from = file_from.read().split('\n')

        for el in lst_file_from[::-1]:
            print(el)

turn_around()
