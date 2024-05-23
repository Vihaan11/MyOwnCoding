import random

suits = ('Hearts',
         'Diamonds',
         'Spades',
         'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five',
         'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit0 in suits:
            for rank0 in ranks:
                # Create the card object
                created_card = Card(suit0, rank0)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def get_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.my_cards = []

    def __str__(self):
        return f"Player {self.name} has {len(self.my_cards)} cards"

    def remove_one(self):
        return self.my_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.my_cards.extend(new_cards)
        else:
            self.my_cards.append(new_cards)

game_on=True

player_one=Player("ONE")
player_two=Player("TWO")

new_Deck=Deck()
new_Deck.shuffle_deck()

for x in range(26):
    player_one.add_cards(new_Deck.get_one())
    player_two.add_cards(new_Deck.get_one())

round_num=0

while game_on:
    round_num+=1
    print(f"Round {round_num}")

    if len(player_one.my_cards)==0:
        print("Player One doesn't have enough cards! Player Two wins")
        game_on=False
        break
    if len(player_two.my_cards)==0:
        print("Player One doesn't have enough cards! Player One wins")
        game_on=False
        break

    # Start a new round
    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())
    player_two_cards=[]
    player_two_cards.append(player_two.remove_one())

    at_war=True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            # Favour of One
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war=False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            # Favour of Two
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war=False

        else:
            print("WAR!")
            if len(player_one.my_cards) < 5:
                print("Player One unable to fight war")
                print("Player Two wins!")

                game_on = False
                break

            elif len(player_two.my_cards) < 5:
                print("Player Two unable to fight war")
                print("Player One wins!")

                game_on = False
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
