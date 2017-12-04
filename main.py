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
        print()

        if choice == "5":
            display = dbs.display_cards()
            if display != 1:
                print()
                op = int(input('Choose card: '))
                dbs.withdraw_money(op)
                dbs.balance(op)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "4":
            display = dbs.display_cards()
            if display != 1:
                print()
                op = int(input('Choose card: '))
                dbs.import_money(op)
                dbs.balance(op)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "3":
            display = dbs.display_cards()
            if display != 1:
                print()
                op = int(input('Choose card: '))
                dbs.balance(op)
            dbs.total_balance()
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


menu()