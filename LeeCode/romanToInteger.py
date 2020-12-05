class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        valueDict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        ret = 0
        lastC = None
        for tempC in s:
            print(tempC)
            lastValue = 0 if lastC is None else valueDict[lastC]
            curValue = valueDict[tempC]
            if curValue > lastValue:
                ret = ret-2*lastValue+curValue
            else:
                ret += curValue
            lastC = tempC
        # print(ret)
        return ret
                

print(Solution().romanToInt("III"))
