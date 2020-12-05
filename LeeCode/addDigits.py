class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 10:
            temp = []
            while num > 0:
                temp.append(num % 10)
                num = num // 10
            num = sum(temp)
        return num
