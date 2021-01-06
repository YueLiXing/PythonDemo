class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        last = None
        for index in range(len(nums)-1):
            if nums[index] <= nums[index+1]:
                pass
            else:
                count += 1
                if (index+2 < len(nums) and nums[index] > nums[index+2]) and (index-1 >= 0 and nums[index-1] > nums[index+1]):
                    return False
                if count >= 2:
                    return False
                
        return True

print(Solution().checkPossibility([2,3,3,2,4])) # True
print(Solution().checkPossibility([4,2,3])) # True
print(Solution().checkPossibility([3, 4, 2, 3]))  # false
print(Solution().checkPossibility([-1, 4, 2, 3]))  # True

