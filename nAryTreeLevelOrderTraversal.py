
# Definition for a Node.


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


# 没写完

class Solution:
    # 迭代法先序遍历N叉树
    def levelOrder(self, root: 'Node') -> [[int]]:
    #     self.ret = []
    #     return self.ret
    # def preorder(self, root: 'Node') -> [int]:
        ret = []
        cache = []
        curr = root
        while curr or len(cache) > 0:
            if curr:
                ret.append(curr.val)

                # flag = False
                if curr.children != None and len(curr.children) > 0:
                    if len(curr.children) > 1:
                        for i in range(len(curr.children)-1, 0, -1):
                            cache.append(curr.children[i])

                    curr = curr.children[0]
                else:
                    if len(cache) > 0:
                        curr = cache.pop()
                    else:
                        break
                # curr = cache.pop()
            else:
                if len(cache) > 0:
                    curr = cache.pop()
                else:
                    break
                # curr = curr.right

        return ret


l = Node(3, [Node(5, None), Node(6, None)])
root = Node(1, [l, Node(2, None), Node(4, None)])


print(Solution().levelOrder(root))


# test = [1,2,3,4,5]
# print(test.pop())
# print(test)
