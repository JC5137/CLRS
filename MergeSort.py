def Merge(A,p,q,r):
    n1 = q - p + 1;
    n2 = r - (q + 1) + 1;
    
    L = [0] * (n1 + 1);
    R = [0] * (n2 + 1);

    
    for i in range(0,n1):
        L[i] = A[p + i]
    for j in range(0,n2):
        R[j] = A[q + 1 + j]
        
    L[n1] = float('inf');
    R[n2] = float('inf');

    i = 0;
    j = 0;
    k = p;
    n = r; #K = (p,r)
    print p,q,r
    while k <= n:
        if L[i] <= R[j]:
            A[k] = L[i];
            i = i + 1    
        else:
            A[k] = R[j];
            j = j + 1
        k = k + 1
    print A
    
def MergeSort(A,p,r):
    if p < r:
        q = (p + r) / 2
        MergeSort(A,p,q)
        MergeSort(A,q + 1,r)
        Merge(A,p,q,r)

if __name__ == "__main__":
    A = [2,3,4,5,1,4,5,7,1,1,2,3,4,5,6,7,8,42,2,32,4,5,67,42,2]
    MergeSort(A,0,len(A) - 1)
    print A