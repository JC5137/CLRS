def CountSort(A,B,k):
    C = [0] * k;
    A_length = len(A)
    for i in range(A_length):
        C[A[i]] = C[A[i]] + 1
        
    for i in range(1,k):
        C[i] = C[i] + C[i - 1]
    for j in range(A_length)[::-1]:
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1

if __name__ = '__main__':        
    array = [2,5,3,0,2,3,0,3,1,2,3,4,5,6,7,1,2,3,4,5]
    B = [0] * len(array)
    CountSort(array,B,max(array) + 1)
    print B