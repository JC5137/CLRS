#coding:utf-8
import sys
import random

sys.path.append('../unit10')
from DoubleLinkList import *

class HashTable_List:
    def __init__(self,m):
        self.Table_List = [ DoubleLinkList() for i in range(m)]
        self.Length = m
    def HashInsert_List(self,key):
        self.Table_List[self.Hash_List(key)].ListInsert(LinkListNode(key))
    def HashSearch_List(self,key):
        Index = self.Hash_List(key)
        return (Index,self.Table_List[self.Hash_List(Index)].ListSearch(key))    
    def HashDelete_List(self,Node):
        self.Table_List[self.Hash_List(Node.key)].ListDelete(Node)
    def Hash_List(self,key):
        return key % self.Length

class HashTable_Array:
    def __init__(self,m):
        self.Table_Array = [ None ] * m * 2
        self.Length = m * 2
    def HashInsert_Array(self,key):
        i = 0
        j = self.Hash_Array(key,i)
        while i != self.Length and self.Table_Array[j] != None:
            i = i + 1
            j = self.Hash_Array(key,i)
        if i != self.Length:
            self.Table_Array[j] = key
            return j
        else:
            print "HashTableOverFlow"
    def HashSearch_Array(self,key):
        
        i = 0
        j = self.Hash_Array(key,i)
        Count = 1
        while self.Table_Array[j] != None and self.Table_Array[j] != key and i != self.Length:
            i = i + 1
            j = self.Hash_Array(key,i)
            Count = Count + 1
        if self.Table_Array[j] == key:
            return (Count,j)
        else:
            return (Count,None)
    def Hash_Array(self,key,i):
        return (key + i) % self.Length
    

if __name__ == '__main__':
    Size = 11
    print "链表解决哈希冲突"
    HashTableListob = HashTable_List(Size)
    for i in range(Size):
        HashTableListob.HashInsert_List(random.randint(0,10001))
    #随机给出一个元素
    x = random.randint(0,10001)
    i = HashTableListob.HashSearch_List(x)[0]
    
    print "元素: %d,所在链表位置: %d,查找次数：%d" %(x,i,HashTableListob.Table_List[i].ListLen() + 1)
    
    for i in range(Size):
        print str(i) + ':',
        HashTableListob.Table_List[i].ListPrint()
        print
    
    
    print "开放寻址法解决冲突"
    HashTableArrayob = HashTable_Array(Size)
    for i in range(Size):
        HashTableArrayob.HashInsert_Array(random.randint(0,10001))
        
    (i,j) = HashTableArrayob.HashSearch_Array(x)
    print "元素: %d,所在数组位置: %s,查找次数：%d" %(x,j,i)
    
    for i in range(HashTableArrayob.Length):
        print i,HashTableArrayob.Table_Array[i]
    
    
    
    
        