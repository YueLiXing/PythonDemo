# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        orginHead = head
        lastNode = head
        while head:
            if head.val == val:
                if head == orginHead:
                    orginHead = head.next
                lastNode.next = head.next
                head = lastNode.next
            else:
                lastNode = head
                head = head.next
        return orginHead
