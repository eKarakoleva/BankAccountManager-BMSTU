import classes as cl
from tinydb import *


db = TinyDB("DB.json")

Card = Query()
cards = db.table('cards')
history = db.table('history')


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
        del all_cards
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
        del all_cards
        return arr
    return arr


def check_id(new_id):
    b_cards = get_cards()
    for card in b_cards:
        if card['number'] == new_id:
            del b_cards
            return True
        else:
            del b_cards
            return False


def add_card():
    arr = []
    en = input('Enter card name')
    arr.append(en)
    en = int(input('Enter card number'))
    if not check_id(en):
        arr.append(en)
        en = float(input('Enter card balance'))
        arr.append(en)
        en = input('Enter card bank')
        arr.append(en)
        emp1 = cl.Card(arr)
        data = emp1.add_card()
        cards.insert(data)
        print('New card is added!')
    else:
        print('Card ID must be unique!')


def delete_card():
    if not empty_file():
        number = int(input('Please write card number in order to delete'))
        cards.remove(where('number') == number)
        history.remove(where('card_id') == number)
        print('Card is deleted!')
    else:
        print('There are no cards to be deleted!')


def balance(option):

    ar = get_cards()
    if len(ar) < option:
        print('Invalid option!')
        del ar
        return 1
    if ar:
        print('Balance: %f' % ar[option - 1]['balance'])
        print()
    else:
        print('There are no cards!')
    del ar


def total_balance():
    total = 0
    for card in cards:
        total += card['balance']
    print('Total balance: %f'%total)
    print()


def import_money(option):
    ar = get_cards()
    if len(ar) < option:
        print('Invalid option!')
        del ar
        return 1
    if ar:
        money = float(input('Amount of money you wanna insert: '))
        new_balance = ar[option - 1]['balance'] + money
        cards.update({'balance': new_balance}, Card.number == ar[option - 1]['number'])
        add_operation(ar, option, money, "import")
        print()
    else:
        print('There are no cards!')
    del ar


def withdraw_money(option):
    ar = get_cards()
    if ar:
        money = float(input('Amount of money you wanna withdraw: '))
        new_balance = ar[option - 1]['balance'] - money
        current_balance = ar[option - 1]['balance']
        if money < current_balance:
            cards.update({'balance': new_balance}, Card.number == ar[option - 1]['number'])
            add_operation(ar, option, money, "withdraw")
        else:
            print('Not enough money in the card!')
    del ar
    return 1


def add_operation(b_card, option, money, op_type):
    data = [b_card[option - 1]['number'], op_type, money, 'savings']
    operation = cl.Operation(data)
    entry = operation.create_operation()
    history.insert(entry)


def show_withdraws():
    data = history.search(where('operation') == "withdraw")
    for b_card in get_cards():
        for operation in data:
            print('CARD: %s MONEY: %f OPERATION: %s'%(b_card['name'],
                                                      operation['money'],
                                                    operation['category']))
    del data
