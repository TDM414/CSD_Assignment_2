from util import Print, Input

class Display_Invoice:
    @staticmethod
    def display_checkID_invoice(Tree_Invoice):
        id = int(Input("Enter ID: "))
        return Tree_Invoice.check_id(id), id

    @staticmethod
    def display_invoice_management():
        Print('='*30)
        Print('1. View list invoice')
        Print('2. Add invoice')
        Print('3. Modify invoice')
        Print('4. Delete invoice')
        Print('5. Back to main menu')
        return Input('Enter your select (1-5): ')
    
    @staticmethod
    def display_view_invoice(Tree_Invoice):
        Print('-'*30)
        info = Tree_Invoice.invoice.inoder()
        max_id = len(str(Tree_Invoice.max_id())) if len(str(Tree_Invoice.max_id())) > len('id') else len('id')
        max_cus_name = len('Customer Name')
        max_cus_phone = len("Customer's Phone Number")
        max_emp_id = len(' Employee ID')
        max_time = len('Time')
        max_list_dish = len('List Dish')
        max_payment_method = len('Payment Method')
        for i in range(len(info)):
            if len(info[i].key.cus_name) > max_cus_name:
                max_cus_name = len(info[i].key.cus_name)
            if len(info[i].key.cus_phone) > max_cus_phone:
                max_cus_phone = len(info[i].key.cus_phone)
            if len(info[i].key.emp_id) > max_emp_id:
                max_emp_id = len(info[i].key.emp_id)
            if len(info[i].key.time) > max_time:
                max_time = len(info[i].key.time)
            if len(info[i].key.list_dish) > max_list_dish:
                max_list_dish = len(info[i].key.list_dish)
            if len(info[i].key.payment_method) > max_payment_method:
                max_payment_method = len(info[i].key.payment_method)

        Print(' '*((max_id - len('id'))//2 + 2) + 'ID' + ' '*((max_id - len('id'))//2 + 2 + (max_id - len('id'))%2) + '|', End ='', time = 0.005)
        Print(' '*((max_cus_name - len('Customer Name'))//2 + 2) + 'Customer Name' + ' '*((max_cus_name - len('Customer Name'))//2 + 2 + (max_cus_name - len('Customer Name'))%2) + '|', End ='', time = 0.005)
        Print(' '*((max_cus_phone - len("Customer's Phone Number"))//2 + 2) + "Customer's Phone Number" + ' '*((max_cus_phone- len("Customer's Phone Number"))//2 + 2 + (max_cus_phone - len("Customer's Phone Number"))%2) + '|', End ='', time = 0.005)
        Print(' '*((max_emp_id - len('Employee ID'))//2 + 2) + 'Employee ID' + ' '*((max_emp_id - len('Employee ID'))//2 + 2 + (max_emp_id - len('Employee ID'))%2) + '|', End ='', time = 0.005)
        Print(' '*((max_time - len('Time'))//2 + 2) + 'Time' + ' '*((max_time - len('ETime'))//2 + 2 + (max_time - len('Time'))%2) + '|', End ='', time = 0.005)
        Print(' '*((max_list_dish - len('List Dish'))//2 + 2) + 'List Dish' + ' '*((max_list_dish - len('List Dish'))//2 + 2 + (max_list_dish - len('List Dish'))%2) + '|', End ='', time = 0.005)
        Print(' '*((max_payment_method - len('Payment Method'))//2 + 2) + 'Payment Method' + ' '*((max_payment_method - len('Payment Method'))//2 + 2 + (max_payment_method - len('Payment Method'))%2) + '|', time = 0.005)

        Print('-'*(max_id + 4 + max_cus_name + 4 + max_cus_phone + 4 + max_emp_id + 4 + max_time + 4 + max_list_dish + 4 + max_payment_method + 4 + 5), time = 0.005)
        for i in range(len(info)):
            Print(' '*2 + str(info[i].key.id) + ' '*(max_id - len(str(info[i].key.id)) + 2) + '|', End='', time = 0.005)
            Print(' '*2 + info[i].key.cus_name + ' '*(max_cus_name - len(info[i].key.cus_name) + 2) + '|', End='', time = 0.005)
            Print(' '*2 + info[i].key.cus_phone + ' '*(max_cus_phone - len(info[i].key.cus_phone) + 2) + '|', End='', time = 0.005)
            Print(' '*2 + info[i].key.emp_id + ' '*(max_emp_id - len(info[i].key.emp_id) + 2) + '|', End='', time = 0.005)
            Print(' '*2 + info[i].key.time + ' '*(max_time - len(info[i].key.time) + 2) + '|', End='', time = 0.005)
            Print(' '*2 + info[i].key.list_dish + ' '*(max_list_dish - len(info[i].key.list_dish) + 2) + '|', End='', time = 0.005)
            Print(' '*2 + info[i].key.payment_method + ' '*(max_payment_method - len(info[i].key.payment_method) + 2) + '|', time = 0.005)

        Input('Press "Enter" to back to Menu Managemnet!')
        return '0'

    @staticmethod
    def display_add_invoice():
        cus_name = Input('Enter customer name: ')
        cus_phone = Input("Enter customer's phone number: ")
        emp_id = Input('Enter employee ID: ')
        time = Input('Enter time (yyyy/mm/dd h:mm:ss): ')
        list_dish = Input('Enter list dish: ')
        payment_method = Input('Enter payment method: ')
        return '0', cus_name, cus_phone, emp_id, time, list_dish, payment_method
    
    @staticmethod
    def display_modify_invoice():
        Print('='*30)
        cus_name = None
        cus_phone = None
        emp_id = None
        time = None
        list_dish = None
        payment_method = None
        selection = Input('Customer Name, Customer Phone, Employee ID, Time, List Dish, Payment Method): ').lower()
        if 'customer' in selection and 'name' in selection:
            cus_name = input('Enter customer name: ')
        if 'customer' in selection and 'phone' in selection:
            cus_phone = input('Enter customer phone: ')
        if 'employee' in selection and 'id' in selection:
            emp_id = input('Enter employee ID: ')
        if 'time' in selection:
            time = input('Enter time: ')
        if 'list' in selection and 'dish' in selection:
            list_dish = input('Enter list dish: ')
        if 'payment' in selection and 'method' in selection:
            payment_method = input('Enter payment method: ')
        return '0', cus_name, cus_phone, emp_id, time, list_dish, payment_method

    @staticmethod
    def display_delete_invoice(Tree_Menu, id):
        Print('='*30)
        selection = Input((f'Are you sure you want to delete "{Tree_Menu.search(id).key.id}" (y/n): '))
        if selection == 'y':
            return True, '0'
        elif selection == 'n':
            return False, '0'
        else:
            return None, '0'