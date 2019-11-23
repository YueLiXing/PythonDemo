class MyQueueNode:
    def __init__(self):
        self.next = None
        self.front = None
        self.value = None


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.top = None
        self.bottom = None
        self.count = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue.
        Return true if the operation is successful.
        """
        if self.count < self.k:
            self.count += 1
            if self.top:
                last = MyQueueNode()
                last.value = value

                last.front = self.bottom
                self.bottom.next = last
                self.bottom = last

            else:
                self.top = self.bottom = MyQueueNode()
                self.top.value = value
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue.
        Return true if the operation is successful.
        """
        flag = False

        if self.count == 1:
            self.top = self.bottom = None
            flag = True
        elif self.top:
            tempNext = self.top.next
            if tempNext:
                tempNext.front = None
            self.top = tempNext
            flag = True
        self.count -= 1 if flag else 0
        return flag

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.top:
            return self.top.value
        else:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.bottom:
            return self.bottom.value
        else:
            return -1
        # return self.bottom

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.k

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
