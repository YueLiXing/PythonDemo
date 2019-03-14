class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        ret = -1
        indexFront = 0
        indexEnd = len(nums)
        indexMiddle = indexFront+1
        while indexFront+1 < indexEnd:
            newR = abs(target-(nums[indexFront] +nums[indexMiddle]+nums[indexEnd]))
            if ret == -1:
                ret = newR
            elif ret > newR:
                ret = newR
            indexMiddle += 1
            if indexMiddle >= indexEnd:
                indef
            indexFront += 1
            indexEnd -= 1
        return ret
