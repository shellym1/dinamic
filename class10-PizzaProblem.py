
def PizzaProblem(x, n):
    F = x +1
    P = n / ( F + 1 )
    r = n % ( F + 1 )
    if r >= 2 and r <= x:
        Eli = (x*P + r -1)/((x+1)*P +r)
        if Eli < x/x+1:
            return True
    return False



def main():
    slices_num = 6
    eaters_speed = 2
    print(PizzaProblem(eaters_speed, slices_num))



if __name__ == '__main__':
    main()
