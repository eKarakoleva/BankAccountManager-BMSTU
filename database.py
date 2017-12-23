import classes as cl
#from datetime import datetime
from tinydb import *
from tinydb_serialization import SerializationMiddleware

serialization = SerializationMiddleware()
serialization.register_serializer(cl.DateTimeSerializer(), 'TinyDate')
db = TinyDB("DB.json", storage = serialization)


Card = Query()
History = Query()
cards = db.table('cards')
history = db.table('history')
categories = db.table('categories')

#cards.insert({'date': datetime.now()})

def empty_cards_database():
    if not cards.all():
        return True
    else:
        return False


def empty_categories_database():
    if not categories.all():
        return True
    else:
        return False

def empty_history_database():
    if not history.all():
        return True
    else:
        return False


def display_cards():
    if not empty_cards_database():
        i = 0
        all_cards = cards.all()
        for card in all_cards:
            print('%d) %s   %s' % (i+1, card['name'], card['bank']))
            i += 1
        del all_cards
    else:
        print('No cards')
        return 1


def display_categories():
    if not empty_categories_database():
        i = 0
        all_cat = categories.all()
        for category in all_cat:
            print('%d) %s' % (i + 1, category['name']))
            i += 1
        print("%d) No category" %(i + 1))
        del all_cat
    else:
        print("%d) No category" % 1)


def check_id(new_id):
    b_cards = cards.all()
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
    if not empty_cards_database():
        number = int(input('Please write card number in order to delete'))
        cards.remove(where('number') == number)
        history.remove(where('card_id') == number)
        print('Card is deleted!')
    else:
        print('There are no cards to be deleted!')


def balance(option):

    ar = cards.all()
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
    ar = cards.all()
    if len(ar) < option:
        print('Invalid option!')
        del ar
        return 1
    if ar:
        money = float(input('Amount of money you wanna insert: '))
        new_balance = ar[option - 1]['balance'] + money
        cards.update({'balance': new_balance}, Card.number == ar[option - 1]['number'])
        add_operation(ar, option, money, "import","")
        print()
    else:
        print('There are no cards!')
    del ar


def choose_category_check(option):
    cats = categories.all()
    if len(cats) >= option:
        return cats[option - 1]['name']
    else:
        del cats
        return "No category"


def withdraw_money(option):
    all_cards = cards.all()
    if all_cards:
        money = float(input('Amount of money you wanna withdraw: '))
        new_balance = all_cards[option - 1]['balance'] - money
        current_balance = all_cards[option - 1]['balance']
        if money < current_balance:
            cards.update({'balance': new_balance}, Card.number == all_cards[option - 1]['number'])
            display_categories()
            op_category = int(input("Choose category"))
            cat_name = choose_category_check(op_category)
            add_operation(all_cards, option, money, "withdraw", cat_name)
        else:
            print('Not enough money in the card!')
    del all_cards
    return 1


def add_operation(b_card, option, money, op_type, op_category):
    data = [b_card[option - 1]['number'], op_type, money, op_category]
    operation = cl.Operation(data)
    entry = operation.create_operation()
    history.insert(entry)


def check_category(name):
    if len(categories.search(where('name') == name)) > 0:
        return True
    else:
        return False


def create_category(name):
    if not check_category(name):
        category = cl.Category(name)
        data = category.create_category()
        categories.insert(data)
    else:
        print("This category already exist!!!")


def delete_category(option):
    if not empty_categories_database():
        category = choose_category_check(option)
        if category != "No category":
            categories.remove(where('name') == category)
            history.remove(where('category') == category)
            print('Category is deleted!')
        else:
            print("This is default category and can not be deleted!")
    else:
        print('There are no categories to be deleted!')


def search_operation(data):
    if data:
        c_names = {}
        for operation in data:
            if operation['card_id'] not in c_names:
                name = cards.search(where('number') == operation['card_id'])
                c_names[operation['card_id']] = name[0]['name']
                del name
            if operation['category'] != "":
                print('CARD: %s MONEY: %f OPERATION: %s' % (c_names[operation['card_id']],
                                                        operation['money'],
                                                        operation['category']))
            else:
                print('CARD: %s MONEY: %f' % (c_names[operation['card_id']],
                                                            operation['money'],
                                                            ))
        del c_names
        del data
    else:
        print("Nothing found!")


def show_withdraws():
    data = history.search(where('operation') == "withdraw")
    search_operation(data)
    del data


def show_withdraws_card(option):
    ar = cards.all()
    card_num = ar[option - 1]['number']
    data = history.search((History.card_id == card_num) & (History.operation == "withdraw"))
    search_operation(data)
    del ar


def show_withdraws_category(option):
    category = choose_category_check(option)
    data = history.search(where('category') == category)
    search_operation(data)


def show_imports():
    data = history.search(where('operation') == "import")
    search_operation(data)
    del data


def show_imports_card(option):
    ar = cards.all()
    card_num = ar[option - 1]['number']
    data = history.search((History.card_id == card_num) & (History.operation == "import"))
    search_operation(data)
    del ar


def delete_history():
    if not empty_history_database():
        history.purge()


def delete_history_card(option):
    if not empty_history_database():
        ar = cards.all()
        card_num = ar[option - 1]['number']
        history.remove(where('card_id') == card_num)


def delete_history_category(option):
    if not empty_history_database():
        category = choose_category_check(option)
        history.remove(where('category') == category)



