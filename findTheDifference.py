class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sCount = {}
        tCount = {}
        for c in s:
            sCount[c] = sCount.get(c, 0)+1
        for c in t:
            temp = tCount.get(c, 0)+1
            if temp > sCount.get(c, 0):
                return c
            tCount[c] = temp
