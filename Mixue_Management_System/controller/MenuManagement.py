from controller.DataStructure import Tree
from modul import Menu
from util import *

class Menu_Management:
    def __init__(self) -> None:
        self.menu = Tree()
        self.data = r'data\menu.txt'

    def load_data(self):
        with open(self.data, mode='r', encoding='utf8') as f:
            data = f.read()
        if data == '':
            return
        data = str_split(data, '\n')
        for i in range(len(data)):
            data[i] = str_split(data[i], ', ')
        for dish in data:
            self.menu.add(Menu(int(dish[0]), dish[1], dish[2], dish[3], dish[4]))
    
    def search(self, id):
        return self.menu.search(self.menu.root, Menu(id, None, None, None, None))
    
    def check_id(self, id):
        if self.search(id) != None:
            return True
        return False

    def max_id(self):
        if self.menu.root == None:
            return 0
        return self.menu.max_value(self.menu.root).key.id

    def add(self, id, name, price, size, description):
        if Input(f'Are you sure you want to add {name} to the menu? (y/n): ') == 'y':
            self.menu.add(Menu(id, name, price, size, description))
        
    def modify(self, id, name, price, size, description):
        if Input('Are you sure you want to save changes to the menu? (y/n): ') == 'y':
            info = self.search(id).key
            if name != None: info.name = name
            if price != None: info.price = price
            if size != None: info.size = size
            if description != None: info.description = description

    def delete(self, id):
        self.menu.delete_node(self.menu.root, self.search(id).key)
        temp = self.menu.inoder()
        for i in temp:
            if i.key.id > id:
                i.key.id = i.key.id-1 

        Print(f'delete {id} completed!')

    def update_data(self):
        with open(self.data, mode='w', encoding='utf8') as file:
            all_info = self.menu.inoder()
            file.write(f'{all_info[0].key.id}, {all_info[0].key.name}, {all_info[0].key.price}, {all_info[0].key.size}, {all_info[0].key.description}')
            for i in range(1, len(all_info)):
                file.write(f'\n{all_info[i].key.id}, {all_info[i].key.name}, {all_info[i].key.price}, {all_info[i].key.size}, {all_info[i].key.description}')

a = Menu_Management()
a.load_data()