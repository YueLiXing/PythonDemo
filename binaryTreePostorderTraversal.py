# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> [int]:
        ret = []
        cache = []
        userCache = []
        curr = root
        while curr or len(cache) > 0:
            if curr:
                if curr in userCache:
                    pass
                else:
                    cache.append(curr)
                    curr = curr.left
            else:
                curr = cache.pop()
                ret.append(curr.val)
                userCache.append(curr)
                curr = curr.right
        return ret

root = TreeNode(1)
r = TreeNode(2)
r.left = TreeNode(3)
root.right = r

print(Solution().postorderTraversal(root))
