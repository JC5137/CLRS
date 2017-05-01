A = [3,5,7,8,9,12,15,17,21,33,45]

def BinarySearchRecursive(array,start,end,element):
    if start >=0 and end >= 0 and start <= end:
        middle = start + (end - start) / 2
        if array[middle] == element:
            return start + middle
        elif array[middle] < element:
            return BinarySearchRecursive(array,middle + 1,end,element)
        elif array[middle] > element:
            return BinarySearchRecursive(array,start,middle - 1,element)
def BinarySearchLoop(array,start,end,element):
    print start,end
    print (end - start) / 2
    while start >=0 and end >= 0 and start <= end:
        middle = start + (end - start) / 2
        if array[middle] == element:
            return middle
        elif array[middle] > element:
            end = middle - 1
        elif array[middle] < element:
            start = middle + 1
            
            
print BinarySearchRecursive(A,0,len(A) - 1,15)
