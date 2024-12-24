

def NumbersGame2(a):
    n = len(a)
    mat = [[0] * n for x in range(n)]
    for i in range(n):
        mat[i][i] = a[i]
    i = n - 2
    while i >= 0:
        for j in range(i+1, n):
            mat[i][j] = max(int(a[i]) - int(mat[i + 1][j]), int(a[j]) - int(mat[i][j - 1]))
        i -= 1
    # print(mat)
    return mat

def clcsums(game):
    sum = 0;
    firstsum = 0;
    first = 0;
    secoundsum = 0;
    secound = 0;
    n = len(game);
    mat = NumbersGame2(game)
    i = 0;
    j = n-1;

    while j > i:
            if game[i] - mat[i + 1][j] > game[j] - mat[i][j - 1]:
                print("ALICE: I take the first:", game[i])
                firstsum += game[i]
                first = i
                i += 1
            else:
                print("ALICE: I take the secound:", game[j])
                firstsum += game[j]
                first = j
                j -= 1
            if game[i] - mat[i + 1][j] > game[j] - mat[i][j - 1]:
                print("BOB: I take the first:", game[i])
                secoundsum += game[i]
                secound = i
                i += 1
            else:
                print("BOB: I take the secound:", game[j])
                secoundsum += game[j]
                secound = j
                j -= 1
    if n % 2 != 0:
        print("ALICE: I take the last number:", game[j])
        firstsum += game[j]
        first = j
        j -= 1
    print("Sum - ALICE:", firstsum, ", BOB:", secoundsum)
    print("Congratulations! Sum of first player (Alice) =", firstsum, ", Sum of second player (BOB) =", secoundsum,
          ", diff =", int(firstsum - secoundsum))




def clc(game):
    n = len(game);
    mat = [[0]*n] *n;
    i = 0
    j = n-1
    sum1 = 0;
    sum2 = 0;

    while j > i:
        if mat[i][j] == mat[i][i] - mat[i+1][j]:
            sum1 += mat[i][i]
            i += 1
        elif mat[i][j] == mat[j][j] - mat[i][j-1]:
            sum1 += mat[j][j]
            j -= 1
        if mat[i][j] == mat[i][i] - mat[i+1][j]:
            sum2 += mat[i][i]
            i += 1
        elif mat[i][j] == mat[j][j] - mat[i][j-1]:
            sum2 += mat[j][j]
            j -= 1
    if n % 2 != 0:
        sum1 += mat[i][i]
    return("the sum of player 1 is " , sum1,
           "the sum of player 2 is " ,sum2,
           "the diff is ", int(sum1-sum2))










def main():
    '''
    a = [1,3,6,1,3,6]
    NumbersGame2(a)
'''
    a = [1, 3, 6, 1, 3, 6]
    print(NumbersGame2(a))
    
    #print(clcsums(a))

    clc(a)



if __name__ == '__main__':
    main()






