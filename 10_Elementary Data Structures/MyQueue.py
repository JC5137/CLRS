#coding:utf-8
class Queue:
    def __init__(self,n):
        self.size = n
        self.QueueArray = [None for i in range(n)]
        self.head = 0
        self.tail = 0
    def EnQueue(self,x):
        if self.IsFull() != True:
            self.QueueArray[self.tail] = x
            if self.tail == self.size - 1:
                self.tail = 0
            else:
                self.tail = self.tail + 1
        else:
            print "OverflowError"
    def DeQueue(self):
        if self.IsEmpty() != True:
            x = self.QueueArray[self.head]
            if self.head == self.size - 1:
                self.head = 0
            else:
                self.head = self.head + 1
            return x
        else:
            print "UnderflowError"
            
    def IsEmpty(self):
        if self.head == self.tail:
            return True
        else:
            return False
    
    def IsFull(self):
        if self.head == (self.tail + 1) % self.size:  #浪费一个元素用来判断队满的条件
            return True
        else:
            return False
if __name__ == "__main__":
    Queueob = Queue(5)
    Queueob.EnQueue(1)
    Queueob.EnQueue(1)
    Queueob.EnQueue(1)
    Queueob.EnQueue(1)
    Queueob.EnQueue(1)
    Queueob.DeQueue()
    Queueob.DeQueue()
    Queueob.DeQueue()
    Queueob.DeQueue()
    Queueob.DeQueue()
    Queueob.DeQueue()
    print Queueob.QueueArray,Queueob.head,Queueob.tail