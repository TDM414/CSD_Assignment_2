from controller.DataStructure import Tree
from modul import Employee
from util import *

class Employee_Management:
    def __init__(self) -> None:
        self.employees = Tree()
        self.data = r'data\employees.txt'

    def load_data(self):
        with open(self.data, mode='r', encoding='utf8') as f:
            data = f.read()
        if data == '':
            return
        data = str_split(data, '\n')
        for i in range(len(data)):
            data[i] = str_split(data[i], ', ')

        for employee in data:
            self.employees.add(Employee(int(employee[0]), employee[1], employee[2], employee[3], employee[4], employee[5], employee[6]))
    
    def search(self, id):
        return self.employees.search(self.employees.root, Employee(id, None, None, None, None, None, None))
    
    def check_id(self, id):
        if self.search(id) != None:
            return True
        return False

    def max_id(self):
        if self.employees.root == None:
            return 0
        return self.employees.max_value(self.employees.root).key.id

    def add(self, id, name, position, salary, sex, address, phone_number):
        if Input(f'Are you sure you want to add {name} to the menu? (y/n): ') == 'y':
            self.employees.add(Employee(id, name, position, salary, sex, address, phone_number))

    def modify(self, id, name, position, salary, sex, address, phone_number):
        if Input('Are you sure you want to save changes to the menu? (y/n): ') == 'y':
            info = self.search(id).key
            if name != None: info.name = name
            if position != None: info.position = position
            if salary != None: info.salary = salary
            if sex != None: info.sex = sex
            if address != None: info.address = address
            if phone_number != None: info.phone_number = phone_number

    def delete(self, id):
        self.employees.delete_node(self.employees.root, self.search(id).key)
        temp = self.employees.inoder()
        for i in temp:
            if i.key.id > id:
                i.key.id = i.key.id-1 
        print(f'{id} does not exists!')

    def update_data(self):
        with open(self.data, mode='w', encoding='utf8') as file:
            all_info = self.employees.inoder()
            file.write(f'{all_info[0].key.id}, {all_info[0].key.name}, {all_info[0].key.position}, {all_info[0].key.salary}, {all_info[0].key.sex}, {all_info[0].key.address}, {all_info[0].key.phone_number}')
            for i in range(1, len(all_info)):
                file.write(f'\n{all_info[0].key.id}, {all_info[0].key.name}, {all_info[0].key.position}, {all_info[0].key.salary}, {all_info[0].key.sex}, {all_info[0].key.address}, {all_info[0].key.phone_number}')

    def test(self):
        return self.employees.__str__()
