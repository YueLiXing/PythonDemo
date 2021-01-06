class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cacheDict = {}
        cacheTset = set()
        for index in range(len(s)):
            cS = s[index]
            cT = t[index]
            if cS in cacheDict:
                if cacheDict[cS] == cT:
                    continue
                else:
                    return False
            else:
                if cT in cacheTset:
                    return False
                else:
                    cacheTset.add(cT)
                    cacheDict[cS] = cT
        return True
