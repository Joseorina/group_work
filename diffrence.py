import sys

def find_smallest_differences(A, B, m, n):
    """
    Find the smallest diffrence given two arrays
    
    Arguments:
        A {[int]} -- [array of integer values]
        B {[int]} -- [array of integer values]
        m {[int]} -- [length of array A]
        n {[int]} -- [length of array B]
    
    Returns:
        [result] -- [smallest diffrence of array]
    Runtime:
        [O(n2)]
    """
    A.sort()
    B.sort()
    
    a = 0
    b = 0
    
    result = sys.maxsize
    
    while(a < m and b < n):
        if (abs(A[a] - B[b]) < result):
            result = abs(A[a] - B[b])
            
        if (A[a] < B[b]):
            a += 1
                
        else:
            b += 1
    return result        
    
A = [-1, 5, 10, 20, 28, 3]
B = [26, 134, 135, 15, 17]
m = len(A)
n = len(B)
print(find_smallest_differences(A, B, m, n))