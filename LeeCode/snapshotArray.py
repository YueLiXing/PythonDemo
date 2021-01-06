class SnapshotArray:

    def __init__(self, length: int):
        self.snapIndex = 0
        self.cache = {}

    def set(self, index: int, val: int) -> None:
        temp = None
        if self.snapIndex in self.cache:
            temp = self.cache[self.snapIndex]
        else:
            self.cache[self.snapIndex] = {}
            temp = self.cache[self.snapIndex]
        temp[index] = val

    def snap(self) -> int:
        self.snapIndex += 1
        return self.snapIndex-1

    def get(self, index: int, snap_id: int) -> int:
        # print(self.cache, snap_id)
        while snap_id >= 0:
            tempCache = None
            if snap_id in self.cache:
                tempCache = self.cache[snap_id]
            else:
                snap_id -= 1
                continue
            if index in tempCache:
                return tempCache[index]
            else:
                snap_id -= 1
        return 0


# 一顿折腾，修改了数据结构，还不如刚开始的时候速度快
# class SnapshotArray:

#     def __init__(self, length: int):
#         self.snapIndex = 0
#         self.cache = {}

#     def set(self, index: int, val: int) -> None:
#         temp = None
#         if index in self.cache:
#             temp = self.cache[index]
#         else:
#             self.cache[index] = {}
#             temp = self.cache[index]
#         temp[self.snapIndex] = val

#     def snap(self) -> int:
#         self.snapIndex += 1
#         return self.snapIndex-1

#     def get(self, index: int, snap_id: int) -> int:
#         # print(self.cache, snap_id)
#         if index in self.cache:
#             tempCache = self.cache[index]
#             while snap_id >= 0:
#                 if snap_id in tempCache:
#                     return tempCache[snap_id]
#                 else:
#                     snap_id -= 1
#                     continue
#         return 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(3)
# obj.set(0, 5)
# param_2 = obj.snap()
# print(param_2)
# obj.set(0, 6)
# param_3 = obj.get(0, 0)
# print(param_3)

obj = SnapshotArray(4)
param_2 = obj.snap()
print(param_2)
param_2 = obj.snap()
print(param_2)
obj.set(0, 6)
param_3 = obj.get(0, 0)
print(param_3)
