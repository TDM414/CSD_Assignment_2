from util import Print, Input

class Display_Menu:
    @staticmethod
    def display_checkID_menu(Tree_Menu):
        id = int(Input("Enter ID: "))
        return Tree_Menu.check_id(id), id

    @staticmethod
    def display_menu_management():
        Print('='*30)
        Print('1. View list menu')
        Print('2. Add dish')
        Print('3. Modify dish')
        Print('4. Delete dish')
        Print('5. Back to main menu')
        return Input('Enter your select (1-5): ')
    
    @staticmethod
    def display_view_menu(Tree_Menu):
        Print('='*30)
        info = Tree_Menu.menu.inoder()
        max_id = len(str(Tree_Menu.max_id())) if len(str(Tree_Menu.max_id())) > len('id') else len('id')
        max_name = len('name')
        max_price = len('price')
        max_size = len('size')
        max_description = len('description')
        for i in range(len(info)):
            if len(info[i].key.name) > max_name:
                max_name = len(info[i].key.name)
            if len(info[i].key.price) > max_price:
                max_price = len(info[i].key.price)
            if len(info[i].key.size) > max_size:
                max_size = len(info[i].key.size)
            if len(info[i].key.description) > max_description:
                max_description = len(info[i].key.description)

        Print(' '*((max_id - len('id'))//2 + 2) + 'ID' + ' '*((max_id - len('id'))//2 + 2 + (max_id - len('id'))%2) + '|', End ='', time=0.005)
        Print(' '*((max_name - len('name'))//2 + 2) + 'Name' + ' '*((max_name - len('name'))//2 + 2 + (max_name - len('name'))%2) + '|', End ='', time=0.005)
        Print(' '*((max_price - len('price'))//2 + 2) + 'Price' + ' '*((max_price- len('price'))//2 + 2 + (max_price - len('price'))%2) + '|', End ='', time=0.005)
        Print(' '*((max_size - len('size'))//2 + 2) + 'Size' + ' '*((max_size - len('size'))//2 + 2 + (max_size - len('size'))%2) + '|', End ='', time=0.005)
        Print(' '*((max_description - len('description'))//2 + 2) + 'Description' + ' '*((max_description - len('description'))//2 + 2 + (max_description - len('description'))%2) + '|', time=0.005)

        Print('-'*(max_id + 4 + max_name + 4 + max_price + 4 + max_size + 4 + max_description + 4 + 5), time=0.005)
        for i in range(len(info)):
            Print(' '*2 + str(info[i].key.id) + ' '*(max_id - len(str(info[i].key.id)) + 2) + '|', End='', time=0.005)
            Print(' '*2 + info[i].key.name + ' '*(max_name - len(info[i].key.name) + 2) + '|', End='', time=0.005)
            Print(' '*2 + info[i].key.price + ' '*(max_price - len(info[i].key.price) + 2) + '|', End='', time=0.005)
            Print(' '*2 + info[i].key.size + ' '*(max_size - len(info[i].key.size) + 2) + '|', End='', time=0.005)
            Print(' '*2 + info[i].key.description + ' '*(max_description - len(info[i].key.description) + 2) + '|', time=0.005)

        Input('Press "Enter" to back to Menu Managemnet!')
        return '0'

    @staticmethod
    def display_add_menu():
        Print('='*30)
        name = Input('Enter dish name: ')
        price = Input('Enter price: ')
        size = Input('Enter size: ')
        description = Input('Enter description (press Enter to skip "Description"): ')
        return '0', name, price, size, description if description != '' else None
    
    @staticmethod
    def display_modify_menu():
        Print('='*30)
        new_name = None
        new_price = None
        new_size = None
        new_description = None
        slection = Input('What do you want to chantge (Name, Price, Size, description): ').lower()
        if 'name' in slection:
            new_name = input('Enter new name: ')
        if 'price' in slection:
            new_price = input('Enter new price: ')
        if 'size' in slection:
            new_size = input('Enter new size: ')
        if 'description' in slection:
            new_description = input('Enter new desctiprion: ')
        return '0', new_name, new_price, new_size, new_description

    @staticmethod
    def display_delete_menu(Tree_Menu, id):
        Print('='*30)
        selection = Input((f'Are you sure you want to delete "{Tree_Menu.search(id).key.name}" (y/n): '))
        if selection == 'y':
            return True, '0'
        elif selection == 'n':
            return False, '0'
        else:
            return None, '0'