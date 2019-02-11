class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        sumRet = 0
        leftIndex = 0
        rightIndex = len(height)-1
        while leftIndex < rightIndex:
            if index <= leftIndex:
                index += 1
                continue
            if height[index] >= height[leftIndex]:
                top = min(height[index], height[leftIndex])
                ret = 0
                for temp in range(leftIndex,index):
                    print("- ",top-height[temp])
                    ret += top-height[temp]
                leftIndex = index
                # print(ret)
                sumRet += ret
            index += 1
        return sumRet
        # print(sumRet)

Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
