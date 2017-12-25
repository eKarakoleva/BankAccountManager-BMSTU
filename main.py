import database as dbs
from tinydb import *


def menu():
    print()
    while 1:
        print("Actions with cards:")
        print("   1.Add card")
        print("   2.Delete card")
        print("   3.Import money")
        print("   4.Withdraw money")
        print("Actions with categories:")
        print("   5.Create category")
        print("   6.Delete category")
        print("   7.Show all categories")
        print("Information:")
        print("   8.Check balance")
        print("   9.Show chart of imports and withdraws by month")
        print("   10.Show chart of withdraws by category")
        print("   11.Show all withdraws")
        print("      11.1 Show withdraws by card")
        print("      11.2 Show withdraws by category")
        print("      11.3 Show withdraws by date (today)")
        print("      11.4 Show withdraws by month")
        print("   12.Show transfers")
        print("   13.Show all imports")
        print("      13.1 Show imports by card")
        print("      13.2 Show imports by date (today)")
        print("      13.3 Show imports by month")
        print("Actions with history:")
        print("   14.Delete all")
        print("      14.1 Delete by card")
        print("      14.2 Delete by category")
        print("Transfers")
        print("   15.Transfer between cards")
        print("")

        choice = input("Please make a choice: ")
        print()
        if choice == "15":
            db = TinyDB("DB.json")
            cards = db.table('cards')
            if len(cards.all()) > 1:
                display = dbs.display_cards()
                if display != 1:
                    print()
                    op1 = int(input('Choose a card to withdraw from: '))
                    op2 = int(input('Choose a card to insert in: '))
                    if op1 != op2:
                        money = float(input('Amount of money you wanna insert: '))
                        dbs.transfer(op1, op2, money)
                    else:
                        print("You must have 2 or more cards to make this operation")
            else:
                print("You have only one card!")
            del cards
            del db
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "14.2":
            display = dbs.display_categories()
            if display != 1:
                print()
                op = int(input('Choose category: '))
                dbs.delete_history_category(op)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "14.1":
            display = dbs.display_cards()
            if display != 1:
                print()
                op = int(input('Choose card: '))
                dbs.delete_history_card(op)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "14":
            op = input('Are you sure you want to delete all history?')
            if op == 'Y' or op == 'y':
                dbs.delete_history()
            else:
                print("Action canceled")
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "13.3":
            month = int(input("Enter number of a month you want to check (1 to 12)"))
            if month <= 12:
                dbs.search_by_month(month, "import")
            else:
                print("Enter number between 1 and 12")
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "13.2":
            dbs. operations_today("import")
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "13.1":
            display = dbs.display_cards()
            if display != 1:
                print()
                op = int(input('Choose card: '))
                dbs.show_imports_card(op)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "13":
            dbs.show_imports()
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "12":
            dbs.show_transfers()
            print()
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "11.3":
            dbs.operations_today("withdraw")
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "11.4":
            month = int(input("Enter number of a month you want to check (1 to 12)"))
            if month <= 12:
                dbs.search_by_month(month, "withdraw")
            else:
                print("Enter number between 1 and 12")
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "11.2":
            display = dbs.display_categories()
            if display != 1:
                print()
                op = int(input('Choose category: '))
                dbs.show_withdraws_category(op)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "11.1":
            display = dbs.display_cards()
            if display != 1:
                print()
                op = int(input('Choose card: '))
                dbs.show_withdraws_card(op)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "11":
            dbs.show_withdraws()
            print()
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "10":
            dbs.chart_operation_category()
            print()
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "9":
            month = int(input("Enter number of a month you want to check (1 to 12)"))
            if month <= 12:
                dbs.chart_operation_month(month)
            else:
                print("Enter number between 1 and 12")
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "8":
            display = dbs.display_cards()
            if display != 1:
                print()
                op = int(input('Choose card: '))
                dbs.balance(op)
            dbs.total_balance()
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "7":
            dbs.display_categories()
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "6":
            display = dbs.display_categories()
            if display != 1:
                print()
                op = int(input('Choose category: '))
                dbs.delete_category(op)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "5":
            name = input("Write category: ")
            dbs.create_category(name)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "4":
            display = dbs.display_cards()
            if display != 1:
                print()
                op = int(input('Choose card: '))
                money = float(input('Amount of money you wanna withdraw: '))
                dbs.display_categories()
                op_category = int(input("Choose category"))
                op_description = input("Add description (optional): ")
                dbs.withdraw_money(op,money,op_category,op_description)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "3":
            display = dbs.display_cards()
            if display != 1:
                print()
                op = int(input('Choose card: '))
                money = float(input('Amount of money you wanna insert: '))
                dbs.import_money(op,money)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "2":
            dbs.delete_card()
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "1":
            dbs.add_card()
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        else:
            print("EXIT")
            break
    return 0

menu()