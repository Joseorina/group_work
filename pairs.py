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