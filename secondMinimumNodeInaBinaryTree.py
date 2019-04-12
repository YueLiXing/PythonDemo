# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.min0 = root.val # 最小
        self.min1 = root.val # 第二小

        def traTree(r: TreeNode):
            x = r.val
            # print(x, self.min0, self.min1)
            if self.min0 == self.min1:
                if x < self.min0:
                    self.min1 = self.min0
                    self.min0 = x
                elif x > self.min0:
                    self.min1 = x
            else:
                if x < self.min0:
                    self.min1 = self.min0
                    self.min0 = x
                elif self.min0 < x < self.min1:
                    self.min1 = x
            # print(x, self.min0, self.min1," --")
            if r.left:
                traTree(r.left)
            if r.right:
                traTree(r.right)
        traTree(root)
        # print(self.min0, self.min1)
        if self.min0 == self.min1:
            return -1
        else:
            return self.min1


root = TreeNode(5)
root.left = TreeNode(8)
root.right = TreeNode(5)

# right = root.right
# right.left = TreeNode(15)
# right.right = TreeNode(7)

print(Solution().findSecondMinimumValue(root))
