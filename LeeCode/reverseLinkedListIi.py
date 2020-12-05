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
        if head is None:
            return head
        index = 1
        pre = None
        current = head
        while index < m:
            pre = current
            current = current.next
            index += 1

        con = pre
        tail = current
        print(tail.val)

        while index <= n:
            tempN = current.next
            current.next = pre
            pre = current
            current = tempN
            index += 1
        if con:
            con.next = pre
        else:
            head = pre
        tail.next = current
        return head
            



# 1->2->3->4->5->NULL
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

# l.print()
# Solution().reverseBetween(l,2,4).print()
# Solution().reverseBetween(l, 2, 4).print()  # 1->4->3->2->5
Solution().reverseBetween(l, 1, 4).print() #
