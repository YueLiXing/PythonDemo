class Solution:
    def decodeString(self, s: str) -> str:
        ret = ""
        cacheArr = []
        cacheCountArr = []
        tempCount = 0
        for c in s:
            if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
                if len(cacheArr) > 0:
                    cacheArr[-1] = cacheArr[-1]+c
                else:
                    ret += c
            elif '[' == c:
                cacheCountArr.append(tempCount)
                cacheArr.append("")
                tempCount = 0
            elif ']' == c:
                lastS = cacheArr.pop()
                lastCount = cacheCountArr.pop()
                if len(cacheArr) > 0:
                    cacheArr[-1] = cacheArr[-1]+lastS*lastCount
                else:
                    ret += lastS*lastCount
                tempCount = 0
            else:
                tempCount = tempCount*10+int(c)
        return ret


# print(Solution().decodeString("3[a]2[bc]"))
# print(Solution().decodeString("3[a2[c]]"))
print(Solution().decodeString("2[abc]3[cd]ef"))

