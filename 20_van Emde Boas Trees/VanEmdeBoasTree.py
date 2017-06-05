#coding:utf-8
import math
class VEB:
    def __init__(self,size):
        self.size = size
        self.min = None
        self.max = None
        if size == 2:
            return
        else:
            self.high_sqrt_size = int(2 ** math.ceil(math.log(size,2) / 2.0))
            self.low_sqrt_size =  int(2 ** math.floor(math.log(size,2) / 2.0))
            self.cluster = [ VEB(self.low_sqrt_size) for i in range(self.high_sqrt_size) ]
            self.summary = VEB(self.high_sqrt_size)
            self.HIGH = lambda x: x / self.low_sqrt_size
            self.LOW = lambda x: x % self.low_sqrt_size
            self.INDEX = lambda high,low: high * self.low_sqrt_size + low
class VEBTreeProcess:
    @classmethod
    def minimum(cls,VEBob):
        return VEBob.min
    @classmethod
    def maximum(cls,VEBob):
        return VEBob.max
    @classmethod
    def member(cls,VEBob,element):
        if element == VEBob.min or element == VEBob.max:
            return True
        elif VEBob.size == 2:
            return False
        else:
            return cls.member(VEBob.cluster[VEBob.HIGH(element)],VEBob.LOW(element))
    @classmethod
    def successor(cls,VEBob,element):
        if VEBob.size == 2:
            if element == 0 and VEBob.max == 1:
                return 1
            else:
                return None
        elif VEBob.min != None and element < VEBob.min:
            return VEBob.min
        else:
            max_low = cls.maximum(VEBob.cluster[VEBob.HIGH(element)])
            if max_low != None and VEBob.LOW(element) < max_low:
                offset = cls.successor(VEBob.cluster[VEBob.HIGH(element)],VEBob.LOW(element))
                return VEBob.INDEX(VEBob.HIGH(element),offset)
            else:
                succ_cluster = cls.successor(VEBob.summary,VEBob.HIGH(element))
                if succ_cluster == None:
                    return None
                else:
                    offset = cls.minimum(VEBob.cluster[succ_cluster])
                    return VEBob.INDEX(succ_cluster,offset)
    @classmethod
    def predecessor(cls,VEBob,element):
        if VEBob.size == 2:
            if element == 1 and VEBob.min == 0:
                return 0
            else:
                return None
        elif VEBob.max != None and element > VEBob.max:
            return VEBob.max
        else:
            min_low = cls.minimum(VEBob.cluster[VEBob.HIGH(element)])
            if min_low != None and VEBob.LOW(element) > min_low:
                offset = cls.predecessor(VEBob.cluster[VEBob.HIGH(element)],VEBob.LOW(element))
                return VEBob.INDEX(VEBob.HIGH(element),offset)
            else:
                pred_cluster = cls.predecessor(VEBob.summary,VEBob.HIGH(element))
                if pred_cluster == None:
                    if VEBob.min != None and element > VEBob.min:
                        return VEBob.min
                    else:
                        return None
                else:
                    offset = cls.maximum(VEBob.cluster[pred_cluster])
                    return VEBob.INDEX(pred_cluster,offset)
    @classmethod
    def _emptyInsert(cls,VEBob,element):
        VEBob.min = element
        VEBob.max = element
    @classmethod
    def insert(cls,VEBob,element):
        if VEBob.min == None:
            cls._emptyInsert(VEBob,element)
        else:
            if element < VEBob.min:
                element,VEBob.min = VEBob.min,element
            if VEBob.size > 2:
                if cls.minimum(VEBob.cluster[VEBob.HIGH(element)]) == None:
                    cls.insert(VEBob.summary,VEBob.HIGH(element))
                    cls._emptyInsert(VEBob.cluster[VEBob.HIGH(element)],VEBob.LOW(element))
                else:
                    cls.insert(VEBob.cluster[VEBob.HIGH(element)],VEBob.LOW(element))
            if element > VEBob.max:
                VEBob.max = element
    @classmethod
    def delete(cls,VEBob,element):
        if VEBob.min == VEBob.max:
            VEBob.min = VEBob.max = None
        elif VEBob.size == 2:
            if element == 0:
                VEBob.min = 1
            else:
                VEBob.min = 0
            VEBob.max = VEBob.min
        else:
            if element == VEBob.min:
                first_cluster = cls.minimum(VEBob.summary)
                element = VEBob.INDEX(first_cluster,
                                      cls.minimum(VEBob.cluster[first_cluster]))
                VEBob.min = element
            cls.delete(VEBob.cluster[VEBob.HIGH(element)],VEBob.LOW(element))
            if cls.minimum(VEBob.cluster[VEBob.HIGH(element)]) == None:
                cls.delete(VEBob.summary,VEBob.HIGH(element))
                if element == VEBob.max:
                    summary_max = cls.maximum(VEBob.summary)
                    if summary_max == None:
                        VEBob.max = VEBob.min
                    else:
                        VEBob.max = VEBob.INDEX(summary_max,
                                                cls.maximum(VEBob.cluster[summary_max]))
            elif element == VEBob.max:
                VEBob.max = VEBob.INDEX(VEBob.HIGH(element),
                                        cls.maximum(VEBob.cluster[VEBob.HIGH(element)]))
    @classmethod
    def PrettyPrint(cls,VEBob,NumTab):
        if VEBob.size == 2:
            print '----' * NumTab,
            print (VEBob.size,VEBob.min,VEBob.max)
        else:
            print '----' * NumTab,
            print (VEBob.size,VEBob.min,VEBob.max)
            cls.PrettyPrint(VEBob.summary,NumTab + 1)
            for i in range(len(VEBob.cluster)):
                cls.PrettyPrint(VEBob.cluster[i],NumTab + 1)
                
            
if __name__ == '__main__':
    VEBob = VEB(16)
    List = [2,3,4,5,7,14,15]
    for i in range(len(List)):
        VEBTreeProcess.insert(VEBob,List[i])
    print VEBTreeProcess.maximum(VEBob)
    
    print VEBTreeProcess.minimum(VEBob)
    
    print VEBTreeProcess.member(VEBob,14)
    print VEBTreeProcess.predecessor(VEBob,3)
    print VEBTreeProcess.successor(VEBob,15)
    print 
    VEBTreeProcess.PrettyPrint(VEBob,0)
    VEBTreeProcess.delete(VEBob,15)
    print 
    VEBTreeProcess.PrettyPrint(VEBob,0)
    
                
            
         
         