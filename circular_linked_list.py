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
        
    def to_string(self):
        return "Node value: " + str(self.data)
    
class CircularLinkedList(object):
    
    def __init__(self, r=None):
        self.root = r
        self.size = 0
        
    def get_size(self):
        return self.size
    
    def add(self, d):
        if self.get_size() == 0:
            self.root = Node(d)
            self.root.set_next(self.root)
        else:
            new_node = Node(d, self.root.get_next())
            self.root.set_next(new_node)
        self.size += 1
        
    def remove(self, d):
        this_node = self.root
        prev_node = None
        
        while True:
            if this_node.get_data() == d:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    while this_node.get_next != self.root:
                        this_node = this_node.get_next()
                    this_node.set_next(self.root.get_next())
                    self.root = self.root.get_next()
                self.size -=1
            elif this_node.get_next() == self.root:
                return False
            prev_node = this_node
            this_node = this_node.get_next()
            
    def find(self, d):
        this_node = self.root
        while True:
            if this_node.get_data() == d:
                return d
            elif this_node.get_next() == self.root:
                return False
            this_node = this_node.get_next()
            
    def print_list(self):
        print('Print List................')
        if self.root is None:
            return
        this_node = self.root
        print(this_node.to_string())
        while this_node.get_next() != self.root:
            this_node = this_node.get_next()
            print(this_node.to_string())
                
def main():
    myList = CircularLinkedList()
    myList.add(5)
    myList.add(7)
    myList.add(3)
    myList.add(8)
    myList.add(9)
    print("Find 8", myList.find(8))
    print("Find 12", myList.find(12))
    cur = myList.root
    print (cur.to_string())
    for i in range(8):
    	cur = cur.get_next();
    	print (cur.to_string())

    print("size="+str(myList.get_size()))
    myList.print_list()
    myList.remove(8)
    print("size="+str(myList.get_size()))
    print("Remove 15", myList.remove(15))
    print("size="+str(myList.get_size()))
    myList.remove(5)	# delete root node
    myList.print_list()

main()
            
        
    