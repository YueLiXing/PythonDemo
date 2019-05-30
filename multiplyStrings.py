class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ret = ""
        flag = 0
        l1 = len(num1)
        l2 = len(num2)
        index1 = l1-1
        index2 = l2-1
        while index1 >= 0 or index2 >= 0 or flag > 0:
            a = 0
            b = 0
            if index1 >= 0:
                a = int(num1[index1])
                index1 -= 1
            if index2 >= 0:
                b = int(num2[index2])
                index2 -= 1
            r = a+b+flag
            ret = str(r % 10)+ret
            flag = r//10
        return ret

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        tempResult = ""
        zeroCount = 0
        l2 = len(num2)
        l1 = len(num1)
        for index2 in range(l2-1,-1,-1):
            a = int(num2[index2])
            tempS = ""
            for i in range(zeroCount):
                tempS += "0"
            index1 = l1-1
            flag = 0
            while index1 >= 0 or flag > 0:
                b = 0
                if index1 >= 0:
                    b = int(num1[index1])
                r = a*b+flag
                flag = r//10
                tempS = str(r%10)+tempS
                index1 -= 1

            tempResult = self.addStrings(tempResult, tempS)
            zeroCount += 1
        return tempResult


print(Solution().multiply("9", "9"))
