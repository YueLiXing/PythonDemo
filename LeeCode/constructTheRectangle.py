import math
class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        L = int(math.sqrt(area))
        L = max(L, int(area/L))
        while area%L != 0:
            L += 1
        return [L,area//L]


print(Solution().constructRectangle(2))
# print(Solution().constructRectangle(4))

