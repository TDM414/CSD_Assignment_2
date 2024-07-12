#=========================LinkedList================================
class List_Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        newNode = List_Node(data)
        if self.head == None:
            self.head = self.tail = newNode
            self.size += 1
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.size += 1

    def delete_index(self, index):
        if index < 0 or index > self.size-1:
            raise IndexError
        elif index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(1, index+1):
                current = current.next
            if current.prev != None:
                current.prev.next = current.next
            if current.next != None:
                current.next.prev = current.prev
            self.size -= 1

    def delete_data(self, data):
        if self.head == None:
            raise IndexError
        else:
            current = self.head
            while current != None:
                if current.data == data:
                    if current.prev != None:
                        current.prev.next = current.next
                    if current.next != None:
                        current.next.prev = current.prev
                    return
                else: current = current.next

    def check_item(self, item):
        current = self.head
        while current != None:
            if current.data == item:
                return True
            current = current.next
        return False

    def is_empty(self):
        if self.head == None and self.tail == None:
            return True
        False
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.head == None:
            # print('linked list is empty')
            return '[]'
        add_str  = lambda data: f"'{data}'" if type(data) == str else f'{data}'
        Str = f'[{add_str(self.head.data)}'
        current = self.head.next
        while current != None:
            Str += f', {add_str(current.data)}'
            current = current.next
        Str += ']'
        return Str
    
    def __iter__(self):
        current = self.head
        while True:
            if current == None:
                return
            yield current.data
            current = current.next

    def __getitem__(self, index):
        current = self.head
        if index < 0:
            raise IndexError(f'linkedList.__getitem__: index out of range')
        elif index == 0:
            return current.data
        else:
            for _ in range(1, index+1):
                if current == None:
                    raise IndexError(f'linkedList.__getitem__: index out of range')
                current = current.next
            return current.data
        
    def __setitem__(self, index, value):
        current = self.head
        if index < 0:
            raise IndexError(f'linkedList.__getitem__: index out of range')
        elif index == 0:
            current.data =  value
        else:
            for _ in range(1, index+1):
                if current == None:
                    raise IndexError(f'linkedList.__getitem__: index out of range')
                current = current.next
            current.data = value
        return self.head
    
    def pop(self):
        temp = self.head
        self.head = self.head.next
        return temp
    
#====================================================================

#==========================Queue=====================================
class Queue_Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
    
    def add(self, data):
        new_Node = Queue_Node(data)
        if self.front == None and self.rear == None:
            self.front = self.rear = new_Node
        else:
            self.rear.next = new_Node
            new_Node.prev = self.rear
            self.rear = new_Node

    def pop(self):
        if self.front == None:
            return ''
        elif self.front == self.rear:
            temp = self.front
            self.front = self.rear = None
            return temp
        temp = self.front
        self.front = self.front.next
        return temp.data
    
    def is_empty(self):
        if self.front == None and self.rear == None:
            return True
        return False

    def __str__(self):
        if self.front == None:
            return ''
        Str = f'[{self.front.data}'
        current = self.front.next
        while current.next != None:
            Str += f', {current.data}'
            current = current.next
        Str += f', {self.rear.data}]'
        return Str

    def __iter__(self):
        current = self.front
        while current != None:
            yield current.data
            current = current.next                  
#====================================================================

#==============================Stack=================================
class Stack_Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
    
    def push(self, data):
        newNode = Stack_Node(data)
        if self.top == None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode

    def pop(self):
        if self.top == None:
            raise LookupError
        else:
            temp = self.top
            self.top = self.top.next 
            return temp.data
    
    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def __str__(self):
        Str = ''
        current = self.top
        while current != None:
            Str += f'{current.data} '
            current = current.next
        return Str
    
    def check_item(self, item):
        current = self.top
        while current != None:
            if current.data == item:
                return True
            current = current.next
        return False
    
    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False
#====================================================================

#============================Tree====================================

class Tree_Node:
    def __init__(self, Key) -> None:
        self.key = Key
        self.right = None
        self.left = None

class Tree:
    def __init__(self) -> None:
        self.root = None
#====================================================================
#--------------------------Traversal Order---------------------------
    def lv_order(self):
        list_data = LinkedList()
        list_data.append(self.root)
        for node in list_data:
            if node.left != None:
                list_data.append(node.left)
            if node.right != None:
                list_data.append(node.right)
        return list_data

    def preoder(self):
        node_stack = Stack()
        result = LinkedList()
        node_stack.push(self.root)
        while node_stack.is_empty() == False:
            temp = node_stack.pop()
            result.append(temp.key)
            if temp.right != None:
                node_stack.push(temp.right)
            if temp.left != None:
                node_stack.push(temp.left)
        return result

    def recursive_preorder(self, root):
        if root != None:
            print(root.key, end=' ')
            self.recursive_preorder(root.left)
            self.recursive_preorder(root.right)

    def inoder(self):
        if self.root == None:
            return ''
        node_stack = Stack()
        result = LinkedList()
        node_stack.push(self.root)
        while node_stack.is_empty() == False:
            temp = node_stack.peek()
            if temp.left != None:
                if result.check_item(temp.left) == False:
                    node_stack.push(temp.left)
                else:
                    result.append(node_stack.pop())
                    node_stack.push(temp.right) if temp.right != None else 1

            elif temp.left == None:
                result.append(node_stack.pop())
                if temp.right != None:
                    node_stack.push(temp.right)
        return result

    def recursive_inoder(self, root):
        if root != None:
            self.recursive_inoder(root.left)
            print(root.key, end=" "),
            self.recursive_inoder(root.right)

    def postorder(self):
        node_stack = Stack()
        result = LinkedList()
        node_stack.push(self.root)
        while node_stack.is_empty() == False:
            temp = node_stack.peek()
            if temp.left != None and node_stack.check_item(temp.left) == False and result.check_item(temp.left.key) == False:
                node_stack.push(temp.left)
            elif temp.right != None and node_stack.check_item(temp.right) == False and result.check_item(temp.right.key) == False:
                node_stack.push(temp.right)
            else:
                result.append(node_stack.pop().key)
        return result
    
    def recursive_postoder(self, root):
        if root != None:
            self.recursive_postoder(root.left)
            self.recursive_postoder(root.right)
            print(root.key, end=" "),
#----------------------------------------------------------------------------------

#---------------------add------------------
    def add(self, key):
        self.root = self.add_node(self.root, Tree_Node(key))
    
    def add_node(self, root, new_node):
        if root == None:
            return new_node
        elif new_node.key < root.key:
            root.left = self.add_node(root.left, new_node)

        elif new_node.key > root.key:
            root.right = self.add_node(root.right, new_node)
        else:
            raise ValueError
        return self.add_rotation(root)

    def add_rotation(self, root):
        if self.balance(root) == 2 and self.balance(root.left) == 1:
            return self.right_rotation(root)
        elif self.balance(root) == 2 and self.balance(root.left) == -1:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)
        elif self.balance(root) == -2 and self.balance(root.right) == -1:
            return self.left_rotation(root)
        elif self.balance(root) == -2 and self.balance(root.right) == 1:
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)
        else:
            return root

#---------------------del------------------
    def delete(self, key):
        self.root = self.delete_node(self.root, key)

    def delete_node(self, root, key):
        if root == None:
            raise ValueError

        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
        
            root.key = self.max_value(root.left).key
            root.left = self.delete_node(root.left, root.key)
        return self.delete_rotation(root)
    
    def delete_rotation(self, root):
        if self.balance(root) == 2 and self.balance(root.left) >= 0:
            return self.right_rotation(root)
        if self.balance(root) == -2 and self.balance(root.right) <= 0:
            return self.left_rotation(root)
        if self.balance(root) == 2 and self.balance(root.left) < 0:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)
        if self.balance(root) == -2 and self.balance(root.right) > 0:
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)

        return root

    def mini_value(self, root):
        while True:
            if root.left == None: 
                return root
            root = root.left
        
    def max_value(self, root):
        while True:
            if root.right == None:
                return root
            root = root.right

#-----------------suport func---------------
    def get_node(self, key):
        current = self.root
        while current != None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current
        print(f"{key} doesn't exits")

    def __str__(self):
        list_node = self.inoder()
        Str = f'[{list_node[0].key}'
        
        for i in range(1, len(list_node)):
            Str += f'\n{list_node[i].key}'
        Str += ']'
        return Str

    def search(self, root, key):
        if root == None:
            return None
        elif key == root.key:
            return root
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

#------------------AVL-----------------------
    def height(self, root):
        if root == None:
            return -1
        return max(self.height(root.left), self.height(root.right)) + 1
    
    def balance(self, root):
        if root == None:
            return float('inf')
        return self.height(root.left) - self.height(root.right)
    
    def right_rotation(self, root):
        temp = root.left.right
        new_root = root.left
        new_root.right = root
        root.left = temp
        return new_root
    
    def left_rotation(self, root):
        temp = root.right.left
        new_root = root.right
        new_root.left = root
        root.right = temp
        return new_root
#====================================================================
