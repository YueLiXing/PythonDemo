class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cacheDict = {}
        for c in s:
            cacheDict[c] = cacheDict.get(c, 0) + 1
        for c in t:
            if c in cacheDict:
                v = cacheDict[c]-1
                if v == 0:
                    del cacheDict[c]
                else:
                    cacheDict[c] = v
            else:
                return False
        return True if len(cacheDict) == 0 else False


print(Solution().isAnagram("anagram", "nagaram"))
