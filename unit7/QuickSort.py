import random
def QuickSort(A,p,r):
    if p < r:
        q = RandomPartition(A,p,r)
        QuickSort(A,p,q - 1)
        QuickSort(A,q + 1,r)

def Partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i = i + 1
            A[i],A[j] = A[j],A[i]
    A[i + 1],A[r] = A[r],A[i + 1]
    return i + 1
def RandomPartition(A,p,r):
    i = random.randint(p,r)
    A[i],A[r] = A[r],A[i]
    return Partition(A,p,r)
    
