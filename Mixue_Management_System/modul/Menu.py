class Menu:
    def __init__(self, id, name, price, size, description) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.size = size
        self.description = description
        
    def __str__(self):
        return f'[{self.id}, {self.name}, {self.price}, {self.size}, {self.description}]'
    
    def __eq__(self, other):
        if type(other) == Menu:
            return self.id == other.id
        else: raise ValueError(f"'==' not supported between instances of 'Menu' and '{type(other)}'")

    def __lt__(self, other):
        if type(other) == Menu:
            return self.id < other.id
        else: raise ValueError(f"'==' not supported between instances of 'Menu' and '{type(other)}'")

    def __le__(self, other):
        if type(other) == Menu:
            return self.id <= other.id
        else: raise ValueError(f"'==' not supported between instances of 'Menu' and '{type(other)}'")

    def __gt__(self, other):
        if type(other) == Menu:
            return self.id > other.id
        else: raise ValueError(f"'==' not supported between instances of 'Menu' and '{type(other)}'")

    def __ge__(self, other):
        if type(other) == Menu:
            return self.id >= other.id
        else: raise ValueError(f"'==' not supported between instances of 'Menu' and '{type(other)}'")