# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
         self.swapTree(root)
         return root
    def swapTree(self, root: TreeNode):
        if root:
            t = root.left
            root.left = root.right
            root.right = t
            self.swapTree(root.left)
            self.swapTree(root.right)
        
