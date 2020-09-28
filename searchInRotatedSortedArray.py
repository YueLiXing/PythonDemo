class Solution:
    def search(self, nums: [int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high+1)//2
            if nums[mid] == target:
                return mid
            if nums[low] < nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1


s = Solution()
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = [9,8,7,6,5,4,3,2,1,0]
for k in range(1, len(a)):
    t = a[len(a)-k:len(a)]+a[:len(a)-k]
    print(t)
    for temp in t+[99, -1]:
        print("result:", temp, s.search(t, temp),
              t.index(temp) if temp in t else -1)
