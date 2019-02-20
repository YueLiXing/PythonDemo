class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs(0, nums, ret)
        return ret

    def swap(self, cur, tar, arr):
        temp = arr[cur]
        arr[cur] = arr[tar]
        arr[tar] = temp

    def dfs(self, cur, nums, ret):
        if cur == len(nums)-1:
            ret.append(nums.copy())
            return
        tempS = set()
        for i in range(cur, len(nums)):
            flag = nums[i] in tempS
            if flag:
                continue
            tempS.add(nums[i])
            self.swap(cur, i, nums)
            self.dfs(cur+1, nums, ret)
            self.swap(cur, i, nums)
            


print(Solution().permuteUnique([1, 1, 1, 3]))
