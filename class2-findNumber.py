def findNum(a, x):
    i = 0
    j = len(a) -1
    min = a[i]
    max = a[j]
    while i < j:
        sum = min + max
        if sum == x:
            print(min, max)
            return
        elif sum < x:
            i += 1
            min = a[i]
        elif sum >x:
            j -=1
            max = a[j]
    print("try another number")





def main():
    a = [2,8,6,5,3,1,2]
    a.sort()
    print(a)

    x = 8
    findNum(a, x)

if __name__ == '__main__':
    main()
