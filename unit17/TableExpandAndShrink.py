#coding:utf-8

class ExtendAndShrinkTable:
    def __init__(self):
        self.size = 0
        self.num = 0
        self.table = []
    def Insert(self,x):
        if self.size == 0:
            self.table = [None]
            self.size  = 1
        if self.num == self.size:
            NewTable = [None for i in range(self.size) * 2]
            for i in range(self.size):
                NewTable[i] = self.table[i]
            self.table = NewTable
            self.size = self.size * 2
        self.table[self.num] = x
        self.num = self.num + 1
    def Delete(self,x):
        if self.size == 0:
            print "Table is empty"
        
        self.table[self.table.index(x)] = None
        self.num = self.num - 1
        
        if self.num * 1.0 / self.size <= 0.25:
            NewTable = [None for i in range(self.size / 2) ]
            FilterTable = [element for element in self.table if element != None]
            for i in range(self.size / 4):
                NewTable[i] = FilterTable[i]
            self.table = NewTable
            self.size = self.size / 2
        
        
    
if __name__ == "__main__":
    Tableobject = ExtendAndShrinkTable()
    for element in range(9):
        Tableobject.Insert(element)
    for element in Tableobject.table:
        print element,
    print
    for element in range(4,9)[::-1]:
        Tableobject.Delete(element)
    for element in Tableobject.table:
        print element,
    print
        
                   
            