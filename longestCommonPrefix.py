class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs.first
        reult = ""
        minLength = 10000
        charIndex = 0
        tempChar = ""
        while True:
            flag = False
            for index in range(len(strs)):
                tempStr = strs[index]
                if charIndex == 0:
                    minLength = min(len(tempStr), minLength)
                if index == 0:
                    tempChar = tempStr[charIndex:charIndex+1]
                else:
                    if tempStr[charIndex:charIndex+1] == tempChar:
                        if index+1 == len(strs):
                            reult += tempChar
                        
                    else:
                        flag = True
                        break
            charIndex += 1
            if flag or charIndex > minLength:
                break
        return reult
        # 尝试分治法来着，失败了。。。
        # if len(strs) > 2:
        #     mid = len(strs)//2
        #     strs[:mid]
        #     strs[mid:]
        #     self.longestCommonPrefix
        # else:
        #     if len(strs) == 1:
        #         return strs.first
        #     else:
        #         result = ""
        #         str0 = strs[0]
        #         str1 = strs[1]
        #         for index in range(min(len(str0), len(str1))-1):
        #             if str0[index:index+1] == str1[index:index+1]:
        #                 result += str0[index:index+1]
        #             else:
        #                 break
        #         return result
    # def getCommonPrefix(self, strs0, strs1):
    #     if len(strs0) == 1 and len(strs1) == 1:
    #         result = ""
    #         str0 = strs0[0]
    #         str1 = strs1[0]
    #         for index in range(min(len(str0), len(str1))-1):
    #             if str0[index:index+1] == str1[index:index+1]:
    #                 result += str0[index:index+1]
    #             else:
    #                 break
    #         return result
    #     else:
    #         if len(strs0) > 1:
    #             mid = len(strs0)//2
    #             strs0[:mid]
    #             strs0[mid:]
    #             return self.getCommonPrefix()

test = Solution()
# print([0,1,2,3,4,5,6][:3])
# print([0,1,2,3,4,5,6][3:])
# print("123"[2:3])
print(test.longestCommonPrefix(["flower", "flow", "flight"]))

