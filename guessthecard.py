import random

a = ['6 ', '7 ', '8 ', '9 ', '10 ', 'Jack ', 'Queen ', 'King ', 'Ace ']
b = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
deck = []
i = 0
j = 0
def card(): 
    for i in range(len(a)):
        i = int(i)
        for j in range(len(b)):
            j = int(j)
            deck.append(a[i] + b[j])
    return deck
        
check = card()
cards = []

def random_card(num) -> int:
    x = 0
    while x < num:
        cards.append(check[random.randrange(0, len(check))])
        x += 1
        
def guess(user_card) -> str:
    if user_card in cards:
        print(f"Congratz!!! You're a genius!!!")
    else:
        print(f"Better luck next time...")
        
random_card(int(input('Enter the number of cards: ')))
guess(input('Pick your card: '))
print(cards)