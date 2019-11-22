# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if root.left and root.val != root.left.val:
            return False
        if root.right and root.val != root.right.val:
            return False
        return self.isUnivalTree(root.right) and self.isUnivalTree(root.left)

root = TreeNode(1)
root.left = TreeNode(1)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)

root.right = TreeNode(1)
root.right.right = TreeNode(1)

print(Solution().isUnivalTree(root))