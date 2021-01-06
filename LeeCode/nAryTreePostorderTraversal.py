# 给定一个 N 叉树，返回其节点值的后序遍历。


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children



class Solution(object):
    list = None
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if self.list == None:
            self.list = []
        if root == None:
            return self.list
        for node in root.children:
            self.postorder(node)
        self.list.append(root.val)
        return self.list