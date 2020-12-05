import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null
        so it contains at least one node.
        """
        self.root = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        count = 0
        target = 0
        temp = self.root
        while temp:
            count += 1
            if count == 1:
                target = temp.val
            else:
                if random.randint(1, count) == 1:
                    target = temp.val
            temp = temp.next
        return target


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
