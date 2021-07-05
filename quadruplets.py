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