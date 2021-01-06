class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        cacheDict = {}
        cacheSet = set()
        # print(list(map(pattern.index, pattern)))
        wList = s.split(" ")
        if len(pattern) != len(wList):
            return False
        for index in range(len(wList)):
            c = pattern[index]
            cW = wList[index]
            if c in cacheDict:
                if cacheDict[c] != cW:
                    return False
            else:
                if cW in cacheSet:
                    return False
                else:
                    cacheDict[c] = cW
                    cacheSet.add(cW)
        return True


Solution().wordPattern("abba", "a b b a")
