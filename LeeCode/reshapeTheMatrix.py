class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums)*len(nums[0]) != r*c:
            return nums
        ret = [[]]
        lastA = ret[0]
        count = 0
        countR = 1
        for arr in nums:
            for val in arr:
                lastA.append(val)
                count += 1
                if count == c:
                    count = 0
                    if countR == r:
                        break
                    countR += 1
                    lastA = []
                    ret.append(lastA)
        return ret
