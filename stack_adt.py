class StackAdt:
    
    def __init__(self):
        """
        Initializing of an empty stack using an empty list data structure
        Runtme:
            O(n)
        """
        self.mystack = []
    
    def check_if_empty(self):
        """
        Check whether the stack is empty
        
        Returns:
            [list] -- [empty list]
        Runtime:
                O(n)
        """
        return self.mystack == []
    
    def len_stack(self):
        """
        Returns the length of a stack(list)
        
        Returns:
            [int] -- [length of the stack]
        Runtime:
                O(1)
        """
        return len(self.mystack)
    
    def add_items(self, data):
        """
        Add elements to a stack
        
        Arguments:
            data {[int, str]} -- [datta items to be added to stack]
        
        Returns:
            [int, str] -- [description]
        Runtime:
                O(1)
        """
        return self.mystack.append(data)
        
    def pop_item(self, data):
        """
        Returns top most element of the stack
        
        Arguments:
            data {[]} -- [description]
        
        Raises:
            Exception: [Exception raised incase the stack is empty]
        
        Returns:
            [int,str] -- [description]
        Runtime:   
                O(1)
        """
        if self.mystack == []:
            raise Exception("Stack is empty")
        else:
            return self.mystack.pop(data)
    
    def peeking_items(self):
        """
        Views top most item of the stack but does not remove the item 
        
        Raises:
            Exception: [Exception raised in the case of the stack being empty]
        
        Returns:
            [int, str] -- [Top most data item in the stack]
        Runtime:
                O(1)    
        """
        if self.mystack == []:
            raise Exception("Stack is empty")
        else:
            return self.mystack[-1]
   
    def push_item(self, data):
        """
        Add elements to a stack
        
        Arguments:
            data {[int, str]} -- [datta items to be added to stack]
        
        Returns:
            [int, str] -- [description]
        Runtime:
                O(1)
        """
        return self.mystack.append(data)