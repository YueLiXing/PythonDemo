class Solution:
    def singleNumber(self, nums: [int]) -> int:
        cache = 0
        r = 0
        for i in nums:
            r ^= i

        return r

r = Solution().singleNumber([2, 2, 1])
print(r)
