def halfProblemOptimalSu(a, check):
    l = len(a)
    m = a[0]
    for i in range(check):
        if m < a[i]:
            m = a[i]
    return m








def main():
        a = [1,2,4,6,7,8,99,8,77,6,7889,7,6,5,4,3,3,44444,6,76,5,4342,12224,55778]
        print(halfProblemOptimalSu(a, 8))

if __name__ == '__main__':
        main()


