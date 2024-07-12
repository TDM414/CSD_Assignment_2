from controller.DataStructure import Tree
from modul import Customer
from util import *


class Customer_Management():
    def __init__(self) -> None:
        self.customers = Tree()
        self.data = r'data\customers.txt'
    
    def load_data(self):
        with open(self.data, mode='r', encoding='utf8') as f:
            data = f.read()
        if data == '':
            return
       
        data = str_split(data, '\n')
        for i in range(len(data)):
            data[i] = str_split(data[i], ', ')
        
        for customer in data:
            self.customers.add(Customer(customer[0], customer[1]))

    def show(self):
        info = self.customers.inoder()
        max_phone = len('Phone Number')
        max_name = len('name')
        # max_history = len('order history (invoice ID)')

        for i in range(len(info)):
            if len(info[i].key.phone_number) > max_phone:
                max_phone = len(info[i].key.phone_number)
            if len(info[i].key.name) > max_name:
                max_name = len(info[i].key.name)
            # if len(str(info[i].key.history)) > max_history:
            #     max_history = len(str(info[i].key.history))

        print(' '*((max_phone - len('Phone Number'))//2 + 2) + 'Phone Number' + ' '*((max_phone - len('Phone Number'))//2 + 2 + (max_phone - len('Phone Number'))%2) + '|', end='')
        print(' '*((max_name - len('name'))//2 + 2) + 'Name' + ' '*((max_name - len('name'))//2 + 2 + (max_name - len('name'))%2) + '|')
        # print(' '*((max_history - len('Order history (invoice ID)'))//2 + 2) + 'Order History (Invoice ID)' + ' '*((max_history- len('Order History (invoice ID)'))//2 + 2 + (max_history - len('Order history'))%2) + '|')
        print('-'*( max_phone + 4 + max_name + 4 + 3))
        for i in range(len(info)):
            print(' '*2 + info[i].key.phone_number + ' '*(max_phone - len(info[i].key.phone_number) + 2) + '|', end='')
            print(' '*2 + info[i].key.name + ' '*(max_name - len(info[i].key.name) + 2) + '|')
            # print(' '*2 + str(info[i].key.history) + ' '*(max_history - len(str(info[i].key.history)) + 2) + '|')

    def search(self, phone_number):
        return self.customers.search(self.customers.root, Customer(phone_number, None))
    
    def add(self, phone_number, name):
        self.customers.add(Customer(phone_number, name))

    def update_data(self):
        with open(self.data, mode='w', encoding='utf8') as file:
            all_info = self.customers.inoder()
            file.write(f'{all_info[0].key.phone_number}, {all_info[0].key.name}')
            for i in range(1, len(all_info)):
                file.write(f'\n{all_info[i].key.phone_number}, {all_info[i].key.name}')
