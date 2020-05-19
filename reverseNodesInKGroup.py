# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def append(self, l: []):
        cache = self
        for temp in l:
            cache.next = ListNode(temp)
            cache = cache.next

    def __str__(self):
        cache = ""
        temp = self
        while temp:
            cache += str(temp.val)
            temp = temp.next
        return "ListNode: "+cache


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cacheArr = []
        count = 0
        target = None
        cacheTarget = None
        temp = head
        
        while temp:
            cacheArr.append(temp)
            count += 1
            temp = temp.next

            if count == k:
                if target is None:
                    target = cacheArr[-1]
                    cacheArr.pop()
                    cacheTarget = target
                lenCache = len(cacheArr)
                while lenCache > 0:
                    cacheTarget.next = cacheArr.pop()
                    lenCache -= 1
                    cacheTarget = cacheTarget.next
                cacheTarget.next = None
                count = 0
            elif temp is None:
                if target is None:
                    target = cacheArr[0]
                    cacheArr.pop(0)
                    cacheTarget = target
                lenCache = len(cacheArr)
                while lenCache > 0:
                    cacheTarget.next = cacheArr[0]
                    lenCache -= 1
        return target


root = ListNode(1)
root.append([2, 3, 4, 5])
print(Solution().reverseKGroup(root, 3))
