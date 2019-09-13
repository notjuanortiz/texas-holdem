from .poker import Player, Poker

players = [Player("Tim"), Player("Joe"), Player("Josie"), Player("Tiffany")]

# Create game
poker = Poker(players)

# Shuffle the deck
print("Shuffling deck...")
poker.deck.shuffle()

# Deal cards to players
print("Dealing cards...")
print(" ---- Dealer Activity ---- ")
poker.distribute_cards()

print("There are " + str(poker.deck.cards_left()) + " cards left in the deck.")

# Display each player's hand
print(" ---- Active Hands ---- ")
for player in players:
    print(player.username + ": ")
    cardString = ""
    for card in player.hand:
        cardString += str(card)
       # cardString += " " + str(poker.score(player.hand)) + "%"
    print(cardString)
print("-----------------------")
