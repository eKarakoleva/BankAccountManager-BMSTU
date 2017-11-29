import database as dbs

dbs.display_cards()
print()


def menu():
    choice = '0'
    while choice != '6':
        print("Main Choice: Choose 1 of 5 choices")
        print("1.Add card")
        print("2.Delete card")
        print("3.Check balance")
        print("4.Import money")
        print("5.Withdraw money")

        choice = input("Please make a choice: ")

        if choice == "5":
            dbs.display_cards()
            op = int(input('Choose card: '))
            dbs.withdraw_money(op)
            dbs.balance(op)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "4":
            dbs.display_cards()
            op = int(input('Choose card: '))
            dbs.import_money(op)
            dbs.balance(op)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "3":
            dbs.display_cards()
            op = int(input('Choose card: '))
            dbs.balance(op)
            dbs.total_balance()
            if op == 'N' or op == 'n':
                break
        elif choice == "2":
            dbs.delete_card()
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "1":
            dbs.arr_card_db()
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        else:
            print("EXIT")


menu()