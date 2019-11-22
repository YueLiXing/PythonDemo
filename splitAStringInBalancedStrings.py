import collections

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        startStr = ""
        endStr = ""
        startIndex = 0
        endIndex = len(s)-1
        cacheSet = set()
        while startIndex < endIndex:
            startStr += s[startIndex]
            endStr += s[endIndex]
            if self.judgeStr(startStr, endStr):
                cacheSet.add(startStr)
                result += 2
                startStr = ""
                endStr = ""
            if startStr in cacheSet:
                startStr = ""
                result += 1
            if endStr in cacheSet:
                endStr = ""
                result += 1
            startIndex += 1
            endIndex -= 1
        if len(startStr) > 0:
            result += 1
        return result

    def judgeStr(self, s0: str, s1: str):
        cacheDict0 = collections.defaultdict(int)
        cacheDict1 = collections.defaultdict(int)
        for c in s0:
            cacheDict0[c] += 1
        for c in s1:
            cacheDict1[c] += 1
        # print(cacheDict1,cacheDict0)
        return cacheDict1 == cacheDict0


print(Solution().balancedStringSplit("RLRRLLRLRL"))
