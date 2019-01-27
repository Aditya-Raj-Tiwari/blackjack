import Deck as d
import random


def takingturn(totalamt):
    taketurn= True
    while taketurn:
        cardNo, cardName = d.cardTurn()
        totalamt += cardNo
        break

    return totalamt,cardName