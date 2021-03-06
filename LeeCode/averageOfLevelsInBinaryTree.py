# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
    # def levelOrder(self, root: 'Node') -> [[int]]:
        ret = []
        if root == None:
            return ret

        self.fillRes(root, 0, ret);
        target = []
        for l in ret:
            target.append(sum(l)/len(l))
        return target
    
    def fillRes(self, root: 'Node', level: int, ret: [[int]]):
        if len(ret) < level+1:
            ret.append([])

        ret[level].append(root.val)
        if None != root.left:
            self.fillRes(root.left, level+1, ret)
        if None != root.right:
            self.fillRes(root.right, level+1, ret)

