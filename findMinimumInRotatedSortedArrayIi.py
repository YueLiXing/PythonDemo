class Solution:
    def findMin(self, nums: [int]) -> int:
        low = 0
        high = len(nums)-1
        while low < high:
            mid = (low+high) // 2
            # print(nums[mid], nums[high])
            if nums[mid] > nums[high]:
                low = mid+1
            elif nums[mid] < nums[high]:
                high = mid
            else:
                high -= 1
        # print(low, high)
        return nums[low]


print(Solution().findMin([3, 4, 5, 1, 2]))
