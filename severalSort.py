class Solution:
    def xuanzepaixu(self, nums: [int], asc: bool):
        countN = len(nums)
        for i in range(countN-1):
            for j in range(i+1, countN):
                if (asc is True and nums[i] > nums[j]):
                    t = nums[i]
                    nums[i] = nums[j]
                    nums[j] = t
                elif asc is False and nums[i] < nums[j]:
                    t = nums[i]
                    nums[i] = nums[j]
                    nums[j] = t
        return nums

    def maopaopaixu(self, nums: [int], asc: bool):
        countN = len(nums)
        for i in range(countN):
            for j in range(countN-i-1):
                if asc and nums[j] > nums[j+1]:
                    t = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = t
                elif asc is False and nums[j] < nums[j+1]:
                    t = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = t
        return nums

    def charupaixu(self, nums: [int], asc: bool) -> [int]:
        # 开辟额外存储空间的插入排序
        target = []
        countT = 0
        for tempN in nums:
            if countT == 0:
                target.append(tempN)
                countT += 1
            else:
                left = 0
                right = countT-1
                if tempN > target[right]:
                    target.append(tempN)
                elif tempN < target[left]:
                    target.insert(0, tempN)
                else:
                    while left < right:
                        mid = (left+right) // 2
                        if tempN >= target[mid]:
                            left = mid
                            if tempN < target[mid+1]:
                                break
                        else:
                            right = mid
                    target.insert(left+1, tempN)
                countT += 1
        if asc is False:
            target.reverse()
        return target

    def charupaixu2(self, nums: [int], asc: bool):
        # 使用原数组进行插入排序
        countN = len(nums)
        orderCount = 1
        for index in range(1, countN):
            tempN = nums[index]
            if tempN >= nums[orderCount-1]:
                orderCount += 1
                continue
            if tempN < nums[0]:
                nums.pop(index)
                nums.insert(0, tempN)
                orderCount += 1
                continue
            left = 0
            right = orderCount-1

            while left <= right:
                mid = (left+right) // 2
                if tempN >= nums[mid]:
                    left = mid
                    if nums[mid+1] > tempN:
                        break
                else:
                    right = mid
            nums.pop(index)
            nums.insert(left+1, tempN)
            orderCount += 1
        if asc is False:
            nums.reverse()

    def kuaisupaixu(self, nums: [int], asc: bool):
        self._kuaisupaixu(nums, 0, len(nums)-1)
        if asc is False:
            nums.reverse()

    def _kuaisupaixu(self, nums: [int], low: int, high: int):
        if low < high:
            p = self.getP(nums, low, high)
            print(1, nums)
            print(2, nums[low:p-1])
            print(3, nums[p+1:high])
            self._kuaisupaixu(nums, low, p-1)
            self._kuaisupaixu(nums, p+1, high)

    def getP(self, nums: [int], low: int, high: int) -> int:
        p = nums[low]
        while low < high:
            while low < high and nums[high] >= p:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= p:
                low += 1
            nums[high] = nums[low]
        nums[low] = p
        return low


tempNum = [1, 4, 6, 2, 7, 8, 3, 5, 0, 9]
# tempNum.sort()
# 选择排序
# Solution().xuanzepaixu(tempNum, True)
# Solution().xuanzepaixu(tempNum, False)
# print(tempNum)

# 冒泡排序
# Solution().maopaopaixu(tempNum, True)
# Solution().maopaopaixu(tempNum, False)
# print(tempNum)

# 插入排序
# print(Solution().charupaixu(tempNum, True))
# print(Solution().charupaixu(tempNum, False))

# 插入排序2
# Solution().charupaixu2(tempNum, True)
# Solution().charupaixu2(tempNum, False)
# print(tempNum)

# 快速排序
# Solution().kuaisupaixu(tempNum, True)
Solution().kuaisupaixu(tempNum, False)
print(tempNum)
