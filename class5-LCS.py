
def GreedyLCS(a,b):
    c = ""
    i = 0
    j = 0
    while i < len(a) and j < len(b) :
        if a[i] == b[j]:
            c += a[i]
            i +=1
        else:
            j +=1
    if i == len(a):
        while j < len(b):
            if a[i] == b[j-1]:
                c = c + a[i]
            j += 1
    if j == len(b):
        while i < len(a):
            if a[i] == b[j-1]:
                c = c + a[i]
            i += 1
    return c


def GreedyLCS1(a,b):
    c = ""
    i = 0    # X is the shortest string, Y is the longer string
    j = 0
    while max(i,j) < min(len(a),len(b)):
        if a[i] == b[j]:
            c += a[i]
            i+=1
        else:
            j += 1
    if j == min(len(a),len(b)):
        i += 1
        j = i
        while i != len(a) -1 :
            if a[i] == b[j]:
                c+= a[i]
                i +=1
                j += 1
                if j % len(a) == 0 or j > len(a):
                    j = i
            else:
                j += 1
    return c




def dynamicLCS(a,b):
    i = 0
    j = 0
    m = len(a)
    n = len(b)
    L =[[0] * (n + 1)] * (m + 1)

    for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif a[i-1] == b[j-1]:
                    L[i][j] = L[i-1][j-1] +1
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])

    lcs = ""
    i = m
    j = n
    while i >0 and j>0:
        if a[i-1] == b[j-1]:
            lcs += a[i-1]
            i -=1
            j-=1
        elif L[i][j-1] > L[i - 1][j]:
            j -=1
        else:
            i -=1

    lcs = lcs[::-1]
    return ("LCS of " + a + " and " + b + " is " + lcs)
    return L[m][n]











def main():
    a = "abcbdab"
    b = "bdcaba"
    #print(GreedyLCS(a,b))
    #print(GreedyLCS(b,a))
    #print(GreedyLCS1(b,a))

    X = "AGGTAB"
    Y = "GXTXAYB"
    print(dynamicLCS(Y,X))


if __name__ == '__main__':
        main()

