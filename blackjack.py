import random
import os


def calc_hand(hand):
    sum = 0
    non_aces = [card for card in hand if card != 'A']
    aces = [card for card in hand if card == 'A']
    for card in non_aces:
        if card in 'JQK':
            sum += 10
        else:
            sum += int(card)
    for card in aces:
        if sum <= 10:
            sum += 11
        else:
            sum += 1

    return sum


cards = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
]

random.shuffle(cards)

dealer = []
player = []

player.append(cards.pop())
dealer.append(cards.pop())
player.append(cards.pop())
dealer.append(cards.pop())

standing = False
first_hand = True

while True:
    os.system('cls')
    player_score = calc_hand(player)
    dealer_score = calc_hand(dealer)

    if standing:
        print('Dealer Cards: [{}] ({})'.format(']['.join(dealer), dealer_score))
    else:
        print('Dealer Cards: [{}][?]'.format(dealer[0]))
    print('Your Cards: [{}] ({})'.format(']['.join(player), player_score))
    print('')

    if standing:
        if dealer_score > 21:
            print('Dealer busted, you win!')
        elif player_score == dealer_score:
            print('Push!')
        elif player_score > dealer_score:
            print('You beat the dealer, you win!')
        else:
            print("You lose, try again!")

        break

    if first_hand and player_score == 21:
        print("Blackjack! You Win!")
        break

    first_hand = False

    if player_score > 21:
        print("You busted! Game Over")
        break

    print('Hit or Stand?')
    print(' [1] to hit or [2] to stand')
    print('')
    choice = input('Your choice: ')
    print('')

    if choice == '1':
        player.append(cards.pop())
    elif choice == '2':
        standing = True
        while calc_hand(dealer) <= 16:
            dealer.append(cards.pop())
##test
##test
