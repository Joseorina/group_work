import sys

def find_smallest_differences(A, B, m, n):
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