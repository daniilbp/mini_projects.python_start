def counter():
    count_sum = 0
    with open('numbers.txt', 'r') as file_from, open('answer.txt', 'w') as file_in:
        text_in_file = file_from.read()
        for sym in text_in_file:
            if sym != ' ' and sym != '\n':
                count_sum += int(sym)

        file_in.write(str(count_sum))

counter()
