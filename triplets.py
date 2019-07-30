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
