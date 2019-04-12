
# Definition for a Node.


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


# 没写完

class Solution:
    # 迭代法先序遍历N叉树
    def preorder(self, root: 'Node') -> [int]:
        ret = []
        cache = []
        curr = root
        while curr or len(cache) > 0:
            if curr:
                ret.append(curr.val)

                flag = False
                if curr.children:
                    for t in curr.children:
                        if flag == False:
                            curr = t
                            flag = True
                        else:
                            cache.append(t)
                else:
                    curr = cache.pop()
                # curr = cache.pop()
            else:
                curr = cache.pop()
                # curr = curr.right

        return ret


l = Node(3, [Node(5, None), Node(6, None)])
root = Node(1, [l, Node(2, None), Node(4, None)])


print(Solution().preorder(root))


# test = [1,2,3,4,5]
# print(test.pop())
# print(test)
