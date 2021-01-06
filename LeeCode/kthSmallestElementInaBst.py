# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.cacheArr = []

        def traTree(r: TreeNode):
            if r.val not in self.cacheArr:
                l = len(self.cacheArr)
            if l < k:
                flag = False
                for i in range(l):
                    if r.val < self.cacheArr[i]:
                        self.cacheArr.insert(i, r.val)
                        flag = True
                        break
                if flag == False:
                    self.cacheArr.append(r.val)
                # print(self.cacheArr," 0")
            else:
                flag = False
                for i in range(l):
                    if r.val < self.cacheArr[i]:
                        self.cacheArr.insert(i, r.val)
                        flag = True
                        break
                if flag == True:
                    del self.cacheArr[l]
                # print(self.cacheArr, " 1")
            if r.left:
                traTree(r.left)
            if r.right:
                traTree(r.right)
        traTree(root)
        return self.cacheArr[-1]


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)

left = root.left
left.left = TreeNode(2)
left.right = TreeNode(4)
left = left.left

left.left = TreeNode(1)
# right = root.right
# right.left = TreeNode(15)
# right.right = TreeNode(7)

print(Solution().kthSmallest(root,3))
