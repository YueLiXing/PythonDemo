# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTreesImp(self, root: TreeNode, t1: TreeNode, t2: TreeNode):
        t1l = None
        t1r = None
        t2l = None
        t2r = None
        if t1:
            root.val = t1.val
            t1l = t1.left
            t1r = t1.right
        if t2:
            root.val += t2.val
            t2l = t2.left
            t2r = t2.right
        if t1l or t2l:
            lNode = TreeNode(0)
            root.left = lNode
            self.mergeTreesImp(lNode, t1l, t2l)
        if t1r or t2r:
            rNode = TreeNode(0)
            root.right = rNode
            self.mergeTreesImp(rNode, t1r, t2r)

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 or t2:
            root = TreeNode(0)
            self.mergeTreesImp(root, t1, t2)
            return root
        else:
            return None
        
