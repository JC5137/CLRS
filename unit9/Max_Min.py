def Max_Min(Array,n):
    if n % 2 == 0:
        max = Array[1] if Array[1] > Array[0] else Array[0]
        min = Array[1] if Array[1] < Array[0] else Array[0]
        index = 2
    else:
        max = min = Array[0]
        index = 1
    
    for i in range(index,n,2):
        if Array[i] > Array[i + 1]:
            max = max if max > Array[i] else Array[i]
            min = min if min < Array[i + 1] else Array[i + 1]
        else:
            max = max if max > Array[i + 1] else Array[i + 1]
            min = min if min < Array[i] else Array[i]
    return (max,min)

Array = [1,4,5,6,7,8,-1,2,3,4,1,-8]
print Max_Min(Array,len(Array))