class Stack:
    def __init__(self,n):
        self.StackArray = [0] * n
        self.top = -1
        self.size = n
    
    def StackEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    def Push(self,x):
        
        if self.top + 1 != self.size:
            self.StackArray[self.top + 1] = x
            self.top = self.top + 1
        else:
            print "OverflowError"

    def Pop(self):
        if self.StackEmpty():
            print "underflowError"
        else:
            self.top = self.top - 1
            return self.StackArray[self.top + 1]
if __name__ == "__main__":
    Stackob = Stack(4)
    Stackob.Push(10)
    Stackob.Push(10)
    Stackob.Push(10)
    Stackob.Push(10)
    Stackob.Push(10)
    Stackob.Push(10)
    Stackob.Pop()
    Stackob.Pop()
    Stackob.Pop()
    Stackob.Pop()
    Stackob.Pop()
    Stackob.Pop()
    print Stackob.StackArray

            
        