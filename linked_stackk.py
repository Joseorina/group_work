class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedStack:
    def __init__(self):
        self.head = None
    
    def __len__(self):
        pass
    
    def is_empty(self):
        pass
    
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    
    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped
        
_stack = LinkedStack()
while True:
    print('push <value>')
    print('pop')
    print('quit')
    do = input('what would you like to do? ').split()
    
    operation = do[0].strip().lower()
    if operation == 'push':
        _stack.push(int(do[1]))
    elif operation == 'pop':
        popped = _stack.pop()
        if popped is None:
            print('Stack is empty')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break