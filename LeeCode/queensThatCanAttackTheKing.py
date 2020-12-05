class Solution:
    def queensAttacktheKing(self, queens: [[int]], king: [int]) -> [[int]]:
        target = []
        kingX = king[0]
        kingY = king[1]
        directions = [
            [-1, 0], [1, 0], [0, -1], [0, 1],
            [-1, -1], [1, 1], [-1, 1], [1, -1]
        ]
        index = 0
        while index < 8:
            kingX = kingX+directions[index][0]
            kingY = kingY+directions[index][1]
            flag = False
            if 0 <= kingX < 8 and 0 <= kingY < 8:
                temp = [kingX, kingY]
                if temp in queens:
                    target.append(temp)
                    flag = True
            else:
                flag = True
            if flag:
                kingX = king[0]
                kingY = king[1]
                index += 1
        return target

# class Solution:
#     def queensAttacktheKing(self, queens: [[int]], king: [int]) -> [[int]]:
#         target = []
#         count = 0
#         kingX = king[0]
#         kingY = king[1]
#         while count < 2:
#             kingX = kingX + (-1 if count == 0 else 1)
#             if 0 <= kingX < 8:
#                 temp = [kingX, kingY]
#                 if temp in queens:
#                     target.append(temp)
#                     count += 1
#             else:
#                 count += 1
#                 kingX = king[0]
#         count = 0
#         kingX = king[0]
#         while count < 2:
#             kingY = kingY + (-1 if count == 0 else 1)
#             # print(count, [kingX, kingY])
#             if 0 <= kingY < 8:
#                 temp = [kingX, kingY]
#                 if temp in queens:
#                     target.append(temp)
#                     count += 1
#             else:
#                 count += 1
#                 kingY = king[1]
#         count = 0
#         kingX = king[0]
#         kingY = king[1]
#         while count < 2:
#             kingX = kingX + (-1 if count == 0 else 1)
#             kingY = kingY + (-1 if count == 0 else 1)
#             # print(count, [kingX, kingY])
#             if 0 <= kingX < 8 and 0 <= kingY < 8:
#                 temp = [kingX, kingY]
#                 if temp in queens:
#                     target.append(temp)
#                     count += 1
#             else:
#                 count += 1
#                 kingX = king[0]
#                 kingY = king[1]
#         count = 0
#         kingX = king[0]
#         kingY = king[1]
#         while count < 2:
#             kingX = kingX + (1 if count == 0 else -1)
#             kingY = kingY + (-1 if count == 0 else 1)
#             # print(count, [kingX, kingY])
#             if 0 <= kingX < 8 and 0 <= kingY < 8:
#                 temp = [kingX, kingY]
#                 if temp in queens:
#                     target.append(temp)
#                     count += 1
#             else:
#                 count += 1
#                 kingX = king[0]
#                 kingY = king[1]
#         return target


r = Solution().queensAttacktheKing(
    [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], [0, 0])
print(r)
