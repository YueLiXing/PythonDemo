# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.realIsSymmetric(root.left, root.right)

    def realIsSymmetric(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        if left and right:
            if left.val == right.val:
                return self.realIsSymmetric(left.left, right.right) and self.realIsSymmetric(left.right, right.left)
            else:
                return False
        else:
            return False