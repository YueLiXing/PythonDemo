# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = {}
        while head:
            if head in temp:
                return True
            else:
                temp[head] = 1
            head = head.next
        return False
