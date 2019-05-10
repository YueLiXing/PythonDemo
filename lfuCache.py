class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.count = 1
        self.pre = None
        self.next = None

    def show(self):
        ret = "\""
        temp = self
        while temp:
            ret += str(temp.key)+":"+str(temp.val)+"-"+str(temp.count)+" "
            temp = temp.next
        ret = ret[:-1]
        ret += "\""
        return ret

    def deleteLastNode(self):
        temp = self
        while temp.next:
            if temp.next.next == None:
                t = temp.next
                temp.next = None
                return t
            else:
                temp = temp.next


class NodeList:
    def __init__(self, count):
        self.count = count
        self.up = None
        self.down = None
        self.node: Node = None

    def show(self):
        ret = "\""
        temp = self
        while temp:
            # ret += str(temp.count)+" "
            ret += "node "+temp.node.show()
            # ret += "\n"
            temp = temp.down
        ret = ret[:-1]
        ret += "\""
        return ret
   
    def insertNode(self, node):
        temp = self.node
        self.node = node
        node.pre = None
        node.next = temp
        if temp:
            temp.pre = node
        # print(self.node.show())
        
    def appendListNode(self, listNode):
        if self.count > listNode.count:
            temp = self

            while temp:
                if temp.count < listNode.count:
                    temp.up.down = listNode
                    listNode.up = temp.up
                    listNode.down = temp
                    temp.up = listNode
                    break
                else:
                    if temp.count > listNode.count and temp.down == None:
                        temp.down = listNode
                        listNode.up = temp
                        break
                    else:
                        temp = temp.down
                
            return self
        else:
            listNode.down = self
            self.up = listNode
            return listNode
        

    def deleteLastNode(self) -> Node:
        temp = self
        if temp.down == None:
            return temp.node.deleteLastNode()
        else:
            while temp:
                if temp.down == None:
                    t: Node = temp.node
                    if t.next:
                        return t.deleteLastNode()
                    else:
                        if t.pre == None:
                            temp.node = None
                            self.deleteListNode(temp)
                        return t
                else:
                    temp = temp.down

    def deleteListNode(self, listNode):
        if listNode.up == None:
            return listNode.down
        else:
            listNode.up.down = listNode.down
            if listNode.down:
                listNode.down.up = listNode.up
        return self

    def deleteNode(self, node):
        if self.node == node:
            self.node = node.next
        else:
            node.pre.next = node.next
            if node.next:
                node.next.pre = node.pre
            


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheListDict = {}
        self.cacheNodeDict = {}
        self.count = 0
        self.root : NodeList = None

    def get(self, key: int) -> int:

        if key in self.cacheNodeDict:
            node = self.cacheNodeDict[key]
            node.count += 1
            self.reloadData(node)

            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        node: Node = None
        
        if key in self.cacheNodeDict:
            node = self.cacheNodeDict[key]
            node.val = value
            node.count = node.count+1
        else:
            node = Node(key, value)
            if self.count == self.capacity:
                if self.capacity == 1:
                    self.cacheListDict.clear()
                    self.cacheNodeDict.clear()
                    self.root = NodeList(1)
                    self.cacheListDict[1] = self.root
                else:
                    temp = self.root.deleteLastNode()
                    tempList = self.cacheListDict[temp.count]
                    if tempList.node == None:
                        del self.cacheListDict[temp.count]
                    if temp.key in self.cacheNodeDict:
                        del self.cacheNodeDict[temp.key]
            else:
                self.count += 1
            if self.root == None:

                self.root = NodeList(1)
                self.cacheListDict[self.root.count] = self.root
                # self.root.insertNode(node)
            
            self.cacheNodeDict[key] = node
        self.reloadData(node)

    def reloadData(self, node: Node):
        # print("key:"+str(node.key)+" value:"+str(node.val))
        # print(self.root.show(), self.count, 1)
        if node.count-1 > 0:
            nodeList:NodeList = self.cacheListDict[node.count-1]
            nodeList.deleteNode(node)
            if nodeList.node == None:
                # print(self.root.show(),1)
                self.root = self.root.deleteListNode(nodeList)
                del self.cacheListDict[node.count-1]
        # nodeList.dele
        targetList = None
        if node.count in self.cacheListDict:
            targetList = self.cacheListDict[node.count]
        else:
            targetList = NodeList(node.count)
            self.cacheListDict[node.count] = targetList
            if self.root:
                self.root = self.root.appendListNode(targetList)
            else:
                self.root = targetList
        targetList.insertNode(node)
        # print('root', self.root.show())
        


# [[2],[3,1],[2,1],[2,2],[4,4],[2]]

# [[1], [2, 1], [2], [3, 2], [2], [3]]

# ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
# cache = LFUCache(2)
# cache.put(1,1)
# cache.put(2,2)
# print(cache.get(1), "cur:1")
# cache.put(3, 3)
# print(cache.get(2), "cur:-1")
# print(cache.get(3), "cur: 3")
# cache.put(4,4)
# print(cache.get(1), "cur:")
# print(cache.get(3))
# print(cache.get(4))
# ["LFUCache","put","put","get","get","get","put","put","get","get","get","get"]
# [[3],[2,2],[1,1],[2],[1],[2],[3,3],[4,4],[3],[2],[1],[4]]
# cache = LFUCache(3)
# cache.put(2, 2)
# cache.put(1, 1)
# print("get ",cache.get(2), "cur:2")
# print("get ",cache.get(1), "cur:1")
# print("get ",cache.get(2), "cur:2")
# cache.put(3, 3)
# cache.put(4, 4)
# print("get ",cache.get(3), "cur:-1")
# print("get ",cache.get(2), "cur:2")
# print("get ",cache.get(1), "cur:1")
# print("get ",cache.get(4), "cur:4")


# ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
cache = LFUCache(2)
cache.put(1,1)
cache.put(2,2)
print("get",cache.get(1),"cur:1")
cache.put(3, 3)
print("get",cache.get(2),"cur:-1")
print("get",cache.get(3),"cur:3")
cache.put(4, 4)
print("get",cache.get(1),"cur:-1")
print("get",cache.get(3),"cur:3")
print("get",cache.get(4),"cur:4")
