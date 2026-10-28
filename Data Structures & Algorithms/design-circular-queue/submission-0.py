class LinkedList:

    def __init__(self, val = None):
        self.prev = None
        self.next = None
        self.val = val

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.front = None
        self.rear = None
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = LinkedList(value)
            self.rear = self.front
            self.size = 1
        else:
            if not self.front.next:
                self.front.next = LinkedList(value)
            else:
                self.front.next.val = value
            tmp = self.front
            self.front = self.front.next
            self.front.prev = tmp
            self.size += 1
            if self.isFull():
                self.front.next = self.rear
                self.rear.prev = self.front
        return True
            

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.rear = self.rear.next
            self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.rear.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.front.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()