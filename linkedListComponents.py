# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def numComponents(self, head: ListNode, G: [int]) -> int:
        result = 0
        tempSet = set(G)
        lastContent = False
        while head:
            if head.val in tempSet:
                lastContent = True
            else:
                if lastContent is True:
                    lastContent = False
                    result += 1
            head = head.next
        if lastContent is True:
            result += 1
        return result


a = [1, 2, 3, 4, 1, 2, 3]
print(set(a))
