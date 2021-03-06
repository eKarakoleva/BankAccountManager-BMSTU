import classes as cl
from tinydb import *
from tinydb_serialization import SerializationMiddleware
from time import gmtime, strftime
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

serialization = SerializationMiddleware()
serialization.register_serializer(cl.DateTimeSerializer(), 'TinyDate')
db = TinyDB("DB.json", storage = serialization)


Card = Query()
History = Query()
cards = db.table('cards')
history = db.table('history')
categories = db.table('categories')
default_cat = ["No category", "Transfer"]


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
            print('%d) %s  %s' % (i+1, card['name'], card['bank']))
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
        print("%d) %s" %((i + 1), default_cat[0]))
        del all_cat
    else:
        print("%d) %s" % (1, default_cat[0]))


def check_id(new_id):
    if cards.contains(Card.number == new_id):
        return True
    else:
        return False


def add_card():
    arr = []
    en = input('Enter card name')
    arr.append(en)
    try:
        en = int(input('Enter card number'))
    except ValueError:
        print("Card number can contain only digits")
        return 1
    if not check_id(en):
        arr.append(en)
        try:
            en = float(input('Enter card balance'))
        except ValueError:
            print("Card balance can contain only digits")
            return 1
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
        card_info = cards.search(where('number') == number)
        if int(card_info[0]['balance']) > 0:
            op = input("You have money in your card. Are you sure you want to delete it?")
            if op == "Y" or op == "y":
                cards.remove(where('number') == number)
                history.remove(where('card_id') == number)
                print('Card is deleted!')
            else:
                print("Operation is canceled")
        else:
            cards.remove(where('number') == number)
            history.remove(where('card_id') == number)
    else:
        print('There are no cards to be deleted!')


def balance(option):
    ar = cards.all()
    option = abs(option)
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


def import_money(option, money):
    ar = cards.all()
    option = abs(option)
    if len(ar) < option:
        print('Invalid option!')
        del ar
        return 1
    if ar:
        new_balance = ar[option - 1]['balance'] + abs(round(money, 2))
        cards.update({'balance': new_balance}, Card.number == ar[option - 1]['number'])
        add_operation(ar, option, money, "import", "", "")
        print("Success!")
    else:
        print('There are no cards!')
    del ar


def choose_category_check(option):
    cats = categories.all()
    option = abs(option)
    if len(cats) >= option:
        return cats[option - 1]['name']
    else:
        del cats
        return default_cat[0]


def withdraw_money(option, money, op_category, op_description):
    all_cards = cards.all()
    option = abs(option)
    if len(all_cards) >= option:
        if all_cards:
            new_balance = all_cards[option - 1]['balance'] - abs(round(money, 2))
            current_balance = all_cards[option - 1]['balance']
            if money < current_balance:
                cards.update({'balance': new_balance}, Card.number == all_cards[option - 1]['number'])
                if not isinstance(op_category, str):
                    cat_name = choose_category_check(op_category)
                else:
                    cat_name = default_cat[1]
                add_operation(all_cards, option, money, "withdraw", cat_name, op_description)
            else:
                print('Not enough money in the card!')
    else:
        print('Invalid option!')
    del all_cards
    return 1


def add_operation(b_card, option, money, op_type, op_category, op_description):
    date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(" ")
    data = [b_card[option - 1]['number'], op_type, money, op_category, op_description, date_time[0], date_time[1]]
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
    option = abs(option)
    if not empty_categories_database():
        category = choose_category_check(option)
        if category != default_cat[0]:
            categories.remove(where('name') == category)
            op = input("Do you want to delete history with this categoty too?")
            if op == 'Y' or op == 'y':
                history.remove(where('category') == category)
            print('Category is deleted!')
        else:
            print("This is default category and can not be deleted!")
    else:
        print('There are no categories to be deleted!')


def print_res(operation, c_names):
    if operation['card_id'] not in c_names:
        name = cards.search(where('number') == operation['card_id'])
        c_names[operation['card_id']] = name[0]['name']
        del name
    if operation['category'] != "":
        print('CARD: %s \nMONEY: %.2f \nCATEGORY: %s \nDESCRIPTION: %s\nDATE: %s\nTIME: %s\n'
              % (c_names[operation['card_id']], operation['money'], operation['category'],
                 operation['description'], operation['date'],
                 operation['time']))
    else:
        print('CARD: %s \nMONEY: %.2f \nDATE:%s\nTIME: %s\n' % (c_names[operation['card_id']],
                                                                operation['money'], operation['date'],
                                                                operation['time']))
    del c_names


def search_operation(data):
    if data:
        c_names = {}
        for operation in data:
            print_res(operation, c_names)

        del data
    else:
        print("Nothing found!")


def show_withdraws():
    data = history.search(where('operation') == "withdraw")
    search_operation(data)
    del data


def show_withdraws_card(option):
    ar = cards.all()
    option = abs(option)
    if len(ar) >= option:
        card_num = ar[option - 1]['number']
        data = history.search((History.card_id == card_num) & (History.operation == "withdraw"))
        search_operation(data)
    else:
        print("Invalid option")
    del ar


def show_withdraws_category(option):
    option = abs(option)
    category = choose_category_check(option)
    data = history.search(where('category') == category)
    search_operation(data)


def show_imports():
    data = history.search(where('operation') == "import")
    search_operation(data)
    del data


def show_imports_card(option):
    ar = cards.all()
    option = abs(option)
    if len(ar) >= option:
        card_num = ar[option - 1]['number']
        data = history.search((History.card_id == card_num) & (History.operation == "import"))
        search_operation(data)
    else:
        print("Invalid option!")
    del ar


def delete_history():
    if not empty_history_database():
        history.purge()


def delete_history_card(option):
    if not empty_history_database():
        ar = cards.all()
        option = abs(option)
        if len(ar) >= option:
            card_num = ar[option - 1]['number']
            history.remove(where('card_id') == card_num)
        else:
            print("Invalid option")


def delete_history_category(option):
    if not empty_history_database():
        ar = categories.all()
        option = abs(option)
        if len(ar) >= option or not (len(ar)+1 == option):
            category = choose_category_check(option)
            history.remove(where('category') == category)
        else:
            print("Invalid option or you're trying\nto delete default category")


def transfer(card1, card2, money):
    ar = cards.all()
    op_description = "Transfer from " + ar[card1-1]['name'] + " to " + ar[card2-1]['name']
    withdraw_money(card1, money, default_cat[1], op_description)
    import_money(card2, money)


def show_transfers():
    data = history.search(where('category') == default_cat[1])
    search_operation(data)
    del data


def operations_today(search_op):
    date_now = strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(" ")
    data = history.search((History.date == date_now[0]) & (History.operation == search_op))
    search_operation(data)


def search_by_month(month, his_operation):
    his = history.all()
    c_names = {}
    for entry in his:
        date = entry['date'].split("-")
        if int(date[1]) == month and entry['operation'] == his_operation:
            print_res(entry, c_names)


def get_month_money(month, his_operation):
    his = history.all()
    month_money = 0
    if his:
        for entry in his:
            date = entry['date'].split("-")
            if int(date[1]) == month and entry['operation'] == his_operation:
                month_money += entry['money']
    return month_money



def chart_operation_month(month):
    w_money = get_month_money(month, "withdraw")
    i_money = get_month_money(month, "import")

    objects = ('Withdraws', 'Imports')
    y_pos = np.arange(len(objects))
    money = [w_money, i_money]

    plt.bar(y_pos, money, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Money')
    plt.title('Money moving')
    plt.show()


def get_sum_withdraws_category(o_categoty):
    data = history.search((History.category == o_categoty) & (History.operation == "withdraw"))
    sum_money = 0
    if data:
        for entry in data:
            sum_money += entry['money']
    return sum_money


def chart_operation_category():
    cats = categories.all()
    money = []
    objects = []
    for category in cats:
        money.append(get_sum_withdraws_category(category['name']))
        objects.append(category['name'])
    money.append(get_sum_withdraws_category(default_cat[0]))
    objects.append(default_cat[0])

    y_pos = np.arange(len(objects))
    plt.bar(y_pos, money, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Money')
    plt.title('Withdraws by category')
    plt.show()
