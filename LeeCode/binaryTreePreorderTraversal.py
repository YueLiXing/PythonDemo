
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

    def preorderTraversal2(self, root: TreeNode) -> [int]:
        result = []
        if root:
            tempArr = []
            tempArr.append(root)
            while len(tempArr) > 0:
                top = tempArr.pop()
                result.append(top.val)
                if top.right:
                    tempArr.append(top.right)
                if top.left:
                    tempArr.append(top.left)
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(Solution().preorderTraversal(root))
print(Solution().preorderTraversal2(root))


# test = [1,2,3,4,5]
# print(test.pop())
# print(test)
