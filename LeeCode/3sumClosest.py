class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums.sort()
        ret = sum(nums[:3])

        for index in range(len(nums)-2):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            num0 = nums[index]
            index1 = index+1
            index2 = len(nums)-1
            while index1 < index2:
                num1 = nums[index1]
                num2 = nums[index2]
                tempS = num0+num1+num2
                if tempS == target:
                    return target
                else:
                    if abs(target-tempS) < abs(target-ret):
                        ret = tempS
                    if tempS > target:
                        index2 -= 1
                    else:
                        index1 += 1
        
        return ret


# Solution().threeSumClosest([-1,2,3,4,-34],1)
print(Solution().threeSumClosest([-1,2,1,-4], 1))
