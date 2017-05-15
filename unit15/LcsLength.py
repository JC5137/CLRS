def LcsLength(str1,str2):
    str1Len = len(str1)
    str2Len = len(str2)
    LcsTable = [[0 for j in range(str2Len + 1)] for i in range(str1Len + 1)]
    for i in range(1,str1Len + 1):
        for j in range(1,str2Len + 1):
            try:
                if str1[i - 1] == str2[j - 1]:
                    LcsTable[i][j] = LcsTable[i - 1][j - 1] + 1
                elif LcsTable[i - 1][j] >= LcsTable[i][j - 1]:
                    LcsTable[i][j] = LcsTable[i - 1][j]
                else:
                    LcsTable[i][j] = LcsTable[i][j - 1]
            except:
                print i,j
                
    return LcsTable
def PrintLcs(str1,str2,LcsTable,i,j):
    try:
        if i == 0 or j == 0:
            return
        if str1[i - 1] == str2[j - 1]:
            PrintLcs(str1,str2,LcsTable,i - 1,j - 1)
            print str1[i - 1],
        elif LcsTable[i - 1][j] >= LcsTable[i][j - 1]:
            PrintLcs(str1,str2,LcsTable,i - 1,j)
        else:
            PrintLcs(str1,str2,LcsTable,i,j - 1)
    except:
        print i,j

if __name__ == "__main__":
    str1 = "ABCBDAB"
    str2 = "BDCABA"
    PrintLcs(str1,str2,LcsLength(str1,str2),len(str1),len(str2))