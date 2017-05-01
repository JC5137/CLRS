class Heap:
    def __init__(self,Array):
        self.heap_size = self.arrayLength = len(Array)
        self.array = Array
        self.BUILD_MAX_HEAP()
    
    def BUILD_MAX_HEAP(self):
        for i in range(self.arrayLength / 2)[::-1]:
            self.Max_HeapIFY(i)     
        
    def Max_HeapIFY(self,i):
        LEFT = lambda i : i * 2
        RIGHT = lambda i : i * 2 + 1
        l = LEFT(i)
        r = RIGHT(i)
        
        if l < self.heap_size and self.array[l] > self.array[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.array[r] > self.array[largest]:
            largest = r
        
        if largest != i:
            self.array[i],self.array[largest] = self.array[largest],self.array[i]
            self.Max_HeapIFY(largest)
    
    def HEAPSORT(self):
        for i in range(self.arrayLength)[:0:-1]:
            self.array[0],self.array[i] = self.array[i],self.array[0]
            self.heap_size = self.heap_size - 1
            self.Max_HeapIFY(0) 
    def Heap_Maximum(self):
        return self.array[0]
    def Heap_Extract_Max(self):
        if self.heap_size <= 0:
            print "heap OverflowError"
        else:
            max = self.array[0]
            self.array[0] = self.array[self.heap_size - 1]
            self.heap_size = self.heap_size - 1
            self.Max_HeapIFY(0)
            return max
    def Heap_Increase_Key(self,i,key):
        PARENT = lambda i: i / 2
        if self.array[i] >= key:
            print "new key is smaller than current key"
        else:
            self.array[i] = key
            while i > 0 and self.array[PARENT(i)] < self.array[i]:
                self.array[PARENT(i)],self.array[i] = self.array[i],self.array[PARENT(i)]
                i = PARENT(i)
    def Heap_Insert(self,key):
        self.heap_size = self.heap_size + 1
        self.array.append(-float('inf'))
        self.Heap_Increase_Key(self.heap_size - 1,key)
        

array  = [4,1,3,2,16,9,10,14,8,7]
HeapOb = Heap(array)

HeapOb.Heap_Insert(20)
for i in range(HeapOb.heap_size):
    print array[i]

    
    