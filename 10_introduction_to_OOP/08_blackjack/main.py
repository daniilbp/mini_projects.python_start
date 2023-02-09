import random


class Players:
    def __init__(self, count):
        self.deck = Deck()
        self.players = [Player(input(f'Введите имя игрока №{index} (для компьтера введите: PC): '), self.deck) for index in range(1, count+1)]

    def all_info(self):
        print(f'\nКарт в колоде: {len(self.deck.deck)}')
        for player in self.players:
            player.info()


class Player:
    def __init__(self, name, deck):
        self.name = name
        self.cards = [Card(deck) for _ in range(2)]
        self.check_ace()

    def info(self):
        print(f'На руке у {self.name}:', [card.card for card in self.cards])
        print(f'Сумма карт на руке:', sum([card.rank for card in self.cards]))

    def take_card(self, deck):
        self.cards.append(Card(deck))
        self.check_ace()

    def check_ace(self):
        sum_ranks = 0
        for card in self.cards:
            if not isinstance(card.rank, list):
                sum_ranks += card.rank
            else:
                if sum_ranks <= 10:
                    card.card[2] = 11
                    card.rank = 11
                else:
                    card.card[2] = 1
                    card.rank = 1


class Deck:
    def __init__(self):
        suits = {'Пик', 'Черви', 'Крести', 'Буби'}
        ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'В': 10, 'Д': 10, 'К': 10, 'Т': [1, 11]}
        self.deck = [[rank, suit, value] for suit in suits for rank, value in ranks.items()]


    def do_card(self):
        new_card = random.choice(self.deck)
        self.deck.remove(new_card)

        return new_card


class Card:
    def __init__(self, deck):
        self.card = deck.do_card()
        self.suit = self.card[0] + self.card[1]
        self.rank = self.card[2]


def check_choice(choice):
    while True:
        try:
            if choice not in [0, 1]:
                raise ValueError
            return choice
        except ValueError:
            print('Введено некорректное значение. Введите 1 или 0!')
            choice = int(input('Выберите 1 (Взять карту) или 0 (Остановиться): '))

def choice(player, deck):
    if player.name != 'PC':
        choice = int(input('Выберите 1 (Взять карту) или 0 (Остановиться): '))
        choice = check_choice(choice)
    else:
        if sum([card.rank for card in player.cards]) <= 11:
            choice = 1
        else:
            choice = random.randint(0, 1)

    if choice == 0:
        print(f'Игрок {player.name} закончил игру.')
        return False

    if choice == 1:
        print(f'Игрок {player.name} берет карту.')
        player.take_card(deck)
        return True

def check_res(player):
    if sum([card.rank for card in player.cards]) > 21:
        return False
    return True

def the_game(num):
    my_game = Players(num)
    my_game.all_info()

    for player in my_game.players:
        while True:
            action = choice(player, my_game.deck)
            my_game.all_info()

            if not check_res(player):
                print(f'Игрок {player.name} "сгорел"')
                break

            if not action:
                break

        if not check_res(player):
            break
    else:
        ranks = [sum([card.rank for card in player.cards]) for player in my_game.players ]
        max_rank = max(ranks)
        index_max_rank = ranks.index(max_rank)
        winner = my_game.players[index_max_rank].name
        print(f'\nПобедил {winner}!!!')


the_game(2)
