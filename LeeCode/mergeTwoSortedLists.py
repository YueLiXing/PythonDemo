# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        list = ListNode(0)
        current = list
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    current.val = l1.val
                    l1 = l1.next
                else:
                    current.val = l2.val
                    l2 = l2.next
            else:
                if l1:
                    current.val = l1.val
                    l1 = l1.next
                else:
                    current.val = l2.val
                    l2 = l2.next
            if l1 or l2:
                current.next = ListNode(0)
                current = current.next
        return list
