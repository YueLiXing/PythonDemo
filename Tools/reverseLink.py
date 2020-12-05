class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        cache = ""
        temp = self
        while temp:
            cache += str(temp.val)
            temp = temp.next
        return "ListNode: "+cache


class Solution:
    def reverseLink(self, head: ListNode) -> ListNode:
        pre = None
        current = head
        while current:
            tempN = current.next
            if current:
                current.next = pre
            pre = current
            current = tempN
        return pre

    def reverseLink2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        tempN = self.reverseLink2(head.next)
        head.next.next = tempN
        head.next = None
        return tempN


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

print(Solution().reverseLink(head))
# print(Solution().reverseLink2(head))
