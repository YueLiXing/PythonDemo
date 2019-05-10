class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        temp = {}
        for i in range(len(nums)):
            v = nums[i]
            if v in temp:
                if i-temp[v] <= k:
                    return True
            temp[v] = i
        return False



print(Solution().containsNearbyDuplicate([1,2,3,1],k=3))
