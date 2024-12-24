from random import randint
from operator import xor


def flip_coin():
    '''
    :return: returns 0 or 1 randomly
    '''
    return randint(0, 1)


def AliceGame():
    return flip_coin()

def BobGame():
    return flip_coin()

def AliceBobGame():
    alice = AliceGame()
    bob = BobGame()
    # result = True if (alice == bob) or (bob ^ alice) else False
    # result = True if (alice == bob) or (bob == 1 - alice) else False
    # result = True if (alice == bob) or (bob != alice) else False
    result = True if (alice == bob) or xor(bob, alice) else False
    return result


def flip_coin2():
    '''
    :return: returns 0 or 1 randomly
    '''
    return randint(0, 1)


def AliceGame2():
    return flip_coin()

def BobGame2():
    return flip_coin()

def AliceBobGame2():
    alice = AliceGame()
    bob = BobGame()
    t = 'false'
    if (alice == bob) or (bob == 1- alice):
        t = 'true'
    return t







def main():
    count = 1000000
    strategy_lst = [0] * 4  # [0,0,0,0]
    for i in range(count):
        strategy_lst[0] += AliceBobGame()
    for i in range(len(strategy_lst)):
        print(f"Strategy{i + 1} probability ==>", strategy_lst[i] / count)

    i=0;
    for i in range(1, count):
        result = AliceBobGame2()
        if (result == 'true'):
            AliceBobGame2+1
    return "Alice & Bob game : Strategy4 probability = " + AliceBobGame2/count


if __name__ == '__main__':
    main()


