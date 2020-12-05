# Definition for singly-linked list.
class ListNode:
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
        print(ret)


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        cacheDict = {}
        temp = head
        while temp != None:
            cacheDict[length] = temp
            length += 1
            temp = temp.next
        # print(cacheDict, length, n)
        targetIndex = length-n
        needDelete = cacheDict[targetIndex]
        if targetIndex > 0:
            preHead = cacheDict[targetIndex-1]
            preHead.next = needDelete.next
            return head
        else:
            return needDelete.next

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

Solution().removeNthFromEnd(l,2).print()

# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
