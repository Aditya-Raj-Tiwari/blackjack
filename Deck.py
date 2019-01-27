# to check if he wants to do next round or not
import random


def cardTurn():
    cardNumber = random.randint(1, 13)
    cards = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
             'K': 13}

    for i, j in cards.items():
        if cardNumber == j:
            if j >= 10:
               return 10,i
            return j, i

def playerhand(number):
    playertotal = 0
    play = True

    while play:
        ans = input('Do you want to stand or hit (h-> hit s--> stand) : ').lower()
        if ans == 'h':
            playertotal += number
            return True,playertotal

        else:
            return False,0




# number,cardName = cardTurn()
# print(str(number)+' '+cardName)
