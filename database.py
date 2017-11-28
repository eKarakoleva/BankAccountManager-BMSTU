import classes as cl
from tinydb import *


def display_cards(cards):
    i = 0
    arr = []
    for card in cards:
        print('%d) %s   %s' % (i+1, card['name'], card['bank']))
        arr.append(card)
        i += 1
    return arr


def arr_card_db(cards):
    arr = []
    print("Do Something 1")
    en = input('Enter card name')
    arr.append(en)
    en = int(input('Enter card number'))
    arr.append(en)
    en = float(input('Enter card balance'))
    arr.append(en)
    en = input('Enter card bank')
    arr.append(en)
    emp1 = cl.Card(arr)
    data = emp1.add_card()
    cards.insert(data)


def delete_card(cards):
    number = int(input('Please write card number in order to delete'))
    cards.remove(where('number') == number)


def balance(cards):
    ar = display_cards(cards)
    op = int(input('Choose card: '))
    print('Balance: %f' % ar[op - 1]['balance'])
    print()


def total_balance(cards):
    total = 0
    for card in cards:
        total += card['balance']
    print("Total balance: %f"%total)
    print()
