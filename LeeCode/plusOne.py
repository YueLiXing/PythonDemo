class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        l = len(digits)
        index = l-1
        flag = 1
        while flag > 0:
            ret = flag
            if index >= 0:
                ret += digits[index]
                digits[index] = ret % 10
                index -= 1
            else:
                digits.insert(0,ret%10)
            flag = ret//10
        return digits


print(Solution().plusOne([9,9,9,9]))
