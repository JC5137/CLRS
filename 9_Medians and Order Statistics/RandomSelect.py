import sys
sys.path.append(r'../7_Quicksort') 
from QuickSort import *
sys.path.append(r'../')
from InsertSort import *


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

        
if __name__ == '__main__':
    array = [2,8,7,1,3,5,6,4,9,10,11,12,13,14,15]  #[1 2 3 4 5 6 7 8 9 10]
    print RandomSelect(array,0,len(array) - 1,(len(array) + 1) / 2)
    print SelectDriver(array,len(array))