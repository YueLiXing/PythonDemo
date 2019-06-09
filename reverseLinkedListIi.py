# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def print(self):
        ret = ""
        n = self
        while n != None:
            ret += str(n.val)
            n = n.next
            if n:
                ret += "->"
            else:
                break
        print(ret)


class Solution(object):
    # 迭代法
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        t = None
        i = 0
        root = head
        preNode = None
        nextNode = None
        while head != None:
            buffer = head.next
            i += 1
            if m <= i <= n:
                if t != None:
                    head.next = t
                    t = head
                else:
                    t = head
                    t.next = None
            else:
                if i+1 == m:
                    preNode = head
                if i == n+1:
                    nextNode = head
                t = head
            head = buffer

        if m > 1:
            return root
        else:
            return t



# 1->2->3->4->5->NULL
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

# l.print()
Solution().reverseBetween(l,2,4).print()
