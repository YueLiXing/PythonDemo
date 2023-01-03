# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pPath = []
        self.search(root, p, [], pPath)
        qPath = []
        self.search(root, q, [], qPath)
        pPath = pPath[0]
        qPath = qPath[0]
        cacheNode = None
        index = 0
        while index < len(pPath) and index < len(qPath):
            if pPath[index] == qPath[index]:
                cacheNode = pPath[index]
                index += 1
            else:
                break
        return cacheNode

    def search(self, node: TreeNode, targetNode: TreeNode, cachePath:[int], path: [int]) -> bool:
        if node is None:
            return False
        cachePath.append(node)
        if node.val == targetNode.val:
            path.append(cachePath)
            return True
        return self.search(node.left, targetNode, cachePath.copy(), path) or self.search(node.right, targetNode, cachePath.copy(), path)