# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        low = fast = head
        while fast:
            if fast.next is None:
                return low
            if fast.next.next is None:
                return low.next
            low = low.next
            fast = fast.next.next
        return low
