def maxmaxNaivi(a):
    max1 = a[0]
    max2 = a[1]
    for i in range(len(a)):
        if max1 < a[i]:
            max1 = a[i]
            index = i
    a[index] , a[len(a)-1] = a[len(a)-1] , a[index]
    for i in range(len(a) -1):
        if max2 < a[i]:
            max2 = a[i]
            index = i
    a[index], a[len(a) - 2] = a[len(a) - 2], a[index]

    return max1,max2, a

def maxmax2(a):
    max1 = max(a[0], a[1])
    max2 = min(a[0], a[1])

    for i in range(len(a)):
        if max1 < a[i]:
            max2 = max1
            max1 = a[i]
        elif max2 < a[i]:
            max2 = a[i]
    return max1, max2



def maxmax4(a):
    max1 = max(a[0], a[1])
    max2 = min(a[0], a[1])


    for i in range(0, len(a)-1, 2):
        if a[i] >= a[i+1]:
            if max1 < a[i]:
                max2 = max(max1, a[i+1])
                max1 = a[i]
            else:
                if max1 < a[i+1]:
                    max2 = max(max1, a[i])
                    max1 = a[i+1]
                else:
                    if max2 < a[i+1]:
                        max2 = a[i+1]
    if (len(a)) %2 !=0:
        if max1 < a[len(a)-1]:
            max2 = max1
            max1 = a[len(a)-1]
        elif max2 < a[len(a)-1]:
            max2 = a[len(a)-1]



    return max1, max2




class stack:
    def __init__(self):
        self.top = 0
        self.st = []


def maxmax5(a):














def main():
    a = [8,7,9,6,5,4]
    b = [1,2,44,3,65,132,9]
    #print(maxmaxNaivi(a))
    #print(maxmax2(b))
    print(maxmax4(b))



if __name__ == '__main__':
    main()
