# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def midTravel(self, root: TreeNode):
        if root.left:
            self.midTravel(root.left)
        if self.root is None:
            self.current = self.root = TreeNode(root.val)
        else:
            self.current.right = TreeNode(root.val)
            self.current = self.current.right
        if root.right:
            self.midTravel(root.right)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.root = None
        self.current = None
        self.midTravel(root)
        return self.root
