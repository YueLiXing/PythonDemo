# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        cacheArr = []
        self.travel(root, 0, cacheArr)
        return cacheArr[-1][0]
    
    def travel(self, root: TreeNode, level: int, cacheArr: [int]):
        if root is None:
            return
        lenCache = len(cacheArr)
        if level+1 > lenCache:
            cacheArr.append([])
        cacheArr[level].append(root.val)
        self.travel(root.left, level+1, cacheArr)
        self.travel(root.right, level+1, cacheArr)
