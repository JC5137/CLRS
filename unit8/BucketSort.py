import sys
sys.path.append(r'../') 


from InsertSort import *

def BucketSort(Array):
    n = len(Array)
    B = [[] for i in range(n)] #±‹√‚«≥≤„øΩ±¥
    for i in range(n):
        B[int(n * Array[i])].append(Array[i])
    for i in range(n):
        InsertSort(B[i])
    
    SortedList = []
    for i in range(n):
        if B[i] != []:
            SortedList.extend(B[i])
    return SortedList
array = [0.78,0.17,0.39,0.26,0.72,0.94,0.21,0.12,0.23,0.68]
print BucketSort(array)


