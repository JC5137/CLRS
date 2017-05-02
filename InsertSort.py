def InsertSort(array,start,Length):
    for j in range(start + 1,start + Length):
        key = array[j];
        
        i = j - 1;
        while i >= start and array[i] > key:
            array[i + 1] = array[i]; #big elements into the tail of array
            i = i - 1;
        array[i + 1] = key;



