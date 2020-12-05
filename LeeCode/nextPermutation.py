class Solution:
    def swap(self, cur, tar, arr):
        temp = arr[cur]
        arr[cur] = arr[tar]
        arr[tar] = temp
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = len(nums)-1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            self.swap(i,j,nums)
        # print('i:' ,i);
        # print(nums)
        # else:
        self.reverse(nums,i+1)

    def reverse(self, nums, start):
        i = start
        j = len(nums)-1
        while i < j:
            self.swap(i,j,nums)
            i += 1
            j -= 1



            
temp = [1, 3, 2] # [2, 1, 3]
# temp = [2, 3, 1]
# temp = [1, 2, 3] # [1, 3, 2]
Solution().nextPermutation(temp)
print(temp)
