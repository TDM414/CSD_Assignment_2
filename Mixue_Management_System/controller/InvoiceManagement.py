from controller.DataStructure import Tree
from modul import Invoice
from util import *

class Invoice_Managerment:
    def __init__(self) -> None:
        self.invoice = Tree()
        self.data = r'data\invoice.txt'

    def load_data(self):
        with open(self.data, mode='r', encoding='utf8') as f:
            data = f.read()
        if data == '':
            return
        data = str_split(data, '\n')
        for i in range(len(data)):
            data[i] = str_split(data[i], ', ')
        for invoice in data:
            self.invoice.add(Invoice(int(invoice[0]), invoice[1], invoice[2], invoice[3], invoice[4], invoice[5], invoice[6]))
    
    def search(self, id):
        return self.invoice.search(self.invoice.root, Invoice(id, None, None, None, None, None, None))
    
    def check_id(self, id):
        if self.search(id) != None:
            return True
        return False

    def max_id(self):
        if self.invoice.root == None:
            return 0
        return self.invoice.max_value(self.invoice.root).key.id

    def add(self, id, time, emp_id, cus_phone, cus_cus_name, list_dish, payment_method):
        if Input(f'Are you sure you want to add {id} to the menu? (y/n): ') == 'y':
            self.invoice.add(Invoice(id, time, emp_id, cus_phone, cus_cus_name, list_dish, payment_method))

    def modify(self, id, cus_name, cus_phone, emp_id, time, list_dish, payment_method):
        if Input('Are you sure you want to save changes to the menu? (y/n): ') == 'y':
            info = self.search(id).key
            if cus_name != None: info.cus_name = cus_name
            if cus_phone != None: info.cus_phone = cus_phone
            if emp_id != None: info.emp_id = emp_id
            if time != None: info.time = time
            if list_dish != None: info.list_dish = list_dish
            if payment_method != None: info.payment_method = payment_method
            
    def delete(self, id):
        self.invoice.delete_node(self.invoice.root, self.search(id).key)
        temp = self.invoice.inoder()
        for i in temp:
            if i.key.id > id:
                i.key.id = i.key.id-1 

        Print(f'delete {id} completed!')

    def update_data(self):
        with open(self.data, mode='w', encoding='utf8') as file:
            all_info = self.invoice.inoder()
            file.write(f'{all_info[0].key.id}, {all_info[0].key.cus_name}, {all_info[0].key.cus_phone}, {all_info[0].key.emp_id}, {all_info[0].key.time}, {all_info[0].key.list_dish}, {all_info[0].key.payment_method}')
            for i in range(1, len(all_info)):
                file.write(f'\n{all_info[i].key.id}, {all_info[i].key.cus_name}, {all_info[i].key.cus_phone}, {all_info[i].key.emp_id}, {all_info[i].key.time}, {all_info[i].key.list_dish}, {all_info[i].key.payment_method}')
