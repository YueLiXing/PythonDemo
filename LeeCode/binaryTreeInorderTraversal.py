
# import stac
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 迭代法中序遍历二叉树
    def inorderTraversal(self, root: TreeNode) -> [int]:
        ret = []
        cache = []
        curr = root
        while curr or len(cache) > 0:
            if curr:
                cache.append(curr)
                curr = curr.left
            else:
                curr = cache.pop()
                ret.append(curr.val)
                curr = curr.right
            # print("ret ",ret)
            
        return ret


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

Solution().inorderTraversal(root)


# test = [1,2,3,4,5]
# print(test.pop())
# print(test)
