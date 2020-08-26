class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        maxCount = 0
        for tempF in range(N+1):
            count = 0
            low = 1
            high = N
            while low <= high:
                mid = (low+high) // 2
                count += 1
                if tempF < mid:
                    high = mid-1
                else:
                    low = mid
            maxCount = max(maxCount, count)
                    
        return maxCount


print(Solution().superEggDrop(1, 2))
print(Solution().superEggDrop(2, 6))
print(Solution().superEggDrop(3, 14))
