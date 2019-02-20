# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        midNode = None
        fast = head
        slow = head
        while fast:
            # print(slow.val,fast.val)
            if fast.next == None:
                midNode = slow
                print(midNode.val," +")
                break
            elif fast.next != None and fast.next.next == None:
                midNode = slow.next
                print(midNode.val, " =")
                break
            else:
                slow = slow.next
                fast = fast.next
                fast = fast.next
        tempArr = []
        tempMid = midNode
        while midNode:
            tempArr.insert(0,midNode.val)
            midNode = midNode.next
        # print(tempArr)
        i = 0
        while head and i < len(tempArr):
            if head.val != tempArr[i]:
                return False
            head = head.next
            i += 1
        return True



a = [
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5]
]

for arr in a:
    start = None
    temp = None
    for val in arr:
        if start == None:
            start = ListNode(val)
            temp = start
        else:
            temp.next = ListNode(val)
            temp = temp.next

    print(Solution().isPalindrome(start))
