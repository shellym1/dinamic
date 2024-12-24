import random

class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size

    def setData(self, value):
        self.data = value

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.head.prev = self.tail
        else:
            temp = new_node(value)
            self.head.prev = temp
            temp.next = self.head
            self.tail.next = temp
            temp.prev = self.tail
            temp = self.head
        self.size += 1

    def getHead(self):
        return self.head

class Cars:
    def createRand(self, maxsize):
        self.cars = DoubleLinkedList()
        for i in range(maxsize):
            c = chr(random.randint(65, 90))
            # while c == "V" or c == "W":
            # c = chr(random.randint(65, 90))
            self.cars.add(c)
        print(self.cars)

    def calcCars(self):
        copyList = self.cars
        if copyList.head() is None:
            return 0
        else:
            temp = copyList.head.value()
            copyList.head.setData("V")
            counter = 1
        while True:
            if temp.value() == "V":
                temp.value = "W"
                steps = counter
                while steps > 0:
                    temp = temp.prev
                    steps -= 1
                if temp.value == "W":
                    break
                else:
                    counter = 1
                    temp = copyList.head()
                    temp = temp.next
            else:
                temp = temp.next
                counter += 1
        return counter


    def calcList(self):
        if self.cars is None:
            return 0
        head = self.cars.head
        node = self.cars.head.next
        counter = 1
        while node != head:
            node = node.next
            counter += 1
        return counter

if __name__ == '__main__':
    '''
    Capital letters are in range of 65, 90
    small letters are in the range 97 (ascii 'a' is 97,), 97+26-1 (there are 26 letters in the alphabet)
    arr = [chr(random.randrange(65,90)) for i in range(13)]
    print("array:", arr)

    print(chr(90))
    '''

    parking = Cars()
    print("number of cars by DCLL =", parking.calcCars())
    print("number of cars by two pointers =", parking.calcList())














