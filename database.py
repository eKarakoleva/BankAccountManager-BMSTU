import classes as cl
from tinydb import *


db = TinyDB("DB.json")
Card = Query()
cards = db.table('cards')


def display_cards():
    i = 0
    all_cards = cards.all()
    for card in all_cards:
        print('%d) %s   %s' % (i+1, card['name'], card['bank']))
        i += 1


def get_cards():
    i = 0
    arr = []
    all_cards = cards.all()
    for card in all_cards:
        arr.append(card)
        i += 1
    return arr


def arr_card_db():
    arr = []
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
    print('New card is added!')


def delete_card():
    number = int(input('Please write card number in order to delete'))
    cards.remove(where('number') == number)
    print('Card is deleted!')


def balance(option):
    ar = get_cards()
    print('Balance: %f' % ar[option - 1]['balance'])
    print()


def total_balance():
    total = 0
    for card in cards:
        total += card['balance']
    print('Total balance: %f'%total)
    print()


def import_money(option):
    ar = get_cards()
    money = float(input('Amount of money you wanna insert: '))
    new_balance = ar[option - 1]['balance'] + money
    cards.update({'balance': new_balance}, Card.number == ar[option - 1]['number'])
    print()


def withdraw_money(option):
    ar = get_cards()
    money = float(input('Amount of money you wanna withdraw: '))
    new_balance = ar[option - 1]['balance'] - money
    current_balance = ar[option - 1]['balance']
    if money < current_balance:
        cards.update({'balance': new_balance}, Card.number == ar[option - 1]['number'])
    else:
        print('Not enough money in the card!')

