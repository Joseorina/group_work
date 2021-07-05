class Setm:
    
    def __init__(self, set_name):
        self.set_name = list(set_name)

    def create_set(self, element):
        """
        Creates a set        
        Arguments:
            element {[list]} -- creates a list of elements
        """
        self.set_name.append(element)

    def access_elements(self):
        """
        Outputs the set
        """
        set_name = self.set_name
        output_set = []
        for set_item in set_name:
            output_set.append(set_item)
        return output_set

    def add_elements(self, set_name):
        """
        Adds elements to a set
        
        Arguments:
            set_name {[list]} -- adds an element to a set
        
        Returns:
            set -- set of elements including the added element
        """
        self.set_name.add('element')
        return set_name

    def remove_elements(self, set_item):
        """
        Deletes an element from a set
        
        Arguments:
            set_item {list} -- a list of elements
        
        Returns:
            set -- a set not including the removed item
        """
        if set_item in (self.set_name):
            self.set.remove(set_item)
        else:
            raise KeyError("Element not in set")

    #def __len__(self, set_name)
    def length_set(self, set_name):
        """
        Function returns the length of set
        
        Arguments:
            set_name {list} -- a list of elements
        """
        return len(self.set_item)

    def compare_set(self, set_name, set2_name):
        # if set_name <= set2_name:
        #     print("The sets are equal")
        # else:
        #     print("Not equal")
        """
        Compares two sets
        
        Returns:
            list -- returns subset of both items
        """
        sub_set = self.set_name.issubset(set2_name)
        return sub_set
    
    def set_union(self, set_name, set2_name):
        """
        Combines two list items into a single list
        
        Arguments:
            set_name {list}
            set2_name {list}
        
        Returns:
            list -- a union of set_name and set2_name
        """
        set1_name = self.set_name
        set_union_var = self.set1_name.union(set2_name)
        return set_union_var

    def set_intersection(self, set2_name):
        """
        Checks whether elements in one set exist in another
        
        Arguments:
            set2_name {list}
        
        Returns:
            [list] -- [description]
        """
        set1_name = self.set_name
        inter_set = []
        for set_item in set1_name:
            if set_item in set1_name:
                inter_set.append(set_item)
            return inter_set

    def set_diff(self, set_name, set2_name):
        """
        Outputs the set with the greater number of elements
        
        Arguments:
            set_name {[list]}
            set2_name {[list]}
        
        Returns:
            [list] -- [returns set diffrence]
        """
        
        var_difference = self.set_name.difference(set2_name)
        return var_difference
