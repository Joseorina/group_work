class LinkedStack:
    """
    Stack ADT implementatiion using a linked list
    """
    
    class Node:
        """
        class for storing a single node
        """
        def __init__(self, element, next):
            self._element = element
            self._next = next
    def __init__(self):
        """
        Creating an empty stack
        
        Runtime:
            O(1)
        """
        self.head = None
        self.size = 0
        
    def __len__(self):
        """
        Return number of items in the stack
        
        Returns:
            [int] -- [Number of items in stack]
        
        Runtime:
            O(1)
        """
        return self.size
    
    def check_empty(self):
        """
        Check if stack is empty
        
        Returns:
            [Boolean] -- [Return True if stack is empty]
        
        Runtime:
            O(1)
        """
        return self.size == 0
    
    def push(self, data):
        """
        Add elements to the top of the stack
        
        Arguments:
            data {[iterable]} -- [New element being added to stack]
        
        Runtime:
            O(n)
        """
        self.head = self.Node(data, self.head)
        self.size += 1
        
    def peek_item(self):
        """
        Return top most element of the stack but not remove the element
        
        Raises:
            Exception: [Raise exception if stack is empty]
        
        Returns:
            [iterable] -- [Iterable on top of the list]
        
        Runtime:
            O(n)
        """
        if self.check_empty():
            raise Exception('Stack is empty')
        return self.head.element
    
    def pop(self):
        """
        Remove and return data item from the top of the stack
        
        Raises:
            Exception: [Raise exception is stack is empty]
        
        Returns:
            [iterable] -- [Iteme removed and returned to stack]
        
        Runtime:
            O(n)
        """
        if self.check_empty():
            raise Exception('Stack is empty')
        answer = self.head.element
        self.head = self.head.next
        self.size = 1
        return answer
    