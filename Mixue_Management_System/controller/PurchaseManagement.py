class Puchase_Management:
    @staticmethod
    def customer_buy(list_id_dish, Menu_Tree, Tree_Invoice):
        menu = Menu_Tree.menu.inorder()
        for 