#coding:utf-8
import sys
sys.path.append(r'../6_Heapsort') 


from Heap import *

#StartTime表示任务的开始时间列表，FinnalTime代表任务的结束时间列表,按单调递增顺序排序

class Activity:
    def __init__(self,ActivityIDList,StartTimeList,FinnalTimeList,n):
        self.Length = n
        self.ActivityList = []
        
        for i in range(self.Length):
            self.ActivityList.append(self.ActivityEntity(ActivityIDList[i],StartTimeList[i],FinnalTimeList[i]))
        Comparetor = lambda Object1,Object2: True if Object1.FinnalTime > Object2.FinnalTime else False
        self.ActivityHeap = Heap(self.ActivityList,Comparetor,-float('inf'))
    def GreedyActivitySelectOR(self):
        self.ActivityHeap.HEAPSORT()
        ActivityMaxSubSet = []
        ActivityMaxSubSet.append(self.ActivityList[0].ActivityID)
        k = 0
        for m in range(1,self.Length):
            if self.ActivityList[m].StartTime >= self.ActivityList[k].FinnalTime:
                ActivityMaxSubSet.append(self.ActivityList[m].ActivityID)
                k = m
        return ActivityMaxSubSet
    class ActivityEntity:
        def __init__(self,ActivityID,StartTime,FinnalTime):
            self.ActivityID = ActivityID
            self.StartTime  = StartTime
            self.FinnalTime = FinnalTime
        

if __name__ == '__main__':
    StartTimeList = [1,3,0,5,3,5,6,8,8,2,12]
    FinnalTimeList= [4,5,6,7,9,9,10,11,12,14,16]
    ActivityIDList = [ 'A' + str(i) for i in range(len(FinnalTimeList)) ]
    ActivityOb = Activity(ActivityIDList,StartTimeList,FinnalTimeList,len(ActivityIDList))
    print ActivityOb.GreedyActivitySelectOR()
    