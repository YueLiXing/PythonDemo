class Solution:
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        bufferArr = []
        unBufferArr = []
        resultDict = {}
        def judgeIsPal(s):
                if len(s) >= 2:
                    if len(s) == 2:
                        return s[0:1] == s[1:2]
                    else:
                        l = len(s)
                        midS = s[1:l-1]
                        if midS in bufferArr:
                            return s[0:1] == s[l-1:l]
                        elif midS in unBufferArr:
                            return False
                        else:
                            for index in range(len(s)//2):
                                if s[index:index+1] != s[len(s)-1-index:len(s)-index]:
                                    return False
                            return True
                else:
                    return True
        count = 0
        subCount = 0
        for start in range(len(S)):
            for end in range(start+1,len(S)+1):
                tempS = S[start:end]
                subCount += 1
                if tempS in resultDict:
                    count += 1
                    # print(tempS)
                elif judgeIsPal(tempS):
                    resultDict[tempS] = ""
                    # print(tempS)
                    count += 1
        # print(resultDict)
        print(subCount)
        # print(count % (10**9+7))
        return count % (10**9+7)


Solution().countPalindromicSubsequences(
    "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba")

