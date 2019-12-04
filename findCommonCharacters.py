class Solution:
    # def commonCharsIMP(self, s0: str, s1: str, A: [str]) -> set:
    #     # print(s0, s1)
    #     # print('A', A)
    #     tempSet0 = set()
    #     for c in s0:
    #         key = c
    #         count = 0
    #         while key in tempSet0:
    #             key = c + "_" + str(count)
    #             count += 1
    #         tempSet0.add(key)
    #     tempSet1 = set()
    #     if s1:
    #         for c in s1:
    #             key = c
    #             count = 0
    #             while key in tempSet1:
    #                 key = c + "_" + str(count)
    #                 count += 1
    #             tempSet1.add(key)
    #         tempSet0 = tempSet0 & tempSet1
    #         if len(tempSet0) == 0:
    #             return tempSet0
            
    #         if A is not None and len(A) > 0:
    #             tempS = None
    #             lA = len(A)
    #             if lA == 1:
    #                 tempS = self.commonCharsIMP(A[0], None, None)
    #             elif lA == 2:
    #                 tempS = self.commonCharsIMP(A[0], A[1], None)
    #             else:
    #                 tempS = self.commonCharsIMP(A[0], A[1], A[2:])
    #             return tempSet0 & tempSet1 & tempS
    #         else:
    #             tempSet0 = tempSet0 & tempSet1
    #             return tempSet0
    #     else:
    #         return tempSet0

    # def commonChars(self, A: [str]) -> [str]:
    #     la = len(A)
    #     # print('l', la)
    #     allCacheSet = None
    #     if la == 1:
    #         allCacheSet = self.commonCharsIMP(A[0], None, None)
    #     elif la == 2:
    #         allCacheSet = self.commonCharsIMP(A[0], A[1], None)
    #     else:
    #         allCacheSet = self.commonCharsIMP(A[0], A[1], A[2:])
    #     result = []
    #     for c in allCacheSet:
    #         result.append(c.split("_")[0])
    #     return result

    # 执行用时 : 356 ms , 在所有 python3 提交中击败了 5.36% 的用户
    # 内存消耗: 12.9 MB , 在所有 python3 提交中击败了 99.30% 的用户
    # 经过一顿折腾，反而效率不如刚开始写的。。2333
    def commonChars(self, A: [str]) -> [str]:
        allCacheSet = None
        for index in range(len(A)):
            s = A[index]
            tempSet = set()
            for c in s:
                key = c
                count = 0
                while key in tempSet:
                    key = c + "_" + str(count)
                    count += 1
                tempSet.add(key)
            if index == 0:
                allCacheSet = tempSet
            else:
                allCacheSet = tempSet & allCacheSet
        result = []
        for c in allCacheSet:
            result.append(c.split("_")[0])
        return result


# print(Solution().commonChars(["bella", "label", "roller"]))
print(Solution().commonChars(["acabcddd", "bcbdbcbd", "baddbadb",
                              "cbdddcac", "aacbcccd", "ccccddda", "cababaab", "addcaccd"]))
