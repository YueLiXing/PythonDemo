# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def levelOrder(self, root: 'Node') -> [[int]]:
#         ret = []
#         if root == None:
#             return ret

#         self.fillRes(root, 0, ret);
#         return ret;
#     def fillRes(self, root: 'Node', level: int, ret: [[int]]):
#         if len(ret) < level+1:
#             ret.append([])
#         ret[level].append(root.val)
#         if None != root.left:
#             self.fillRes(root.left, level+1, ret)
#         if None != root.right:
#             self.fillRes(root.right, level+1, ret)


class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        ret = []
        self.orger(root, 0, ret)
        return ret

    # 递归遍历，swift 里面使用了迭代法，进行层序遍历
    def orger(self, n: TreeNode, level, ret):
        if n is not None:
            if len(ret) < level+1:
                ret.append([])
            ret[level].append(n.val)
            self.orger(n.left, level+1, ret)
            self.orger(n.right, level+1, ret)
    
    def levelOrder2(self, root: TreeNode) -> [[int]]:
        ret = []
        if root:
            nodeCache = [[root]]
            level = 0
            while len(nodeCache) > 0:
                nextNodeCache = []
                if level == len(ret):
                    ret.append([])
                for tempNode in nodeCache[0]:
                    ret[level].append(tempNode.val)
                    if tempNode.left:
                        nextNodeCache.append(tempNode.left)
                    if tempNode.right:
                        nextNodeCache.append(tempNode.right)
                if len(nextNodeCache) > 0:
                    nodeCache.append(nextNodeCache)
                nodeCache.pop(0)
                level += 1

        return ret
