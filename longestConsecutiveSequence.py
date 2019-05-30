class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tempS = set(nums)
        maxCount = 0
        tempCount = 0
        left = 0
        right = 0
        cur:int = None
        while len(tempS) > 0:
            if cur == None:
                cur = tempS.pop()
                tempCount = 1
                left = cur-1
                right = cur+1
            else:
                flagL = left in tempS
                flagR = right in tempS
                if flagL:
                    tempS.remove(left)
                    tempCount += 1
                    left -= 1
                if flagR:
                    tempS.remove(right)
                    tempCount += 1
                    right += 1
                else:
                    if flagL == False:
                        maxCount = max(maxCount,tempCount)
                        cur = None
        return max(tempCount,maxCount)


# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4

print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
