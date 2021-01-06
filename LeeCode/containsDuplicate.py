class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        temp = set()
        for v in nums:
            if v in temp:
                return True
            else:
                temp.add(v)
        return False


# class Solution:
#     def containsDuplicate(self, nums: [int]) -> bool:
#         return len(set(nums)) != len(nums)

print(Solution().containsDuplicate([1,2,3,1]))
