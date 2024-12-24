#hamdani
def hamdaniSumGame(A):
    player1 = 0
    player2 = 0
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] >= A[j]:
            player1 += A[i]
            i += 1
        else:
            player1 += A[j]
            j -= 1
        if A[i] >= A[j]:
            player2 += A[i]
            i += 1
        else:
            player2 += A[j]
            j -= 1
    if len(A) % 2 != 0:
        player1 += A[i]

    if player1 > player2:
        return ("player1 is the winner! the sum is: ", player1)
    elif player1 < player2:
        return ("player2 is the winner! the sum is: ", player2)
    else:
        return("there is a tie! player1 equals to player2! the sum is: ", player1)

#////////
def AlwaysWinning(A):
    player1 = 0
    player2 = 0
    S1 = 0
    S2 = 0
    i = 0
    j = len(A) -1
    while i < j:
        S1 += A[i]
        S2 += A[i+1]
        i += 2
    if len(A) % 2 != 0:
        S1 += A[i]
    i = 0
    if S1 >= S2:
        while i < j:
            player1 += A[i]
            player2 += A[i+1]
            i += 2
    else:
        while i < j:
            player1 += A[i+1]
            player2 += A[i]
            i += 2
    player1 += A[i]


    return ("The WINNER is player1! the sum is: ", player1)

#///////////
def adaptivyAlgorithem(A):
    player1 = 0
    player2 = 0
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] > A[j]:
            player1 += A[i]
            i += 1
        else:
            player1 += A[j]
            j -= 1
        if A[i] > A[j]:
            player2 += A[i]
            i += 1
        else:
            player2 += A[j]
            j -= 1
        if A[i] + A[i+2] > A[j] + A[j-2] & (i < j):
            player1 += A[i]
            i += 1
        else:
            player1 += A[j]
            j -= 1
        if A[i] > A[j]:
            player2 += A[i]
            i += 1
        else:
            player2 += A[j]
            j -= 1
    if len(A) % 2 != 0:
        player1 += A[i]

    if player1 > player2:
        return ("The WINNER is player1! the sum is: ", player1)
    elif player1 < player2:
        return("The WINNER is player1! the sum is: ", player2)
    else:
        return("The sum is equal and both players are winners!, the sum is: ", player1)


def adaptivyAlgorithemOn(A):
    player1 = 0
    player2 = 0
    S1 = 0
    S2 = 0
    i = 0
    j = len(A) -1
    while i < j:
        S1 += A[i]
        S2 += A[i+1]
        i += 2
    if len(A) % 2 != 0:
        S1 += A[i]
    i = 0
    while i < j:
        if S1 >= S2:
                player1 += A[i]
                S1 -= A[i]
                i += 1
        elif S1 < S2:
                player1 += A[i+1]
                S2 -= A[i+1]
                i += 1
    player1 += A[i]

    if player1 > player2:
        return ("The WINNER is player1! the sum is: ", player1)
    elif player1 < player2:
        return("The WINNER is player1! the sum is: ", player2)
    else:
        return("The sum is equal and both players are winners!, the sum is: ", player1)












def main():
    A = [2, 8, 6, 5, 7]
    B = [1,3,6,1,3,6]
    C = [1,6,3,1,3,6]
    #print(hamdaniSumGame(A))
    #print(AlwaysWinning(A))
    #print(adaptivyAlgorithem(C))
    print(adaptivyAlgorithemOn(C))

if __name__ == '__main__':
        main()