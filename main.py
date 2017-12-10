import database as dbs

dbs.display_cards()
print()


def menu():
    choice = input("Please make a choice: ")
    print()
    while choice != '6':
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
        print("Information:")
        print("   8.Show all withdraws")
        print("      8.1 Show withdraws by card")
        print("      8.2 Show withdraws by category")
        print("   ~9.Show all imports")
        print("      ~9.1 Show imports by card")
        print("~Actions with history:")
        print("    ~10.Delete all")
        print("      ~10.1.Delete all by card")
        print("      ~10.2.Delete all by category")
        print("")

        choice = input("Please make a choice: ")
        print()
        if choice == "8.2":
            display = dbs.display_categories()
            if display != 1:
                print()
                op = int(input('Choose category: '))
                dbs.show_withdraws_category(op)

            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "8.1":
            display = dbs.display_cards()
            if display != 1:
                print()
                op = int(input('Choose card: '))
                dbs.show_withdraws_card(op)

            op = input('Wanna continue?: ')
            if op == 'N' or op == 'n':
                break
        elif choice == "8":
            dbs.show_withdraws()
            print()
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


menu()