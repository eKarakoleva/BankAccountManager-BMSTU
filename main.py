import database as dbs

def menu():
    #choice = input("Please make a choice: ")
    print()
    while 1:
        print("Main Choice: Choose 1 of 5 choices")
        print("Actions with cards:")
        print("   1.Add card")
        print("   2.Delete card")
        print("   3.Check balance")
        print("   4.Import money")
        print("   5.Withdraw money")
        print("Actions with categories:")
        print("   6.Create category")
        print("   7.Delete category")
        print("   8.Show all categories")
        print("Information:")
        print("   9.Show all withdraws")
        print("      9.1 Show withdraws by card")
        print("      9.2 Show withdraws by category")
        print("   10.Show all imports")
        print("      10.1 Show imports by card")
        print("Actions with history:")
        print("   11.Delete all")
        print("      11.1.Delete by card")
        print("      11.2.Delete by category")
        print("~Transfers")
        print("   ~12.Transfer between cards")
        print("")

        choice = input("Please make a choice: ")
        print()
        if choice == "11.2":
            display = dbs.display_categories()
            if display != 1:
                print()
                op = int(input('Choose category: '))
                dbs.delete_history_category(op)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "11.1":
            display = dbs.display_cards()
            if display != 1:
                print()
                op = int(input('Choose card: '))
                dbs.delete_history_card(op)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "11":
            op = input('Are you sure you want to delete all history?')
            if op == 'Y' or op == 'y':
                dbs.delete_history()
            else:
                print("Action canceled")
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "10.1":
            display = dbs.display_cards()
            if display != 1:
                print()
                op = int(input('Choose card: '))
                dbs.show_imports_card(op)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "10":
            dbs.show_imports()
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "9.2":
            display = dbs.display_categories()
            if display != 1:
                print()
                op = int(input('Choose category: '))
                dbs.show_withdraws_category(op)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "9.1":
            display = dbs.display_cards()
            if display != 1:
                print()
                op = int(input('Choose card: '))
                dbs.show_withdraws_card(op)

            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "9":
            dbs.show_withdraws()
            print()
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "8":
            dbs.display_categories()
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "7":
            display = dbs.display_categories()
            if display != 1:
                print()
                op = int(input('Choose category: '))
                dbs.delete_category(op)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "6":
            name = input("Write category: ")
            dbs.create_category(name)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "5":
            display = dbs.display_cards()
            if display != 1:
                print()
                op = int(input('Choose card: '))
                dbs.withdraw_money(op)
            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "4":
            display = dbs.display_cards()
            if display != 1:
                print()
                op = int(input('Choose card: '))
                dbs.import_money(op)
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
    return 0

menu()