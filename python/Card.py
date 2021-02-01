import random, time

suit_list = ["Heart", "Spade", "Diamond", "Clubs"]
point_list = ["-1", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
player_list = []

class Card:
    global suit_list, point_list

    def __init__(self, suit, point):
        self.suit, self.point = suit, point
    
    def check_suit(self): return suit_list[self.suit]

    def check_point(self): return point_list[self.point]

    def __str__(self): return self.check_suit() + ' ' + self.check_point()

class Deck:
    def __init__(self, num):
        self.card_list = []
        for i in range(num): self.card_list += self.generate_deck()

    def generate_deck(self):
        result = []
        for s in range(4):
            for p in range(1, 14):
                new_card = Card(s, p)
                result.append(new_card)
        return result
    
    def __len__(self): return len(self.card_list)

    def __str__(self): return str([str(c) for c in self.card_list])

    def deal(self): return self.card_list.pop(random.randint(0, len(self) - 1))

    def shuffle(self):
        new_card_list = []
        for i in range(len(self)):
            new_card_list.append(self.deal())
        self.card_list = new_card_list

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = set()
        self.alive = True
    
    def total_points(self): return sum([card.point for card in self.cards])

    def __str__(self): return self.name + ': ' + str([str(card) for card in self.cards])

def initialize(player_list, deck):
    for player in player_list:
        player.cards.add(deck.deal())
        player.cards.add(deck.deal())

def player_turn(player):
    global deck, player_list
    take_card = input('Take a card? (\'y\' or \'n\')\n')
    # print(take_card)
    while take_card != 'y' and take_card != 'n':
        print('You can only input \'y\' or \'n\'')
        time.sleep(0.3)
        take_card = input('Take a card? (\'y\' or \'n\')')
    if take_card == 'y':
        player.cards.add(deck.deal())
        if player.total_points() > 21: 
            player.alive = False
            print(f'''
{player.name} explode
{player.name}\'s point: {player.total_points()}
            ''')
        else: print(f'''
{player.name} haven\'t explode
{player.name}\'s point: {player.total_points()}
        ''')
        return True
    
    return False
    


def next_turn():
    global turn

    if turn == len(player_list) - 1:
        turn = 0
    else: turn += 1

n = int(input('Number of players?\n'))
num = int(input('Number of decks?\n'))
for _ in range(n):
    name = input(f'Player{_ + 1}\'s name?\n')
    player_list.append(Player(name))

deck = Deck(num)
initialize(player_list, deck)

print('''
Game Starts
--------------------
''')
time.sleep(0.7)

Dealer = player_list[random.randint(0, n - 1)]
print(f'{Dealer.name} is the Dealer')
time.sleep(1.2)

# for player in player_list: print(player)

round = 0
proceed = True
while proceed:

    turn = player_list.index(Dealer)
    
    round += 1
    print(f'''
Round {round}
-------------------
    ''')

    while True:
        next_turn()
        if player_list[turn].alive:
            time.sleep(0.5)
            print(f'It\'s {player_list[turn].name}\'s turn')
            time.sleep(1)
            take_card = player_turn(player_list[turn])
            if player_list[turn] is Dealer: 
                if not take_card: proceed = False
                break
                
            
    
    

    

    




    
