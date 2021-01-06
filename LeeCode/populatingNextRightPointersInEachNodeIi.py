# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# 2020年09月28日 每日一题，缩减了内存开销，使用递归层序遍历的思想，进行简化


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cacheDict = {}
        self.travel(root, 0, cacheDict)
        return root

    def travel(self, root: 'Node', level: int, cacheDict: {}):
        if root is None:
            return
        if level in cacheDict:
            cacheDict[level].next = root
            cacheDict[level] = root
        else:
            cacheDict[level] = root
        root.next = None
        self.travel(root.left, level+1, cacheDict)
        self.travel(root.right, level+1, cacheDict)

    # def connect(self, root: 'Node') -> 'Node':
    #     self.cacheL = 0
    #     self.cacheArr = []
    #     self.travle(root, 0)
    #     for arr in self.cacheArr:
    #         l = len(arr)
    #         for i in range(l):
    #             if i < l-1:
    #                 arr[i].next = arr[i+1]
    #             else:
    #                 arr[i].next = None
    #     return root

    # def travle(self, root: 'Node', level: int):
    #     if root == None:
    #         return
    #     tempArr = None
    #     if self.cacheL == level:
    #         tempArr = []
    #         self.cacheArr.append(tempArr)
    #         self.cacheL += 1
    #     else:
    #         tempArr = self.cacheArr[level]
    #     tempArr.append(root)
    #     self.travle(root.left, level+1)
    #     self.travle(root.right, level+1)
