


def SubSeqOf1(a):
    help=[0]*len(a);
    help[0] = a[0];
    for i in range(len(a)-1):
        if a[i+1] == 1:
            help[i+1] = help[i] +1
        else:
            help[i+1] = 0
    maxi = max(help)

    for j in range(len(help)-1):
        if help[j] > help[j+1]:
            index = help[j]
            j+=1
        else:
            j += 1

    return maxi, help.index(maxi)

def main():

    a = [0,0,1,1,0,1,1,1,0,0,1,1,0,1,0]
    print(SubSeqOf1(a))

if __name__ == '__main__':
    main()


