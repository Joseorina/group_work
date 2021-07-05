class Node(object):
    
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n
        
    def get_next(self):
        """
        Get next node
        
        Returns:
            [list] -- [next node in the linked list]
        """
        return self.next_node
    
    def set_next(self, n):
        """
        Set next node in the linked list
        """
        self.next_node = n
        
    def get_data(self):
        """
        Get data from current node
        
        Returns:
            [list] -- [data in current node]
        """
        return self.data
    
    def set_data(self, d):
        """
        Set data in current node
        """
        self.data = d
        
class LinkedList(object):
    
    def __init__(self, r=None):
        self.root = r
        self.size = 0
        
    def get_size(self):
        return self.size
    
    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1
                
    def remove(self, d):
        this_node = self.root
        prev_node = None
        
        while this_node is not None:
            if this_node.get_data() == d:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True 
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
            
    
    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_next() == d:
                return d
            elif this_node.get_next() == None:
                return False
            else:
                this_node = this_node.get_next()
                
def main():
    myList = LinkedList()
    myList.add(5)
    myList.add(9)
    myList.add(3)
    myList.add(8)
    myList.add(9)
    print("size="+str(myList.get_size()))
    myList.remove(8)
    print("size="+str(myList.get_size()))
    print("Remove 15", myList.remove(15))
    print("size="+str(myList.get_size()))
    print("Find 25", myList.find(25))

main()
    
    