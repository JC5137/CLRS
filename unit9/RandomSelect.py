import sys
sys.path.append(r'../unit7') 

from QuickSort import *

def RandomSelect(Array,p,r,i):
    if p == r:
        return Array[p]
    q = RandomPartition(Array,p,r)
    
    k = q - p + 1
    if k == i:
        return Array[q]
    elif i < k:
        return RandomSelect(Array,p,q - 1,i)
    else:
        return RandomSelect(Array,q + 1,r,i - k)

array = [2,8,7,1,3,5,6,4]  #[1 2 3 4 5 6 7 8]
print RandomSelect(array,0,len(array) - 1,8)