# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode) -> [[int]]:
        self.cacheDict = {}

        def traTree(r: TreeNode,x,y):
            if x in self.cacheDict:
                t = self.cacheDict[x]
                if y in t:
                    t[y].append(r.val)
                else:
                    t[y] = [r.val]
            else:
                self.cacheDict[x] = {y:[r.val]}
            if r.left:
                traTree(r.left,x-1,y+1)
            if r.right:
                traTree(r.right, x+1, y+1)
        traTree(root,0,0)
        keyArr = [i for i in self.cacheDict]
        keyArr.sort()
        ret = []
        for i in keyArr:
            indexArr = [i for i in self.cacheDict[i]]
            indexArr.sort()
            r = []
            for index in indexArr:
                self.cacheDict[i][index].sort()
                for v in self.cacheDict[i][index]:
                    r.append(v)
                # print(i,self.cacheDict[i][index])
                # print(r)
            ret.append(r)
        # print(keyArr)
        # print(self.cacheDict.keys)
        # for v in self.cacheDict.keys:
        #     print(v)
        # print(self.cacheDict)
        return ret
            
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
right = root.right

right.left = TreeNode(15)
right.right = TreeNode(7)

print(Solution().verticalTraversal(root))
