# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (p != None) ^ (q != None):
            return False
        else:
            if p != None and q != None:
                if p.val == q.val:
                    return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
                else:
                    return False
            else:
                return True

print(True ^ False)