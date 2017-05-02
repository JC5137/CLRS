def MaximumCrossSubarray(array,start,mid,end):
    left_maxnum = -float('inf')
    sum = 0 
    for k in range(mid,start - 1,-1):
        sum = sum + array[k]
        
        if sum > left_maxnum:
            left_maxnum = sum
            max_left = k
    
    right_maxnum = -float('inf')
    sum = 0
    for k in range(mid + 1,end + 1):
        sum = sum + array[k]
        
        if sum > right_maxnum:
            right_maxnum = sum
            max_right = k
    
    return (max_left,max_right,left_maxnum + right_maxnum)
def MaximumArray(array,start,end):
    if start == end:
        return (start,end,array[start])
    else:
        mid = (start + end) / 2 
        (max_left_start,max_left_end,left_maxnum) = MaximumArray(array,start,mid)
        (max_right_start,max_right_end,right_maxnum) = MaximumArray(array,mid + 1,end)
        (max_cross_srart,max_cross_end,cross_maxnum) = MaximumCrossSubarray(array,start,mid,end)
        if left_maxnum >= right_maxnum and left_maxnum >= cross_maxnum:
            return (max_left_start,max_left_end,left_maxnum)
        elif right_maxnum >= left_maxnum and right_maxnum >= cross_maxnum:
            return (max_right_start,max_right_end,right_maxnum)
        else:
            return (max_cross_srart,max_cross_end,cross_maxnum)


if __name__ == "__main__":            
    array = [-1,-2,3,-4,2,3,-1]
    print MaximumArray(array,0,len(array) - 1)

    
    
        
    