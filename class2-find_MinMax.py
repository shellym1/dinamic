def findMinMax(A):
    i=0
    min = A[i]
    max = A[i + 1]
    l = len(A) if len(A) % 2 == 0 else (len(A) -1)
    for i in range(2, l, 2):
        min1 = A[i] if A[i] < A[i+1] else A[i+1]
        max1 = A[i+1] + A[i] - min1
        if min1 < min:
            min = min1
        if max < max1:
            max = max1
    lastNum = A[-1]
    if lastNum < min:
        min = lastNum
    elif max < lastNum:
        max = lastNum
    return min, max




def main():
    A = [2,8,6,5,3,1,2]
    B = [6,2,3,0,9,200]
    print(findMinMax(B))

if __name__ == '__main__':
    main()

