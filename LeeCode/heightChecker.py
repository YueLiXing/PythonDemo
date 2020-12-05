class Solution:
    def heightChecker(self, heights: [int]) -> int:
        sorted_heights = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                count += 1
        return count


print(Solution().heightChecker([1, 1, 4, 2, 1, 3]))
# print(Solution().heightChecker([2, 1, 2, 1, 1, 2, 2, 1]))
