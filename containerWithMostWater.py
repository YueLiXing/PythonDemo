class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maxArea = 0
        while left < right:
            area = (right-left)*min(height[left],height[right])
            maxArea = max(maxArea,area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxArea
        # print(maxArea)
            
# 双向指针法，从前后同时向当中移动。
# 当左侧的比较高时，右边的就向当中靠一步。反之亦然

print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
