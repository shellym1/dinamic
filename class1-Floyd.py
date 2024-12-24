class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def print_list(self): #הדפסת הרשימה
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next



class Floyd:
    def isCycled(self):
        head = self.head
        if head is None or head.next is None:
            return 'False'
        pointer1 = self.head
        pointer2 = self.head
        while pointer2 is not None and pointer1 is not None and pointer2.next is not None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            if pointer1 == pointer2:
                return True
        return False

    def breakingPoint(self):
        head = self.head
        if head is None or head.next is None:
            return 'False'
        pointer1 = self.head
        pointer2 = self.head
        while pointer2 is not None and pointer1 is not None and pointer2.next is not None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            if pointer1 == pointer2:
                return pointer2
        return 'There is no cycle'

    def startPoint(self):
        head = self.head
        if head is None or head.next is None:
            return 'False'
        pointer1 = self.head
        pointer2 = self.head
        while pointer2 is not None and pointer1 is not None and pointer2.next is not None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            if pointer1 == pointer2:
                pointer1 = head
                while pointer1 != pointer2:
                    pointer1 = pointer1.next
                    pointer2 = pointer2.next.next
            return pointer2

    def loopLength(self, startLoop):
        start = startLoop
        counter = startLoop.next
        len = 1
        while start != counter:
            counter = counter.next
            len += 1
        return len
