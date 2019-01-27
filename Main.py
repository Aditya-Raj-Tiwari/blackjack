import Comp as cmp
import Deck as d
import PlayerHand as ph


def mainmenu():
    playerName = input("What if your name: ")
    betAmount = int(input('Please enter the amount you want to bet you have 900 :  '))
    compTotal = 0
    playerTotal = 0
    play = True
    while play:
        cardVal, cardName = d.cardTurn()
        play, add = d.playerhand(cardVal)
        playerTotal += add
        amount, crdCompname = cmp.takingturn(0)
        compTotal += amount
        print(f'you got {cardName} and now you have a total of {playerTotal}')

    print(f'Comp got a total of {compTotal}')
    ph.moneyTransction(check(playerTotal, playerName, compTotal), betAmount)



def check(playertotal, name, comptotal):
    compCompute = abs(21 - comptotal)
    playerCompute = abs(21 - playertotal)
    if playerCompute > compCompute:
        # print(f'{name} got busted!! Comp wins B-) ')
        return False
    elif compCompute > playerCompute:
        return True


mainmenu()
