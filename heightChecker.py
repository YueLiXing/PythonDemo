import collections


class Solution:
    def heightChecker(self, heights: [int]) -> int:
        cacheDict = collections.defaultdict(int)
        for tempH in heights:
            cacheDict[tempH] += 1
        count = 0
        j = 0
        for i in range(len(heights)):
            cacheDict[heights[i]] -= 1
            while cacheDict[heights[i]] > 0:
                if :
                    pass
                j += 1

        int count = 0
        for (int i=1, j=0, i < arr.length, i++)       {
            while (arr[i]-- > 0) {
                if (heights[j++] != i) count++
            }
        }
        return count


print(Solution().heightChecker([1, 1, 4, 2, 1, 3]))
# print(Solution().heightChecker([2, 1, 2, 1, 1, 2, 2, 1]))
