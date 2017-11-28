from tinydb import *
import database as dbs

db = TinyDB("DB.json")
Card = Query()
cards = db.table('cards')

dbs.display_cards(cards.all())
print()


def menu():
    choice = '0'
    while choice != '6':
        print("Main Choice: Choose 1 of 5 choices")
        print("1.Add card")
        print("2.Delete card")
        print("3.Check balance")
        print("4.Put money")
        print("5.Get money")

        choice = input("Please make a choice: ")

        if choice == "5":
            print("Go to another menu")
        elif choice == "4":
            print("Do Something 4")
        elif choice == "3":
            dbs.balance(cards.all())
            dbs.total_balance(cards.all())
        elif choice == "2":
            dbs.delete_card(cards)
        elif choice == "1":
            dbs.arr_card_db(cards)
        else:
            print("EXIT")


menu()