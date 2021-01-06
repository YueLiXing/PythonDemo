class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) < 3:    
            if n == 1:
                for temp in flowerbed:
                    if temp == 1:
                        return False
                return True
        for i in range(len(flowerbed)-2):
            if n == 0:
                return True
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                return True
            if i == len(flowerbed)-3 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
                flowerbed[i+2] = 1
                n -= 1
                continue
            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
                flowerbed[i+1] = 1
                n -= 1
                continue
        return n <= 0


print(Solution().canPlaceFlowers([0, 0, 0], 1))

