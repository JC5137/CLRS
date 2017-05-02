#coding:utf-8
import sys
sys.path.append(r'../') 


from InsertSort import *

def Partition(Array,start,end,privot,k):
    Array[start],Array[k] = Array[k],Array[start]  #将枢纽元与首位置交换
    i = start + 1 #从枢纽元前面的元素开始
    j = end
    while True:
        while i <= j and Array[i] < privot:
            i = i + 1
        while i <= j and Array[j] >= privot:
            j = j - 1
        if i > j:
            break;
        else:
            Array[i],Array[j] = Array[j],Array[i]
    Array[start],Array[j] = Array[j],Array[start]  #将枢纽元与最后一个小于枢纽元的元素交换
    
    return  j - start + 1  #算出枢纽元大于前面多少个元素
    
def Select(Array,start,Length,k):
    Groupnum = Length / 5
    if start == Length - 1:  #如果只有一个元素，返回
        return Array[start]
    if Length <= 5:  #如果长度小于5排序找到第k个元素
        InsertSort(Array,start,Length)
        return Array[start + k - 1]  #偏移k-1个元素，Array[start + k - 1]是第k大的元素
        
    #长度大于5，进行数组划分排序，并将中位数放到数组开头
    for i in range(0,Groupnum):
        InsertSort(Array,start + i * 5,5)  #每5个元素划为一组
        Array[start + i],Array[start + i * 5 + 2] = Array[start + i * 5 + 2],Array[start + i]
        
    InsertSort(Array,start,Groupnum) #对每个组的中位数进行排序
    midmidIndex = (Groupnum / 2 - 1) if Groupnum % 2 == 0  else ( (Groupnum + 1) / 2 - 1) #奇数的中位数 (n + 1) / 2 ,因为数组下标0开始 ,所以减1，偶数中位数取小的
    privot = Array[start + midmidIndex] #中位数的中位数为枢纽元

    q = Partition(Array,start,start + Length - 1,privot,start + midmidIndex) #q是[start,Index(privot)]的长度
    if q == k:
        return Array[start + k - 1]  #从开始处偏移
    elif k < q:
        return Select(Array,start,q - 1,k) #第三个参数为长度，减掉了枢纽元，重新选择
    else:
        return Select(Array,start + q,Length - q,k - q) #从开始处偏移，越过了枢纽元(start + q) 长度(Length - q)
    
array = [8,12,17,6,70,53,13,62,5,7,30,20,50,1,10,14,2,38,15,25,27,4,24,75,65,9,42,57,72,37,19,60,47,63]


print Select(array,0,len(array),1)
InsertSort(array,0,len(array))
print array



    
    