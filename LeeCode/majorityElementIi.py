import collections


class Solution:
    def majorityElement(self, nums: [int]) -> [int]:
        lenM = len(nums)
        if lenM == 0:
            return []
        cache = 0
        a = None
        b = None
        countA = 0
        countB = 0
        for index in range(lenM):
            t = nums[index]
            if t == a:
                countA += 1
                continue
            if t == b:
                countB += 1
                continue
            if countA == 0:
                a = t
                countA = 1
                continue
            if countB == 0:
                b = t
                countB = 1
                continue
            countA -= 1
            countB -= 1
        countA = countB = 0
        for t in nums:
            if t == a:
                countA += 1
            elif t == b:
                countB += 1
        target = []
        if countA > lenM / 3:
            target.append(a)
        if countB > lenM / 3:
            target.append(b)
        return target
    # def majorityElement(self, nums: [int]) -> [int]:
    #     count = collections.defaultdict(int)
    #     lenM = len(nums)
    #     for index in range(lenM):
    #         count[nums[index]] += 1
    #     target = []
    #     for k in count:
    #         v = count[k]
    #         if v > lenM/3:
    #             target.append(k)
    #     return target


# print(Solution().majorityElement([3, 2, 3]))
# print(Solution().majorityElement([3, 3, 4]))
# print(Solution().majorityElement([2, 2, 1, 3]))
print(Solution().majorityElement([1, 2, 2, 3, 2, 1, 1, 3]))
