class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ret = 0
        flag = 1
        isStart = False
        for tempC in str:
            if tempC == " ":
                if isStart:
                    break
                else:
                    continue
            elif "0" <= tempC <= "9":
                if isStart == False:
                    isStart = True
                ret = ret*10+int(tempC)
            elif "+" == tempC or "-" == tempC:
                if isStart == False:
                    isStart = True
                    flag = 1 if "+" == tempC else -1
                else:
                    break
            else:
                break
        ret = ret*flag
        if -2147483648 > ret:
            return -2147483648
        elif ret > 2147483647:
            return 2147483647
        else:
            return ret


print(Solution().myAtoi("+-42"))
print(Solution().myAtoi(" -42"))
print(Solution().myAtoi("a 42"))
print(Solution().myAtoi(" 42 as"))
print(Solution().myAtoi(" -42 asd"))
