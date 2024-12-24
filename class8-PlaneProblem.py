class Node:
    def __init__(self, data):
        x = 0
        y = 0
        price = 0
        numOfPaths = 0

        self.right = x
        self.down = y
        self.price = None
        self.numOfPaths = None
        self.value =

class PlaneProblem:

    def buildMat(self,a,b): '''build the matrix'''
        m = len(a)
        n = len(b)
        node = self
        matrix = [[0] * (n + 1)] * (m + 1)
        for i in range(m):
            for j in range(n):
                matrix[i][j] = node[i][j]


    def ClcPlaneProblem(self, a,b): '''clc the paths'''
        matrix = buildMat(self,a,b)

        for i in range(m):
            if i == 0:
                matrix[i][0] = matrix[i][0]
            else:
                matrix[i][0] = matrix[i][0] + matrix[i-1][0]
        for j in range(n):
            if j == 0:
                matrix[0][j] = matrix[0][j]
            else:
                matrix[0][j] = matrix[0][j] + matrix[0][j-1]
        for i in range(m):
            for j in range(n):
                down = node[i+1][j].price + node[i+1][j].down
                right = node[i][j+1].price + node[i][j+1].right
                node[i][j].price = min(down, right)
        return node[i][j].price

    def findOptimalPath(self, a, b): '''save the optimal (cheapest) path'''
        i = len(a)
        j = len(b)
        x = 0
        path = 0
        while i >= 0:
            while j >= 0:
                if matrix[i+1][j] > matrix[i][j-1]:
                    path[x] = 1
                    x +=1
                elif matrix[i+1][j] < matrix[i][j-1]:
                    path[x] = 0
                    x+=1
                else:
                    reverse_path[x] = 1

    def findpathbackwards(self, a, b):
        clcentry = findOptimalPath(self, a, b)
        i = len(a)-1
        j = len(b)-1
        path = []
        v = 0;
        while i !=0 and j != 0:
            if matrix[i][j].price == matrix[i-1][j].price + matrix[i-1][j].value:
                path[v] = matrix[i-1][j].price;
                i = i-1
            if matrix[i][j].price == matrix[i][j-1].price + matrix[i][j-1].value:
                path[v] = matrix[i][j-1].price;
            elif:
                path[v] = matrix[i][j-1].price;


    def clcpaths(self, a, b): '''נסמן את המסלול ב1,0 כדי לראות כמה שינויים יש בו'''

        if b.entry +cy == a.entry + cx:
            c.entry = a.entry + b.entry
        if b.entry +cy > a.entry + cx:
            c.entry = a.entry
        else
            c.entry = b.entry




def main():
    a = [3,5,4]
    b = [1,8,3]
    print(ClcPlaneProblem(a,b))


if __name__ == '__main__':
    main()

