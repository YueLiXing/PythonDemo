# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
        self.cacheL = 0
        self.cacheArr = []
        self.travle(root,0)
        return self.cacheArr

    def travle(self, root: 'Node', level: int):
        if root == None:
            return
        tempArr = None
        if self.cacheL == level:
            tempArr = []
            self.cacheArr.append(tempArr)
            self.cacheL += 1
        else:
            tempArr = self.cacheArr[level]
        if level % 2 == 1:
            tempArr.insert(0, root.val)
        else:
            tempArr.append(root.val)
        self.travle(root.left, level+1)
        self.travle(root.right, level+1)
    
