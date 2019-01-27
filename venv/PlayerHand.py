def moneyTransction(boolval,betAmount):
    givenamt = 900
    if betAmount > givenamt:
        print('Sorry cannot bet more than you have')
    else:
        givenamt -= betAmount
        print(f'You have betted {betAmount} you have {givenamt}')
        if boolval == True:
            givenamt += (betAmount * 2)
            print(f'\n'
                  f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n'
                  f'You won {(betAmount * 2)} and now have {givenamt}\n'
                  f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
        else:
            print(f'YOu lost {betAmount} and you have {givenamt}')