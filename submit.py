############################################
def find_triplets(A, n, sum):
    """
    Function to find 3 integers whose sum results to a 0 value
    
    Arguments:
        A {[int]} -- [list of integers]
        n {[int]} -- [lenth of array]
        sum {[int]} -- [sum of numbers]
    Runtime:
        O(n2)
    """
    A.sort()
    for i in range(0, n-1):
        l = i+1
        r = n-1
        x = A[i]
        
        while(l < r):
            if (x + A[l] +A[r] ==  sum):
                print(x, A[l], A[r])
                l = l +1
                r = r -1
            elif (x + A[l] + A[r] < sum):
                l = l + 1
            else:
                r = r -1

arr = [12, 3, 1, 2, -6, 5, -8, 6]
sum = 0
n = len(arr)
find_triplets(arr, n, sum) 

############################################
def find_quadruplets(A, n, X):
    """
    FInd four pairs of integers that sum up to a target sum(0)
    
    Arguments:
        A {[int]} -- [array of integers]
        n {[int]} -- [length of array A]
        X {[int]} -- [target of addition]
    Runtime:
        [O(n)4]
    """
    for i in range(0, n-3):
        for j in range(i+1, n-2):
            for k in range (j+1, n-1):
                for l in range (k+1, n):
                    if A[i] + A[j] + A[k] + A[l] == X:
                        print ("{}, {}, {}, {}".format(A[i], A[j], A[k], A[l]))

A = [7, 6, 4, -1, 1, 2]
n = len(A)
X = 16
print(find_quadruplets(A, n, X))
############################################

A = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10

def two_sum(A, target):
    """
    Finds two numbers which when summed up results to a target of 10
    
    Arguments:
        A {[Array of numbers]} -- []
        target {[Tareget sum]} -- []
    
    Returns:
        [Boolean] -- [True or False]
    Runtime:
        [O(n)]
    """
    x = 0
    y = len(A) -1
    
    while x <= y:
        if A[x] + A[y] == target:
            print(A[x], A[y])
            return True
        elif A[x] + A[y] < target:
            x += 1
        else:
            y -= 1
    return False
print(two_sum(A, target))

######################################
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
