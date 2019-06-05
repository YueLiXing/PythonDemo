class Solution:
    def addBinary(self, num1: str, num2: str) -> str:

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
            ret = str(r % 2)+ret
            flag = r//2
        return ret


print(Solution().addBinary("100", "111"))
