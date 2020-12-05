# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> [int]:
        if root is None:
            return []

        stack = [root]
        output = []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
        # print(output)
        output.reverse()
        return output

# 后序遍历，题目要求不能用递归。
# 后序遍历的顺序是，先左子节点，再右子节点，再根节点

root = TreeNode(1)
r = TreeNode(2)
r.left = TreeNode(3)
root.right = r

print(Solution().postorderTraversal(root))
