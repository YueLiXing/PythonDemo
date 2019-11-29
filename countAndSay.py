class Solution:
    def countAndSay(self, n: int) -> str:
        index = 1
        tempS = "1"
        while index < n and n > 1:
            count = 0
            temp = ""
            lasChar = ""
            l = len(tempS)
            for i in range(l+1):
                if i == l:
                    if count > 0:
                        temp += "%d%s" % (count, lasChar)
                    break
                # print(tempS[i])
                if i == 0:
                    lasChar = tempS[i]
                    count += 1
                else:
                    if tempS[i] == lasChar:
                        count += 1
                    else:
                        temp += "%d%s" % (count, lasChar)
                        count = 1
                        lasChar = tempS[i]
            tempS = temp
            # print(tempS)
            index += 1
        return tempS


# print(Solution().countAndSay(1))
# print(Solution().countAndSay(2))
print(Solution().countAndSay(4))
