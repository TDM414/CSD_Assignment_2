from util import Print, Input

class Display_Main():
    @staticmethod
    def display_main():
        Print('='*30)
        Print('1) Menu Management')
        Print('2) Employee Management')
        Print('3) Customer Management')
        Print('4) Invoice Management')
        Print('5) Close program')
        return Input('Enter your select (1-5): ')
    

