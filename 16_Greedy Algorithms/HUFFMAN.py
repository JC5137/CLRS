#coding:utf-8
import sys
sys.path.append(r'../06_Heapsort')
from Heap import *

class HuffmanNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.freq = None

class CharacterNode:
    def __init__(self,character,freq):
        self.character = character
        self.freq = freq
        
def HUFFMAN(C):
    n = len(C)
    comparetor = lambda Object1,Object2: True if Object1.freq < Object2.freq else False
    CharacterHeap = Heap(C,comparetor,float('inf'))
    for i in range(0,n - 1):
        HuffmanTree = HuffmanNode()
        HuffmanTree.left = CharacterHeap.Heap_Extract_Max_Or_Min()
        print "HuffmanTree.left.freq = ",
        print HuffmanTree.left.freq
        HuffmanTree.right = CharacterHeap.Heap_Extract_Max_Or_Min()
        print "HuffmanTree.right.freq = ",
        print HuffmanTree.right.freq
        HuffmanTree.freq = HuffmanTree.left.freq + HuffmanTree.right.freq
        CharacterHeap.Heap_Insert(HuffmanTree)
    return CharacterHeap.Heap_Extract_Max_Or_Min()
def ParserCharcter(HuffmanTree,seq,i,n,Root):
    if isinstance(HuffmanTree,CharacterNode):
        print HuffmanTree.character,
        if i == n:
            return
        ParserCharcter(Root,seq,i,n,Root)
    elif seq[i] == '0':
        ParserCharcter(HuffmanTree.left,seq,i + 1,n,Root)
    else:
        ParserCharcter(HuffmanTree.right,seq,i + 1,n,Root)
if __name__ == '__main__':
    C = [CharacterNode('a',45),CharacterNode('c',12),CharacterNode('b',13),CharacterNode('d',16),CharacterNode('e',9),CharacterNode('f',5)]
    Root = HUFFMAN(C)
    seq = "0101100"
    ParserCharcter(Root,seq,0,len(seq),Root)
    
    
    
        