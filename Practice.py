suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
suit = suits[2]
rank = "K"
value = 10

print(f"Your card is: {rank} of {suit}")

suits.append("Snakes")
#Aqui parece ser una variable del loop, na que ver con la variable del mismo nombre que esta arriba
for suit in suits:
    print(suit)