from config import *

# __init__
Controll_Menu = Menu_Management()
Controll_Menu.load_data()
Controll_Employee = Employee_Management()
Controll_Employee.load_data()
Controll__Customer = Customer_Management()
Controll__Customer.load_data()
Controll_Invoice = Invoice_Managerment()
Controll_Invoice.load_data()

View_Main = Display_Main()
View_Menu = Display_Menu()
View_Employee = Display_Employee()
View_Customer = Display_Customer()
View_Invoice = Display_Invoice()

#__maim_loop__
if __name__ == '__main__':
    main_selection = '0'
    menu_selection = '0'
    emp_selection = '0'
    cus_selection = '0'
    invoice_selection = '0'
    while True:
        if main_selection == '0':
            main_selection = View_Main.display_main()
        
        elif main_selection == '1':
            
            if menu_selection == '0':
                menu_selection = View_Menu.display_menu_management()
            
            elif menu_selection == '1':
                menu_selection = View_Menu.display_view_menu(Controll_Menu)
            
            elif menu_selection == '2':
                id = Controll_Menu.max_id() + 1
                menu_selection, name, price, size, description = View_Menu.display_add_menu()
                Controll_Menu.add(id, name, price, size, description)
                Controll_Menu.update_data()

            elif menu_selection == '3':
                check_id, id = View_Menu.display_checkID_menu(Controll_Menu)
                if check_id == True:
                    menu_selection, name, price, size, description = View_Menu.display_modify_menu()
                    Controll_Menu.modify(id, name, price, size, description)
                    Controll_Menu.update_data()

            elif menu_selection == '4':
                check_id, id = View_Menu.display_checkID_menu(Controll_Menu)
                if check_id == True:
                    confirm_del, menu_selection = View_Menu.display_delete_menu(Controll_Menu, id)
                    if confirm_del == True:
                        Controll_Menu.delete(id)
                        Controll_Menu.update_data()
            
            elif menu_selection == '5':
                menu_selection = '0'
                main_selection = '0'
            
            else:
                Print('Invalid selection!')
                menu_selection = '0'
        
        elif main_selection == '2':

            if emp_selection == '0':
                emp_selection = View_Employee.display_employee_management()
            
            elif emp_selection == '1':
                emp_selection = View_Employee.display_view_employee(Controll_Employee)

            elif emp_selection == '2':
                id = Controll_Employee.max_id() + 1
                emp_selection, name, position, salary, sex, address, phone = View_Employee.display_add_employee()
                Controll_Employee.add(id, name, position, salary, sex, address, phone)
                Controll_Employee.update_data()

            elif emp_selection == '3':
                check_id, id = View_Employee.display_checkID_employee(Controll_Employee)
                if check_id == True:
                    emp_selection, name, position, salary, sex, address, phone_number = View_Employee.display_modify_menu()
                    Controll_Employee.modify(id, name, position, salary, sex, address, phone_number)
                    Controll_Employee.update_data()

            elif emp_selection == '4':
                check_id, id = View_Employee.display_checkID_employee(Controll_Employee)
                if check_id == True:
                    confirm_del, emp_selection = View_Employee.display_delete_employee(Controll_Employee, id)
                    if confirm_del == True:
                        Controll_Employee.delete(id)
                        Controll_Employee.update_data()

            elif emp_selection == '5':
                emp_selection = '0'
                main_selection = '0'
            
            else:
                Print('Invalid selection!')
                menu_selection = '0'

        elif main_selection == '3':

            if cus_selection == '0':
                cus_selection = View_Customer.display_employee_management()
            
            elif cus_selection == '1':
                cus_selection = View_Customer.display_view_employee(Controll__Customer)
            
            elif cus_selection == '2':
                cus_selection = '0'
                main_selection = '0'
            else:
                cus_selection = '0'

        elif main_selection == '4':
            if invoice_selection == '0':
                invoice_selection = View_Invoice.display_invoice_management()

            elif invoice_selection == '1':
                invoice_selection = View_Invoice.display_view_invoice(Controll_Invoice)

            elif invoice_selection == '2':
                id = Controll_Invoice.max_id() + 1
                invoice_selection, cus_name, cus_phone, emp_id, time, list_dish, payment_method = View_Invoice.display_add_invoice()
                Controll_Invoice.add(id, cus_name, cus_phone, emp_id, time, list_dish, payment_method)
                Controll_Invoice.update_data()

            elif invoice_selection == '3':
                check_id, id = View_Invoice.display_checkID_invoice(Controll_Invoice)
                if check_id == True:
                    invoice_selection, cus_name, cus_phone, emp_id, time, list_dish, payment_method = View_Invoice.display_modify_invoice()
                    Controll_Invoice.modify(id, cus_name, cus_phone, emp_id, time, list_dish, payment_method)
                    Controll_Invoice.update_data()

            elif invoice_selection == '4':
                check_id, id = View_Invoice.display_checkID_invoice(Controll_Invoice)
                if check_id == True:
                    confirm_del, invoice_selection = View_Invoice.display_delete_invoice(Controll_Invoice, id)
                    if confirm_del == True:
                        Controll_Invoice.delete(id)
                        Controll_Invoice.update_data()
            
            elif invoice_selection == '5':
                invoice_selection = '0'
                main_selection = '0'
            else:
                invoice_selection = '0'
        elif main_selection == '5':
            break
        else:
            Print('Invalid selection!')
            main_selection = '0'
