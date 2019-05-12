
# Definition for a Node.


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    # 迭代法先序遍历N叉树
    def levelOrder(self, root: 'Node') -> [[int]]:
        ret = []
        if root == None:
            return ret

        self.fillRes(root, 0, ret);
        return ret;
    
    def fillRes(self, root: 'Node', level: int, ret: [[int]]):
        if len(ret) < level+1:
            ret.append([])

        ret[level].append(root.val)
        if root.children is not None:
            for node in root.children:
                self.fillRes(node,level+1,ret)


l = Node(3, [Node(5, None), Node(6, None)])
root = Node(1, [l, Node(2, None), Node(4, None)])


print(Solution().levelOrder(root))

