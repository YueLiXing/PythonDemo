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
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     t = None
    #     while head != None:
    #         n = head.next
    #         if t != None:
    #             head.next = t
    #             t = head
    #         else:
    #             t = head
    #             t.next = None
    #         head = n
    #         # t.print()
    #     return t

    # 递归法
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        t = None
        def rev(head,t):
            if head == None:
                return t
            else:
                n = head.next
                if t:
                    head.next = t
                else:
                    head.next = None
                t = head
                return rev(n, t)
        return rev(head,t)                    


# 1->2->3->4->5->NULL
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

# l.print()
Solution().reverseList(l).print()

# 事实证明，还是迭代法更快