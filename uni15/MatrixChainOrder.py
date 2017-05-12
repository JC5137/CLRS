import time

def MatrixChainOrder(p):
    n = len(p) - 1
    m = [[ 0 for i in range(n + 1) ] for i in range(n + 1) ]
    s = [[ 0 for i in range(n + 1) ] for i in range(n + 1) ]
    for ChainLen in range(2,n+1):
        for i in range(1,n - ChainLen + 1 + 1):
            j = i + ChainLen - 1
            m[i][j] = float('inf')
            for k in range(i,j - 1 + 1):
                q = m[i][k] + m[k + 1][j] + p[i-1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return (m,s)
def PrintOptionalPerens(s,i,j):
    if i == j:
        print "A" + str(i),
    else:
        print "(",
        PrintOptionalPerens(s,i,s[i][j])
        PrintOptionalPerens(s,s[i][j] + 1,j)
        print ")",
p = [30,35,15,5,10,20,25]
(m,s) = MatrixChainOrder(p)
for i in range(1,len(m)):
    for j in range(i + 1,len(m[i])):
        print m[i][j],
    print
PrintOptionalPerens(s,1,6)


                
            
    
    
     
