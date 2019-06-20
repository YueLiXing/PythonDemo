# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        r = head
        pre = None
        while head and head.next:
            # l = r
            # ret = ""
            # while l:
            #     ret += str(l.val)+"-"
            #     l = l.next
            # print(ret)

            if pre == None:
                r = head.next
                head.next = head.next.next
                r.next = head
                pre = head
                head = head.next
            else:
                n = head.next
                head.next = head.next.next
                pre.next = n
                n.next = head
                pre = head
                head = head.next
        return r

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

l = Solution().swapPairs(l)
while l:
    print(l.val)
    l = l.next
