#coding:utf-8

def OptimalBest(p,q,n):
    #下标从1开始
    e = [ [ 0 for j in range(n + 1) ] for i in range(n + 2) ]  #生成e[n][n + 1]
    w = [ [ 0 for j in range(n + 1) ] for i in range(n + 2) ]  #生成w[n][n + 1]
    root = [ [ 0 for j in range(n + 1) ] for i in range(n + 1) ] #生成Root[n][n]
    for i in range(1,n + 2):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]
    for L in range(1,n + 1):
        for i in range(1,n - L + 2):
            j = i + L - 1
            e[i][j] = float('inf')
            w[i][j] = w[i][j - 1] + p[j] + q[j]
            for r in range(i,j + 1):
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r
    return (e,root)
def PrintTreeInOrder(root,i,j):
    if i <= j:
        PrintTreeInOrder(root,i,root[i][j] - 1)
        print root[i][j],
        PrintTreeInOrder(root,root[i][j] + 1,j)
def PrintTreePreOrder(root,i,j):
    if i <= j:
        print root[i][j],
        PrintTreePreOrder(root,i,root[i][j] - 1)
        PrintTreePreOrder(root,root[i][j] + 1,j)
def PrintTreePostOrder(root,i,j):
    if i <= j:
        print root[i][j],
        PrintTreePostOrder(root,i,root[i][j] - 1)
        PrintTreePostOrder(root,root[i][j] + 1,j)

p = [0,0.15,0.1,0.05,0.1,0.2]
q = [0.05,0.1,0.05,0.05,0.05,0.1]
Result = OptimalBest(p,q,5)

PrintTreeInOrder(Result[1],1,5)
print 
PrintTreePreOrder(Result[1],1,5)

        