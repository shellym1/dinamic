

def SubMatOf1(mat):
    newMat = [[0] * (len(mat))] * (len(mat));
    imaximum = 0;
    jmaximim = 0;
    maxi = 0
    for i in range(len(mat)):
        newMat[i][0] = mat[i][0]
    for j in range(len(mat)):
        newMat[0][j] = mat[0][j]
    i = 0;
    j = 0;
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 0:
                newMat[i][j] = 0
            else:
                i += 1
                j += 1
            for i in range(len(mat)):
                for j in range(len(mat)):
                    newMat[i][j] = min(mat[i][j-1], mat[i-1][j], mat[i-1][j-1]) +1
                    if newMat[i][j] > maxi:
                        maxi = newMat[i][j]
                        imaximum = i
                        jmaximim = j
                    else:
                        i += 1
                        j += 1
    return maxi


def main():



if __name__ == '__main__':
    main()

