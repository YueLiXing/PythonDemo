
# import stac
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 迭代法先序遍历二叉树
    def preorderTraversal(self, root: TreeNode) -> [int]:
        ret = []
        cache = []
        curr = root
        while curr or len(cache) > 0:
            if curr:
                ret.append(curr.val)
                cache.append(curr)
                curr = curr.left
            else:
                curr = cache.pop()
                curr = curr.right

        return ret


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(Solution().preorderTraversal(root))


# test = [1,2,3,4,5]
# print(test.pop())
# print(test)
