class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tempL = 0
        cacheL = 0
        for c in s:
            if c is " ":
                if tempL > 0:
                    cacheL = tempL
                tempL = 0
            else:
                tempL += 1
        return tempL if tempL > 0 else cacheL
