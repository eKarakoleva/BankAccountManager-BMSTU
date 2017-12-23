from datetime import datetime
from tinydb_serialization import Serializer


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


class Operation:
    def __init__(self, arg):
        self.card_id = arg[0]
        self.operation = arg[1]
        self.money = arg[2]
        self.category = arg[3]

    def create_operation(self):
        arr = {'card_id': self.card_id, 'operation': self.operation,
               'money': self.money, 'category': self.category}
        return arr


class Category:
    def __init__(self, arg):
        self.name = arg

    def create_category(self):
        arr = {'name': self.name}
        return arr


class DateTimeSerializer(Serializer):
    OBJ_CLASS = datetime  # The class this serializer handles

    def encode(self, obj):
        return obj.strftime('%Y-%m-%dT%H:%M:%S')

    def decode(self, s):
        return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S')


