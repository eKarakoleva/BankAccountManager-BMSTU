import classes as cl
from tinydb import *
import os


db = TinyDB("DB.json")

Card = Query()
cards = db.table('cards')


def empty_file():
    if not cards.all():
        return True
    else:
        return False


def display_cards():
    if not empty_file():
        i = 0
        all_cards = cards.all()
        for card in all_cards:
            print('%d) %s   %s' % (i+1, card['name'], card['bank']))
            i += 1
    else:
        print('No cards')
        return 1


def get_cards():
    arr = []
    if not empty_file():
        i = 0
        all_cards = cards.all()
        for card in all_cards:
            arr.append(card)
            i += 1
        return arr
    return arr


def add_card():
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
    if not empty_file():
        number = int(input('Please write card number in order to delete'))
        cards.remove(where('number') == number)
        print('Card is deleted!')
    else:
        print('There are no cards to be deleted!')


def balance(option):
    ar = get_cards()
    if ar:
        print('Balance: %f' % ar[option - 1]['balance'])
        print()
    else:
        print('There are no cards!')


def total_balance():
    total = 0
    for card in cards:
        total += card['balance']
    print('Total balance: %f'%total)
    print()


def import_money(option):
    ar = get_cards()
    if ar:
        money = float(input('Amount of money you wanna insert: '))
        new_balance = ar[option - 1]['balance'] + money
        cards.update({'balance': new_balance}, Card.number == ar[option - 1]['number'])
        print()
    else:
        print('There are no cards!')


def withdraw_money(option):
    ar = get_cards()
    if ar:
        money = float(input('Amount of money you wanna withdraw: '))
        new_balance = ar[option - 1]['balance'] - money
        current_balance = ar[option - 1]['balance']
        if money < current_balance:
            cards.update({'balance': new_balance}, Card.number == ar[option - 1]['number'])
        else:
            print('Not enough money in the card!')
    return 1


