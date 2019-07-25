import ctypes

class DynamicArray:
    
    def __init__(self):
        """
        creating an empty array
        """
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
        
    def __len__(self):
        """
        Returning number of elements stored in an array
        
        Returns:
            [int] -- [Integer of items]
        """
        return self._n
    
    def __getitem__(self, k):
        """
        Return element at index k
        
        Arguments:
            k {[int]} -- [index position of element k]
        """
        if not 0 <= k < self._n:
            raise IndexError('Invalid index')
        return self._A[k]
    
    def append_array(self, obj):
        """
        Add an object to the end of the array
        
        Arguments:
            obj {[iterable, int, ]} -- [new item]
        """
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1
    
    def _resize(self, c):
        """
        Resize internal arrat to capacity c
        
        Arguments:
            c {[int]} -- [New capacity of array]
        """
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
        
    def _make_array(self, c):
        """
        Return new array with capacity c
        
        Arguments:
            c {[type]} -- [description]
        """
        return (c * ctypes.py_object)()