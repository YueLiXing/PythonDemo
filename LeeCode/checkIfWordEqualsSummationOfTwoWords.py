# class Solution:
#     def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
#         num0 = 0
#         num1 = 0
#         ret = 0
#         for tempC in firstWord:
#             temp = ord(tempC)-ord('a')
#             num0 = num0*10 + temp
#         for tempC in secondWord:
#             temp = ord(tempC)-ord('a')
#             num1 = num1*10 + temp
#         for tempC in targetWord:
#             temp = ord(tempC)-ord('a')
#             ret = ret*10 + temp
#         return num0 + num1 == ret


class Solution:
    def maxValue(self, n: str, x: int) -> str:
        num = int(n)
        index = -1
        if num > 0:
            for tempIndex in range(len(n)):
                tempC = n[tempIndex]
                temp = ord(tempC)-ord('0')
                if temp <= x:
                    index = tempIndex
                    break
            if index == -1:
                index = len(n)
        else:
            for tempIndex in range(1, len(n), 1):
                tempC = n[tempIndex]
                temp = ord(tempC)-ord('0')
                if temp >= x:
                    index = tempIndex
                    break
            if index == -1:
                index = len(n)
        listN = list(n)
        listN.insert(index, str(x))
        return ''.join(listN)
                    

print(Solution().maxValue('999', 9) == "9999")
print(Solution().maxValue('-32', 1) == "-132")
# print(Solution().maxValue('-12', 9))
print(Solution().maxValue('-12', 9) == "-129")
print(Solution().maxValue('-648468153646', 5) == "-5648468153646")

# Solution().isSumEqual('aaa', 'a', 'aaaa')
