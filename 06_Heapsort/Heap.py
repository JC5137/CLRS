#coding:utf8
#最大堆的话比较函数a > b 返回True,Infinity 为极小值，最小堆相反
class Heap:
    def __init__(self,Array,Comparetor,Infinity):
        self.heap_size = self.arrayLength = len(Array)
        self.Comparator = Comparetor
        self.Infinity = Infinity
        self.array = Array
        self.BUILD_MAX_HEAP()
        
    
    def BUILD_MAX_HEAP(self):
        for i in range(self.arrayLength / 2)[::-1]:
            self.Max_HeapIFY(i)     
        
    def Max_HeapIFY(self,i):
        LEFT = lambda i : i * 2 + 1  #下标从0开始
        RIGHT = lambda i : i * 2 + 2
        l = LEFT(i)
        r = RIGHT(i)
        
        if l < self.heap_size and self.Comparator(self.array[l],self.array[i]) == 1:
            largestOrLeast = l
        else:
            largestOrLeast = i
        if r < self.heap_size and self.Comparator(self.array[r],self.array[largestOrLeast]) == 1:
            largestOrLeast = r
        
        if largestOrLeast != i:
            self.array[i],self.array[largestOrLeast] = self.array[largestOrLeast],self.array[i]
            self.Max_HeapIFY(largestOrLeast)
    
    def HEAPSORT(self):
        for i in range(self.arrayLength)[:0:-1]:
            self.array[0],self.array[i] = self.array[i],self.array[0]
            self.heap_size = self.heap_size - 1
            self.Max_HeapIFY(0) 
    def Heap_Maximum(self):
        return self.array[0]
    def Heap_Extract_Max_Or_Min(self):
        if self.heap_size <= 0:
            print "heap OverflowError"
        else:
            Max_Or_Min = self.array[0]
            self.array[0] = self.array[self.heap_size - 1]
            self.heap_size = self.heap_size - 1
            self.Max_HeapIFY(0)
            return Max_Or_Min
    def Heap_Increase_Key(self,i,Object):
        PARENT = lambda i: i / 2
        if self.array[i] != self.Infinity and self.Comparator(self.array[i],Object) == 1:
            print "new key is smaller than current key"
        else:
            self.array[i] = Object
            while i > 0 and self.Comparator(self.array[i],self.array[PARENT(i)]) == 1:
                self.array[PARENT(i)],self.array[i] = self.array[i],self.array[PARENT(i)]
                i = PARENT(i)
    def Heap_Insert(self,Object):
        self.heap_size = self.heap_size + 1
        self.array.append(None)
        self.array[self.heap_size - 1] = self.Infinity
        self.Heap_Increase_Key(self.heap_size - 1,Object)
        

def Comparator(a,b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1
if __name__ == '__main__':
    array  = [4,1,3,2,16,9,10,14,8,7]
    HeapOb = Heap(array,Comparator,-float('inf'))

    HeapOb.Heap_Insert(20)
    for i in range(HeapOb.heap_size):
        print array[i],

    
    