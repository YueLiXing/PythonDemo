class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastNum = None
        lastNumCount = 0
        lenNums = len(nums)
        index = 0
        while True:
            if index < lenNums:
                current = nums[index]
                if lastNum is None:
                    lastNum = current
                    lastNumCount = 1
                else:
                    if lastNum == current:
                        if lastNumCount < 2:
                            lastNumCount += 1
                        else:
                            nums.pop(index)
                            lenNums -= 1
                            continue
                    else:
                        lastNum = current
                        lastNumCount = 1
                index += 1
            else:
                break
        return lenNums
