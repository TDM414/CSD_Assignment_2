from util import Print, Input

class Display_Customer:

    @staticmethod
    def display_checkID_Customer(Tree_Customer):
        id = int(Input("Enter ID: "))
        return Tree_Customer.check_id(id), id

    @staticmethod
    def display_employee_management():
        Print('='*30)
        Print('Customer Management')
        Print('1. View list customer')
        Print('2. Back to main menu')
        return Input('Enter your select (1-2): ')
    
    @staticmethod
    def display_view_employee(Tree_Customer):
        info = Tree_Customer.customers.inoder()
        max_phone = len('Phone Number')
        max_name = len('name')

        for i in range(len(info)):
            if len(info[i].key.phone_number) > max_phone:
                max_phone = len(info[i].key.phone_number)
            if len(info[i].key.name) > max_name:
                max_name = len(info[i].key.name)

        Print(' '*((max_phone - len('Phone Number'))//2 + 2) + 'Phone Number' + ' '*((max_phone - len('Phone Number'))//2 + 2 + (max_phone - len('Phone Number'))%2) + '|', end='')
        Print(' '*((max_name - len('name'))//2 + 2) + 'Name' + ' '*((max_name - len('name'))//2 + 2 + (max_name - len('name'))%2) + '|')
        Print('-'*( max_phone + 4 + max_name + 4 + 3))
        for i in range(len(info)):
            Print(' '*2 + info[i].key.phone_number + ' '*(max_phone - len(info[i].key.phone_number) + 2) + '|', end='')
            Print(' '*2 + info[i].key.name + ' '*(max_name - len(info[i].key.name) + 2) + '|')
        Input('Press "Enter" to back to Employee Management')
        return '0'


    
