
def find_triplets(A, result, r):
    """
    Find 3 integers that add up to a specified sum
    
    Arguments:
        A {[int]} -- [Array of integers]
        result {[int]} -- [expected sum of triplets]
        r {[int]} -- [length of array]
    """
    for i in range(len(A)-2):
        l = i + 1
        while (l < r):
            _sum = A[i] + A[l] + A[r]
            if (_sum < 0):
                l += 1
            if (_sum > 0):
                r -= 1
            if not _sum:
                result.append([A[i], A[l], A[r]])
                l += 1
                
A = [12, 3, 1, 2, -6, 5, -8, 6]
result = []
A.sort()
r = len(A) - 1
print(find_triplets(A, result, r))