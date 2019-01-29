class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        0             2n-1 3n-1 4n-1
        1       2n-2  2n
        3 2n-3        2n+1
        """
        if numRows == 1:
            return s
        resArr = []
        for i in range(numRows):
            resArr.append([])

        index = 0
        flag = 1
        currentN = 0
        while index < len(s):
            currentArr = resArr[currentN]
            currentArr.append(s[index:index+1])
            index += 1
            currentN += flag
            if currentN == numRows:
                currentN = numRows-2
                flag = -1
            if currentN == -1:
                currentN = 1
                flag = 1
        ret = ""
        for index in range(len(resArr)):
            currentArr = resArr[index]
            for i in range(len(currentArr)):
                ret += currentArr[i]

        return ret
        # print(resArr)


Solution().convert("AB", 1)
# Solution().convert("LEETCODEISHIRING",4)
