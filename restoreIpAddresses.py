class Solution:
    def restoreIpAddresses(self, s):

        def valid(tempS):
            tempI = int(tempS)
            if 0 < tempI <= 255:
                return tempS[:1] != '0'
            elif tempI == 0:
                return len(tempS) == 1
            else:
                return False

        def update_output(curr_pos):
            segment = s[curr_pos + 1:lenS]
            if valid(segment):
                cacheIp.append(segment)
                output.append('.'.join(cacheIp))
                cacheIp.pop()

        def backtrack(prePos=0, dots=3):
            for curPos in range(prePos, min(lenS-1, prePos+3)):
                tempS = s[prePos:curPos+1]
                if valid(tempS):
                    cacheIp.append(tempS)
                    if dots == 1:
                        update_output(curPos)
                    else:
                        backtrack(curPos+1, dots-1)
                    cacheIp.pop()
        lenS = len(s)
        output, cacheIp = [], []
        backtrack()
        return output


print(Solution().restoreIpAddresses("25525511135"))
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
