from random import shuffle
import sys

class Player(object):
    def __init__(self, username: str):
        self.username = username
        ''' The name of this player. '''

        self.hand = []
        ''' A list of cards (2) representing this player's hand.'''
    
class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __cmp__(self, other):
        if self.value < other.value:
            return -1
        elif self.value == other.value:
            return 0
        return 1

    def __str__(self):
        switch = {
            0: "spades",  #'♠',
            1: "hearts", #'♡',
            2: "diamonds", #'♢',
            3: "clubs" #'♣'
        }
        card_value = {
            1: "A",
            11: "J",
            12: "Q",
            13: "K"
        }
        if self.value != 1 and self.value <= 10 :
            return "[" + str(self.value) + " of " + switch.get(self.suit, "Invalid suit") + "]"
        else:
            return "[" + str(card_value.get(self.value, "0")) + " of " + switch.get(self.suit, "Invalid suit") + "]"

class Deck(object):
    def __init__(self):
        # Total cards in deck.
        self.cards_facedown = []
        # Array of cards currently in play.
        self.cards_active = []

        # Populate the deck with every combination of suit/values
        for suit in range(4):
            for value in range(1, 14):
                card = Card(suit, value)
                self.cards_facedown.append(card)

    def shuffle(self):
        ''' Shuffles the position of the cards in the deck. '''

        self.cards_facedown.extend(self.cards_active)
        self.cards_active = []
        shuffle(self.cards_facedown)

        # Return amount of cards remaining in deck
    def cards_left(self):
        return len(self.cards_facedown)

class Poker:
    def __init__(self, players):
        self.deck = Deck()
       # Ensure there is just enough people to play
        if len(players) < 2 or len(players) > 10:
            sys.exit("Insufficient players. Must be between 2 and 10 players")
        else:
            self.players = players

    def fold(self, player):
        ''' To fold is to discard a player's cards. In this instance, we'll just return them back into the deck.'''
        self.deck.cards_facedown.extend(player.hand)
        player.hand = []

    def distribute_cards(self):
        # check if there are enough cards for each player
        if (len(self.players) * 2) > self.deck.cards_left():
            print("Not enough cards in the deck.")
            return False
        else:
            # hand each player two cards from the deck
            for i in range(2):
                for player in self.players:
                    card = self.deck.cards_facedown.pop(i)
                    print(player.username + " is being handed a card: " + str(card))
                    player.hand.append(card)
