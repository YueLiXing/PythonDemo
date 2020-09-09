
engTitle = "convert-sorted-list-to-binary-search-tree"


tempArr = engTitle.split("-")
resultArr = []
for temp in tempArr:
    if len(temp) >= 1 and len(resultArr):
        temp = temp.capitalize()
    resultArr.append(temp)


print("".join(resultArr)+".py")
print("".join(resultArr)+".swift")


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Test:
    def levelTravel(self, root):
        ret = []
        self._levelTral(root, 0, ret)
        return ret

    def _levelTral(self, root, level, ret):
        if root is None:
            return
        if len(ret) <= level:
            ret.append([])
        ret[level].append(root.val)
        self._levelTral(root.left, level+1, ret)
        self._levelTral(root.right, level+1, ret)


t = Test()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

print(t.levelTravel(root))
