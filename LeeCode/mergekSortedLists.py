# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        index = 0
        while True:
            if index >= len(lists):
                break
            if lists[index] == None:
                lists.pop(index)
            else:
                index += 1
        if len(lists) == 0:
            return None
        l = ListNode(0)
        current = l
        while len(lists):
            popIndex = 0
            smallNode = lists[0]
            for index in range(1,len(lists)):
                if lists[index] != None and lists[index].val < smallNode.val:
                    popIndex = index
                    smallNode = lists[index]
            
            if smallNode.next:
                lists[popIndex] = smallNode.next
            else:
                lists.pop(popIndex)
                
            current.val = smallNode.val
            if len(lists):
                current.next = ListNode(0)
                current = current.next
        return l

# 为毛这样提交，运行时间那么长！！
