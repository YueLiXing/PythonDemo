class MyQueueNode:
    def __init__(self):
        self.next = None
        self.front = None
        self.value = None


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here.
        Set the size of the deque to be k.
        """
        self.count = 0
        self.k = k
        self.top = None
        self.bottom = None

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque.
        Return true if the operation is successful.
        """
        if self.count < self.k:
            if self.top:
                top = MyQueueNode()
                top.value = value
                top.next = self.top
                self.top.front = top
                self.top = top
            else:
                self.top = self.bottom = MyQueueNode()
                self.top.value = value
            self.count += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque.
        Return true if the operation is successful.
        """
        if self.count < self.k:
            if self.bottom:
                bottom = MyQueueNode()
                bottom.value = value
                bottom.front = self.bottom
                self.bottom.next = bottom
                self.bottom = bottom
            else:
                self.top = self.bottom = MyQueueNode()
                self.top.value = value
            self.count += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque.
        Return true if the operation is successful.
        """
        if self.count > 0:
            if self.count == 1:
                self.top = self.bottom = None
            else:
                tempNext = self.top.next
                tempNext.front = None
                self.top.next = None
                self.top = tempNext
            self.count -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque.
        Return true if the operation is successful.
        """
        if self.count > 0:
            if self.count == 1:
                self.top = self.bottom = None
            else:
                tempFront = self.bottom.front
                tempFront.next = None
                self.bottom.front = None
                self.bottom = tempFront
            self.count -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.count > 0:
            return self.top.value
        else:
            return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.count > 0:
            return self.bottom.value
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.count == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
