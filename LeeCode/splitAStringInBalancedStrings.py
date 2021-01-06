class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        countR = countL = 0
        for c in s:
            if c == 'R':
                countR += 1
            else:
                countL += 1
            if countL == countR and countR > 0:
                result += 1
                countL = countR = 0
        return result


print(Solution().balancedStringSplit("RLRRLLRLRL"))
