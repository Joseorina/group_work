def find_quadruplets(A, n, X):
    for i in range(0, n-3):
        for j in range(i+1, n-2):
            for k in range (j+1, n-1):
                for l in range (k+1, n):
                    if A[i] + A[j] + A[k] + A[l] == X:
                        print ("{}, {}, {}, {}".format(A[i], A[j], A[k], A[l]))

A = [7, 6, 4, -1, 1, 2]
n = len(A)
X = 0
print(find_quadruplets(A, n, X))