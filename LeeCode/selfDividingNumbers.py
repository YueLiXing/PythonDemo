class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> [int]:
        ret = []
        for temp in range(left,right+1):
            tempS = set()
            a = temp
            while a > 0:
                tempDiv = a % 10
                a = a // 10
                tempS.add(tempDiv)
            if 0 in tempS:
                continue
            flag = True
            for tempA in tempS:
                if temp%tempA != 0:
                    flag = False
                    break
            if flag:
                ret.append(temp)
        return ret

print(Solution().selfDividingNumbers(1, 11))
