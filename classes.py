class Card:

    def __init__(self, arg):
        self.name = arg[0]
        self.number = arg[1]
        self.balance = arg[2]
        self.bank = arg[3]

    def displayCard(self):
        print("Name : ", self.name, ", Bank: ", self.bank)

    def add_card(self):
        arr = {'name': self.name, 'number': self.number, 'bank': self.bank, 'balance': self.balance}
        return arr


