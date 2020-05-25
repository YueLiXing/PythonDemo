import collections


class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

    # def print(self):
    #     ret = []
    #     tempN = self
    #     while tempN:
    #         ret.append(str(tempN.key))
    #         tempN = tempN.next
    #     print("print", "->".join(ret))


class LRUCache(object):

    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity
        self.cacheDict = {}
        self.head = Node(None, None)
        self.last = self.head

    def get(self, key):
        if key not in self.cacheDict:
            return -1
        n = self.cacheDict[key]
        tempN = n.next
        n.pre.next = tempN
        if tempN:
            tempN.pre = n.pre
        else:
            self.last = n.pre
        tempN = self.head.next
        self.head.next = n
        n.next = tempN
        if tempN:
            tempN.pre = n
        else:
            self.last = n
        n.pre = self.head
        return n.val

    def put(self, key, value):
        if key in self.cacheDict:
            n = self.cacheDict[key]
            n.val = value
            tempN = n.next
            n.pre.next = tempN
            if tempN:
                tempN.pre = n.pre
            else:
                self.last = n.pre
            tempN = self.head.next
            if tempN:
                tempN.pre = n
            self.head.next = n
            n.pre = self.head
            n.next = tempN
        else:
            if self.count == self.capacity:
                del self.cacheDict[self.last.key]
                self.last = self.last.pre
                self.last.next = None
            else:
                self.count += 1
            n = Node(key, value)
            self.cacheDict[key] = n
            tempN = self.head.next
            if tempN:
                tempN.pre = n
            else:
                self.last = n
            n.next = tempN
            self.head.next = n
            n.pre = self.head

# class LRUCache(object):

#     def __init__(self, capacity):
#         self.od, self.cap = collections.OrderedDict(), capacity

#     def get(self, key):
#         if key not in self.od:
#             return -1
#         self.od.move_to_end(key)
#         return self.od[key]

#     def put(self, key, value):
#         if key in self.od:
#             del self.od[key]
#         elif len(self.od) == self.cap:
#             self.od.popitem(False)
            
#         self.od[key] = value


# cache = LRUCache(2)

# # cache.put(1, 11)
# # cache.put(2, 22)
# # cache.put(3, 33)
# # print(cache.get(1))
# # print(cache.get(2))


# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1), 1)
# # 返回  1
# cache.put(3, 3)
# # 该操作会使得密钥 2 作废
# print(cache.get(2), -1)
# # 返回 - 1 (未找到)
# cache.put(4, 4)
# # 该操作会使得密钥 1 作废
# print(cache.get(1), -1)
# # #返回 - 1 (未找到)
# # print(cache.get(3),3)
# # #返回  3
# # print(cache.get(4),4)
# # #返回  4
cache = LRUCache(2)
cache.put(2, 1)
cache.put(2, 2)
print(cache.get(2))
cache.put(1, 1)
cache.put(4, 1)
print(cache.get(2))
# print(cache.get(3))
# ["LRUCache", "put", "get", "put", "get", "get"]
# [[1], [2, 1], [2], [3, 2], [2], [3]]

# ["LRUCache","put","put","get","put","put","get"]
# [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]