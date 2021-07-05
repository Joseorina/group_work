class UnsortedMap(MapBase):
    """
    Map implementation using unorderd list
    
    Arguments:
        MapBase {[type]} -- [description]
    """
    
    def __init__(self):
        """
        create and empy map
        """
        self._table = []
        
    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
            raise KeyError('Key Error: ' + repr(k))
    
    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = v
                return
            #did not matvh for key
            self._table.append()(self._item(k, v))
            
    def __delitem__(self, k):
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
            raise KeyError('Key Error: ' + repr(k))
    
    def __len__(self):
        return len(self._table)
    
    def __iter__(self):
        for item in self._table:
            yield item._key