class Invoice:
    def __init__(self, id, cus_name, cus_phone, time, emp_id, list_dish, payment_method) -> None:
        self.id = id
        self.cus_name = cus_name
        self.cus_phone = cus_phone
        self.emp_id = emp_id
        self.time = time
        self.list_dish = list_dish
        self.payment_method = payment_method
        
        
    def __str__(self):
        return f'[{self.id}, {self.cus_phone}, {self.cus_name}, {self.emp_id}, {self.time} ,{self.list_dish}, {self.payment_mentthod}]'
    
    def __eq__(self, other):
        if type(other) == Invoice:
            return self.id == other.id
        else: raise ValueError(f"'==' not supported between instances of 'Menu' and '{type(other)}'")

    def __lt__(self, other):
        if type(other) == Invoice:
            return self.id < other.id
        else: raise ValueError(f"'==' not supported between instances of 'Menu' and '{type(other)}'")

    def __le__(self, other):
        if type(other) == Invoice:
            return self.id <= other.id
        else: raise ValueError(f"'==' not supported between instances of 'Menu' and '{type(other)}'")

    def __gt__(self, other):
        if type(other) == Invoice:
            return self.id > other.id
        else: raise ValueError(f"'==' not supported between instances of 'Menu' and '{type(other)}'")

    def __ge__(self, other):
        if type(other) == Invoice:
            return self.id >= other.id
        else: raise ValueError(f"'==' not supported between instances of 'Menu' and '{type(other)}'")