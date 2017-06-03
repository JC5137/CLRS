def CutRod(price,n):
    if n <= 0:
        return 0
    else:
        q = -float('inf')
        for i in range(1,n+1):
            q = max(q,price[i] + CutRod(price,n - i))
    return q
def Memorized_CutRod(price,n):
    MaxProfit = [-float('inf')] * (n + 1)
    return Memorized_CutRod_Aux(price,n,MaxProfit)
def Memorized_CutRod_Aux(price,n,MaxProfit):
    if MaxProfit[n] >= 0:
        return MaxProfit[n]
    if n == 0:
        q = 0
    else:
        q = -float('inf')
        for i in range(1,n+1):
            q = max(q,price[i] + Memorized_CutRod_Aux(price,n - i,MaxProfit))
        
    MaxProfit[n] = q
    return q
def BottomTopCutRod(price,n):
    MaxProfit = [0] * (n + 1)
    for j in range(1,n + 1):
        q = -float('inf')
        for i in range(1,j + 1):
            q = max(q,price[i] + MaxProfit[j - i])
        MaxProfit[j] = q
    return MaxProfit[n]
def Extended_BottomTopCutRod(price,n):
    MaxProfit = [0] * (n + 1)
    BestLength = [0] * (n + 1)
    
    for j in range(1,n + 1):
        q = -float('inf')
        for i in range(1,j + 1):
            if q < price[i] + MaxProfit[j - i]:
                q = price[i] + MaxProfit[j - i]
                BestLength[j] = i
                MaxProfit[j] = q
    return (MaxProfit,BestLength)
def PrintCutRodSolution(price,n):
    (MaxProfit,BestLength) = Extended_BottomTopCutRod(price,n)
    print MaxProfit
    print BestLength
    
        
    
    
    
 
price = [0,1,5,8,9,10,17,17,20,24,30]
PrintCutRodSolution(price,10)