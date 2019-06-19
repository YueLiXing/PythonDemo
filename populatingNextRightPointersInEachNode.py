
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.cacheL = 0
        self.cacheArr = []
        self.travle(root, 0)
        for arr in self.cacheArr:
            l = len(arr)
            for i in range(l):
                if i < l-1:
                    arr[i].next = arr[i+1]
                else:
                    arr[i].next = None
        return root

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
        tempArr.append(root)
        self.travle(root.left, level+1)
        self.travle(root.right, level+1)
