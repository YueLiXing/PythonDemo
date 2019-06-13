# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> [int]:
        ret = []
        self.travlTree(root,0, ret)
        return ret

    def travlTree(self,root: TreeNode, level: int, ret:[int]):
        if root == None:
            return
        if level == len(ret):
            ret.append(root.val)
        self.travlTree(root.right, level+1, ret)
        self.travlTree(root.left, level+1, ret)
