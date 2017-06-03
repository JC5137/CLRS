import math
class ProtoVEB:
    def __init__(self,size):
        self.size = size
        self.n = 0
        if size == 2:
            self.array = [0 for i in range(2) ]
        else:
            self.sqrt_size = int(math.sqrt(size))
            self.cluster = [ ProtoVEB(self.sqrt_size) for i in range(self.sqrt_size) ]
            self.summary = ProtoVEB(self.sqrt_size)
            self.HIGH = lambda x: x / self.sqrt_size
            self.LOW = lambda x: x % self.sqrt_size
            self.INDEX = lambda high,low: high * self.sqrt_size + low
class ProtoVEBProcess:
    @classmethod
    def member(cls,ProtoVEBOb,element):
        if ProtoVEBOb.size == 2:
            return ProtoVEBOb.array[element] == 1
        else:
            return cls.member(ProtoVEBOb.cluster[ProtoVEBOb.HIGH(element)],ProtoVEBOb.LOW(element))
    @classmethod
    def maximum(cls,ProtoVEBOb):
        if ProtoVEBOb.size == 2:
            if ProtoVEBOb.array[1] == 1:
                return 1
            elif ProtoVEBOb.array[0] == 1:
                return 0
            else:
                return None
        else:
            max_cluster = cls.maximum(ProtoVEBOb.summary)
            if max_cluster == None:
                return None
            else:
                offset = cls.maximum(ProtoVEBOb.cluster[max_cluster])
                return ProtoVEBOb.INDEX(max_cluster,offset)
    @classmethod
    def minimum(cls,ProtoVEBOb):
        if ProtoVEBOb.size == 2:
            if ProtoVEBOb.array[0] == 1:
                return 0
            elif ProtoVEBOb.array[1] == 1:
                return 1
            else:
                return None
        else:
            min_cluster = cls.minimum(ProtoVEBOb.summary)
            if min_cluster == None:
                return None
            else:
                offset = cls.minimum(ProtoVEBOb.cluster[min_cluster])
                return ProtoVEBOb.INDEX(min_cluster,offset)
    @classmethod
    def successor(cls,ProtoVEBOb,element):
        if ProtoVEBOb.size == 2:
            if element == 0 and ProtoVEBOb.array[1] == 1:
                return 1
            else:
                return None
        else:
            offset = cls.successor(ProtoVEBOb.cluster[ProtoVEBOb.HIGH(element)],ProtoVEBOb.LOW(element))
            if offset != None:
                return ProtoVEBOb.INDEX(ProtoVEBOb.HIGH(element),offset)
            else:
                succ_cluster = cls.successor(ProtoVEBOb.summary,ProtoVEBOb.HIGH(element))
                if succ_cluster == None:
                    return None
                else:
                    offset = cls.minimum(ProtoVEBOb.cluster[succ_cluster])
                    return ProtoVEBOb.INDEX(succ_cluster,offset)
    @classmethod
    def predecessor(cls,ProtoVEBOb,element):
        if ProtoVEBOb.size == 2:
            if element == 1 and ProtoVEBOb.array[0] == 1:
                return 0
            else:
                return None
        else:
            offset = cls.predecessor(ProtoVEBOb.cluster[ProtoVEBOb.HIGH(element)],ProtoVEBOb.LOW(element))
            if offset != None:
                return ProtoVEBOb.INDEX(ProtoVEBOb.HIGH(element),offset)
            else:
                succ_cluster = cls.predecessor(ProtoVEBOb.summary,ProtoVEBOb.HIGH(element))
                if succ_cluster == None:
                    return None
                else:
                    offset = cls.maximum(ProtoVEBOb.cluster[succ_cluster])
                    return ProtoVEBOb.INDEX(succ_cluster,offset)
    @classmethod
    def insert(cls,ProtoVEBOb,element):
        ProtoVEBOb.n = ProtoVEBOb.n + 1
        if ProtoVEBOb.size == 2:
            ProtoVEBOb.array[element] = 1
        else:
            cls.insert(ProtoVEBOb.cluster[ProtoVEBOb.HIGH(element)],ProtoVEBOb.LOW(element))
            cls.insert(ProtoVEBOb.summary,ProtoVEBOb.HIGH(element))
    @classmethod
    def delete(cls,ProtoVEBOb,element):
        ProtoVEBOb.n = ProtoVEBOb.n - 1
        if ProtoVEBOb.size == 2:
            ProtoVEBOb.array[element] = 0
        else:
            cls.delete(ProtoVEBOb.cluster[ProtoVEBOb.HIGH(element)],ProtoVEBOb.LOW(element))
            if ProtoVEBOb.cluster[ProtoVEBOb.HIGH(element)].n == 0:
                cls.delete(ProtoVEBOb.summary,ProtoVEBOb.HIGH(element))
if __name__ == '__main__':
    ProtoVEBob = ProtoVEB(16)
    List = [2,3,4,5,7,14,15]
    for i in range(len(List)):
        ProtoVEBProcess.insert(ProtoVEBob,List[i])
    print ProtoVEBProcess.maximum(ProtoVEBob)
    print ProtoVEBProcess.successor(ProtoVEBob,14)
    print ProtoVEBProcess.member(ProtoVEBob,0)
    print ProtoVEBProcess.predecessor(ProtoVEBob,7)
    
    ProtoVEBProcess.delete(ProtoVEBob,7)
    ProtoVEBProcess.delete(ProtoVEBob,4)
    ProtoVEBProcess.delete(ProtoVEBob,5)
    print ProtoVEBob.cluster[1].summary.array
    print ProtoVEBob.summary.cluster[0].array
    
    
        
            
        
                