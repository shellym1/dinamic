def greedyLIS(a):
    ans = []
    j = 0
    temp = a[0]
    ans = a[0]
    for i in range(len(a)-1):
        if temp < a[i]:
            ans[j] = a[i]
            temp = a[i]
            j+=1
    return ans


def greedy(A):   #O👎
    i = A[0]
    B = [i]
    for j in range(1, len(A)):
        if A[j] > i:
            B.append(A[j])
            i = A[j]
    return B





def main():
        a = [8, 7, 9, 6, 5, 4]
        b = [1, 2, 44, 3, 6, 9]
        c = [0,8,4,12,2,10]

        #print(greedyLIS(b))
        print(greedy(a))

if __name__ == '__main__':
    main()
