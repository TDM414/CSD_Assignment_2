from util import Print, Input

class Display_Employee:

    @staticmethod
    def display_checkID_employee(Tree_Employee):
        id = int(Input("Enter ID: "))
        return Tree_Employee.check_id(id), id

    @staticmethod
    def display_employee_management():
        Print('='*30)
        Print('Employee Management')
        Print('1. View list employee')
        Print('2. Add employee')
        Print('3. Modify employee')
        Print('4. Delete employee')
        Print('5. Back to main menu')
        return Input('Enter your select (1-5): ')
    
    @staticmethod
    def display_view_employee(Tree_Employee):
        Print('-'*30)
        info = Tree_Employee.employees.inoder()
        max_id = len(str(Tree_Employee.max_id())) if len(str(Tree_Employee.max_id())) > len('id') else len('id')
        max_name = len('name')
        max_position = len('position')
        max_salary = len('salary')
        max_sex = len('sex')
        max_address = len('address')
        max_phone = len('phone number')
        for i in range(len(info)):
            if len(info[i].key.name) > max_name:
                max_name = len(info[i].key.name)
            if len(info[i].key.position) > max_position:
                max_position = len(info[i].key.position)
            if len(info[i].key.salary) > max_salary:
                max_salary = len(info[i].key.salary)
            if len(info[i].key.sex) > max_sex:
                max_sex = len(info[i].key.sex)
            if len(info[i].key.address) > max_address:
                max_address = len(info[i].key.address)
            if len(info[i].key.phone_number) > max_phone:
                max_phone = len(info[i].key.phone_number)

        Print(' '*((max_id - len('id'))//2 + 2) + 'ID' + ' '*((max_id - len('id'))//2 + 2 + (max_id - len('id'))%2) + '|', End ='', time=0.005)
        Print(' '*((max_name - len('name'))//2 + 2) + 'Name' + ' '*((max_name - len('name'))//2 + 2 + (max_name - len('name'))%2) + '|', End ='', time=0.005)
        Print(' '*((max_position - len('position'))//2 + 2) + 'Position' + ' '*((max_position- len('position'))//2 + 2 + (max_position - len('position'))%2) + '|', End ='', time=0.005)
        Print(' '*((max_salary - len('salary'))//2 + 2) + 'Salary' + ' '*((max_salary - len('salary'))//2 + 2 + (max_salary - len('salary'))%2) + '|', End ='', time=0.005)
        Print(' '*((max_sex - len('sex'))//2 + 2) + 'Sex' + ' '*((max_sex - len('sex'))//2 + 2 + (max_sex - len('sex'))%2) + '|', End='', time=0.005)
        Print(' '*((max_address - len('address'))//2 + 2) + 'Address' + ' '*((max_address - len('address'))//2 + 2 + (max_address - len('address'))%2) + '|', End='', time=0.005)
        Print(' '*((max_phone - len('Phone Number'))//2 + 2) + 'Phone Number' + ' '*((max_phone - len('Phone Number'))//2 + 2 + (max_phone - len('Phone Number'))%2) + '|', time=0.005)

        Print('-'*(max_id + 4 + max_name + 4 + max_position + 4 + max_salary + 4 + max_sex + 4 + max_address + 4 + max_phone + 4 + 7), time=0.005)
        for i in range(len(info)):
            Print(' '*2 + str(info[i].key.id) + ' '*(max_id - len(str(info[i].key.id)) + 2) + '|', End='', time=0.005)
            Print(' '*2 + info[i].key.name + ' '*(max_name - len(info[i].key.name) + 2) + '|', End='', time=0.005)
            Print(' '*2 + info[i].key.position + ' '*(max_position - len(info[i].key.position) + 2) + '|', End='', time=0.005)
            Print(' '*2 + info[i].key.salary + ' '*(max_salary - len(info[i].key.salary) + 2) + '|', End='', time=0.005)
            Print(' '*2 + info[i].key.sex + ' '*(max_sex - len(info[i].key.sex) + 2) + '|', End='', time=0.005)
            Print(' '*2 + info[i].key.address + ' '*(max_address - len(info[i].key.address) + 2) + '|', End='', time=0.005)
            Print(' '*2 + info[i].key.phone_number + ' '*(max_phone - len(info[i].key.phone_number) + 2) + '|', time=0.005)

        Input('Press "Enter" to back to Employee Management')
        return '0'
    
    @staticmethod
    def display_add_employee():
        Print('-'*30)
        name = Input('Enter employee name: ')
        position = Input('Enter position: ')
        salary = Input('Enter salary: ')
        sex = Input('Enter sex: ')
        address = Input('Enter address: ')
        phone = Input('Enter phone number: ')
        return '0', name, position, salary, sex, address, phone
    
    @staticmethod
    def display_modify_employee():
        Print('='*30)
        name = None
        position = None
        salary = None
        sex = None
        address = None
        phone_number = None
        slection = Input('What do you want to chantge (Name, Position, Salary, Sex, Address, Phone Number): ').lower()
        if 'name' in slection:
            name = input('Enter new name: ')
        if 'position' in slection:
            position = input('Enter new position: ')
        if 'salary' in slection:
            salary = input('Enter new salary: ')
        if 'description' in slection:
            sex = input('Enter new sex: ')
        if 'description' in slection:
            address = input('Enter new address: ')
        if 'description' in slection:
            phone_number = input('Enter new phone number: ')
        return '0', name, position, salary, sex, address, phone_number
    
    @staticmethod
    def display_delete_employee(Tree_Employee, id):
        Print('='*30)
        selection = Input((f'Are you sure you want to delete "ID: {Tree_Employee.search(id).key.name}" (y/n): '))
        if selection == 'y':
            return True, '0'
        elif selection == 'n':
            return False, '0'
        else:
            return None, '0'