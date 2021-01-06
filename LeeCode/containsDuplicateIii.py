class Solution:
    def containsNearbyAlmostDuplicate(self, nums: [int], k: int, t: int) -> bool:
        l = len(nums)
        # print(l,k)
        for i in range(l):
            # print(min(l, i+k))
            for j in range(i+1, min(l,i+k+1)):
                # print(i,j)
                # print(nums[i], nums[j], abs(nums[i]-nums[j]))
                if abs(nums[i]-nums[j]) <= t:
                    return True
        return False


print(Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))


