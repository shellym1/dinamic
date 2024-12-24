import sys


def GlassBall(floors, balls):
    f = len(floors)
    b = len(balls)
    i = 0
    j = 0
    mat = [[0] * f for x in b]

    for i in range(f):
        if f == 0:
            mat[0][i] = 0
        if f == 1:
            mat[1][i] = i
    for j in range(b):
        if b == 0:
            mat[j][0] = 0
        if b == 1:
            mat[j][1] = 1

    i = 2
    j = 2
    for i in range(f):
        for j in range(b):
            min = sys.maxsize
            for x in range(f):
                mat[i][j] = 1 + max( mat[i-1][x-1] , mat[i][j-x])
                result = mat[i][j]
                if min > result:
                    min = result
    return mat[floors][balls]








def main():
    floors = 4
    balls = 2
    print(GlassBall(4, 2))

if __name__ == '__main__':
        main()
