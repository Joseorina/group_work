class Map(dict):
    
    def __init__(self):
        pass
    
    def __setitem__(self, key, item):
        self.__dict__[key] = item
        
    def __getitem__(self, key):
        return self.__dict__[key]
    
    def __len__(self):
        return len(self.__dict__)
    
    def __delitem__(self, key):
        del self.__dict__[key]
    
    def clear(self):
        return self.__dict__.clear()
    
    def copy(self):
        return self.__dict__.copy()
    
    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def __keys__(self):
        return self.__dict__.keys()
    
    def values(self):
        return self.__dict__.values()
    
    def items(self):
        return self.__dict__.items()
    
    def __cmp__(self, dict_):
        return self.__cmp__(self.__dict__, dict_)
    
    def __contains__(self, item):
        return item in self.__dict__
    
    def __iter__(self):
        return iter(self.__dict__)