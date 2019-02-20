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
        min2Val = nums[-1]
        min2Index = len(nums)-1
        # for i in range(len(nums)):
        #     if nums[i] < min2Val:
        #         min2Val = nums[i]
        #         min2Index = i
        flag = True
        for i in range(len(nums)-2,-1,-1):
            # print(nums[i])
            if nums[i] < min2Val:
                self.swap(i,min2Index,nums)
                subArr = nums[i+1:]
                subArr.sort()
                nums[i+1:] = subArr
                return 
            if nums[i] < min2Val or (flag == True and nums[i] > min2Val):
                flag = False
                min2Val = nums[i]
                min2Index = i
        nums.sort()

            
temp = [1, 3, 2] # [2, 1, 3]
# temp = [2, 3, 1]
# temp = [1, 2, 3] # [1, 3, 2]
Solution().nextPermutation(temp)
print(temp)
