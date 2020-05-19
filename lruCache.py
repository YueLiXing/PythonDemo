import collections


class LRUCache(object):

    def __init__(self, capacity):
        self.od, self.cap = collections.OrderedDict(), capacity

    def get(self, key):
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            del self.od[key]
        elif len(self.od) == self.cap:
            self.od.popitem(False)
        self.od[key] = value


cache = LRUCache(2)

# cache.put(1, 11)
# cache.put(2, 22)
# cache.put(3, 33)
# print(cache.get(1))
# print(cache.get(2))


cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1),1)
#返回  1
cache.put(3, 3)
#该操作会使得密钥 2 作废
print(cache.get(2),-1)
#返回 - 1 (未找到)
cache.put(4, 4)
#该操作会使得密钥 1 作废
print(cache.get(1),-1)
# #返回 - 1 (未找到)
# print(cache.get(3),3)
# #返回  3
# print(cache.get(4),4)
# #返回  4
