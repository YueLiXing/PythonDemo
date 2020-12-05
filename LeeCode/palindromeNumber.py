# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# https://leetcode-cn.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        temp = []
        while x >= 10:
            temp.append(x%10)
            x = x//10
        if x > 0:
            temp.append(x)
        # print("temp: ",temp)
        # print((len(temp)//2), " count")
        flag = True
        for index in range(0, len(temp)//2):
            if temp[index] != temp[len(temp)-1-index]:
                flag = False
        return flag
test = Solution()
print(test.isPalindrome(123))
print(test.isPalindrome(12321))
print(test.isPalindrome(123321))
print(test.isPalindrome(-121))
print(test.isPalindrome(10))
