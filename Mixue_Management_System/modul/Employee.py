class Employee:
    def __init__(self, id, name, position, salary, sex, address, phone_number) -> None:
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.sex = sex
        self.address = address
        self.phone_number = phone_number
 
    def __str__(self):
        return f'[{self.id}, {self.name}, {self.position}, {self.salary}, {self.sex}, , {self.address}, {self.phone_number}]'
    
    def __eq__(self, other):
        if type(other) == Employee:
            return self.id == other.id
        else: raise ValueError(f"'==' not supported between instances of 'Menu' and '{type(other)}'")

    def __lt__(self, other):
        if type(other) == Employee:
            return self.id < other.id
        else: raise ValueError(f"'==' not supported between instances of 'Menu' and '{type(other)}'")

    def __le__(self, other):
        if type(other) == Employee:
            return self.id <= other.id
        else: raise ValueError(f"'==' not supported between instances of 'Menu' and '{type(other)}'")

    def __gt__(self, other):
        if type(other) == Employee:
            return self.id > other.id
        else: raise ValueError(f"'==' not supported between instances of 'Menu' and '{type(other)}'")

    def __ge__(self, other):
        if type(other) == Employee:
            return self.id >= other.id
        else: raise ValueError(f"'==' not supported between instances of 'Menu' and '{type(other)}'")