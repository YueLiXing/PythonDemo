# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root.right
                root.right = root.left
                root.left = None
                root = root.right
            else:
                root = root.right

    # def flatten(self, root: TreeNode) -> None:
    #     if root is None:
    #         return
    #     print(root.val)
    #     self.flatten(root.left)
    #     self.flatten(root.right)
    #     if root.left is not None:  # 后序遍历
    #         pre = root.left  # 令 pre 指向左子树
    #         while pre.right:
    #             pre = pre.right  # 找到左子树中的最右节点
    #         pre.right = root.right  # 令左子树中的最右节点的右子树 指向 根节点的右子树
    #         root.right = root.left  # 令根节点的右子树指向根节点的左子树
    #         root.left = None  # 置空根节点的左子树
    #     root = root.right  # 令当前节点指向下一个节点


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)
Solution().flatten(root)

print()
while root:
    print(root.val)
    root = root.right
