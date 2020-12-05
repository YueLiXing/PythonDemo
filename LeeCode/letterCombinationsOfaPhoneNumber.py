class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        tempDict = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        tempArr = []
        totalRet = 1
        for tempC in digits:
            tempS = tempDict[tempC]
            tempArr.append(tempS)
            totalRet *= len(tempS)
        restArr = []
        index = 0
        while index < totalRet:
            targetS = ""
            tempI = index
            for tempS in tempArr:
                targetS += tempS[int(tempI % len(tempS)):int(tempI % len(tempS)+1)]
                tempI /= len(tempS)
            restArr.append(targetS)
            index += 1
        return restArr

Solution().letterCombinations("23")
