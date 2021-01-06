class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        lenTarget = 0
        for c in S:
            if 'a' <= c <= 'z':
                lenTarget += 1
            else:
                lenTarget *= int(c)

        for c in reversed(S):
            K %= lenTarget
            if 'a' <= c <= 'z':
                if K == 0:
                    return c
                else:
                    lenTarget -= 1
            else:
                lenTarget /= int(c)
        return ""

    # 下面的方法也行，但是额外内存开销太大
    # def decodeAtIndex(self, S: str, K: int) -> str:
    #     count = 0
    #     target = ""
    #     lenStr = len(S)
    #     for c in S:
    #         if 'a' <= c <= 'z':
    #             count += 1
    #             target += c
    #             if count >= K:
    #                 return target[(K-1) % count]
    #         else:
    #             nCount = count * int(c)
    #             if nCount >= K:
    #                 return target[(K-1) % count]
    #             count = nCount
    #             temp = target
    #             for i in range(int(c)-1):
    #                 target += temp
    #     return target[(K-1) % count]


print(Solution().decodeAtIndex("a3bcd4", 1))  # a
print(Solution().decodeAtIndex("leet2code3", 10))  # o
print(Solution().decodeAtIndex("a2345678999999999999999", 1))  # a
print(Solution().decodeAtIndex("a2b3c4d5e6f7g8h9", 9))  # b
print(Solution().decodeAtIndex("a2b3c4d5e6f7g8h9", 3))  # b
print(Solution().decodeAtIndex("vzpp636m8y", 2920))  # z

# s = "czjkk9elaqwiz7s6kgv"
# "l4gjixan3ky7jfdg3kyop3hu"
# "sw3fm289thisef8blt7a7zr5v5lhxqpntenvxnmlq7l34ay3jaayikjps"
# print(Solution().decodeAtIndex(s, 768077956))
