# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        fast = head
        slow = head
        while True:
            if fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next
        root = TreeNode(slow.val)

        return root

    def insertVal(self, root: TreeNode, val: int) -> TreeNode:
        tempRoot = root
        while True:
            if val < tempRoot.val:
                if tempRoot.left:
                    tempRoot = tempRoot.left
                else:
                    tempRoot.left = TreeNode(val)
                    break
            else:
                if tempRoot.right:
                    tempRoot = tempRoot.right
                else:
                    tempRoot.right = TreeNode(val)
                    break
        return root
