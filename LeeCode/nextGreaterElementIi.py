class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for index in range(len(nums)):
            flag = False
            for i in range(index+1, len(nums)):
                if nums[i] > nums[index]:
                    ret.append(nums[i])
                    flag = True
                    break
            if flag:
                continue
            else:
                for i in range(index):
                    if nums[i] > nums[index]:
                        ret.append(nums[i])
                        flag = True
                        break
                if flag == False:
                    ret.append(-1)
        
        return ret
