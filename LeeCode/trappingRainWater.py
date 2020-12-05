class Solution(object):
    def trap(self, height):
        if height is None or len(height) < 3:
            return 0
        """
        :type height: List[int]
        :rtype: int
        """
        maxHeightIndex = 0
        maxHeight = 0
        for index in range(len(height)):
            temp = height[index]
            if temp > maxHeight:
                maxHeight = temp
                maxHeightIndex = index

        sumRet = 0
        leftIndex = 0
        while leftIndex < maxHeightIndex:
            for j in range(leftIndex+1,maxHeightIndex+1):
                if height[leftIndex] - height[j] > 0:
                    sumRet += height[leftIndex]-height[j]
                else:
                    leftIndex = j
                    break
        rightIndex = len(height)-1
        while rightIndex > maxHeightIndex:
            for j in range(rightIndex-1,maxHeightIndex-1,-1):
                if height[rightIndex] - height[j] > 0:
                    sumRet += height[rightIndex]-height[j]
                else:
                    rightIndex = j
                    break
        return sumRet
        # print(sumRet)


r = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(r)
