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
        
check = set(card())
take_card = check.__iter__()

def random_card(num):
    x = 0
    while x < num:
        print(take_card.__next__())
        x += 1
        
random_card(5)