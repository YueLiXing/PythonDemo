# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 题目原链接
# https: // leetcode-cn.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # 下面添加的两个方法纯粹为了生成链表和日志打印
    def getLast(self):
        if self.next != None:
            return self.next.getLast()
        else:
            return self
    def getAllValue(self):
        ret = [self.val]
        temp = self.next
        while temp:
            ret.append(temp.val)
            temp = temp.next
        return ret

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        orgin = ret
        isFirst = True
        flag = 0
        while l1 or l2 or flag > 0:
            num0 = l1.val if l1 else 0
            num1 = l2.val if l2 else 0
            temp = num0+num1+flag
            flag = int(temp/10)
            temp = temp%10
            if isFirst:
                ret.val = temp
                isFirst = False
            else:
                ret.next = ListNode(temp)
                ret = ret.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            # print(orgin.getAllValue())
        return orgin


test = Solution()
num0 = [1,2,3,4,5]
num1 = [1,2,3,4,5,6]
list1 = ListNode(num0[0])
for index in range(1, len(num0)):
    temp = list1.getLast()
    temp.next = ListNode(num0[index])

list2 = ListNode(num1[0])
for index in range(1, len(num1)):
    temp = list2.getLast()
    temp.next = ListNode(num1[index])

print(list1.getAllValue())
print(list2.getAllValue())
print(test.addTwoNumbers(list1, list2).getAllValue())
