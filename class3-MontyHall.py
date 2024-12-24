from random import randint

def MontyHall():
    index = randint(0, 2)
    A = [0,0,0]
    A[index] = 1
    loose = 0
    win = 0
    if A[1] and A[2] == 0:
        loose +=1
    else:
        win += 1
    return loose, win










def main():
    X = [0,0]
    l = X
    for i in range(1000):
        l, w = MontyHall()
        X[0] += l
        X[1] += w
    print('loose = ', X[0] / 1000,    ' ,win = ' ,X[1]/1000)

if __name__ == '__main__':
        main()