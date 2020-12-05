class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxCount = 0
        bufferArray = []
        bufferDict = {}
        index = 0
        while index < len(s):
            tempC = s[index:index+1]
            if tempC in bufferDict:
                maxCount = max(maxCount,len(bufferArray))
                tempRm = bufferArray.pop(0)
                while True:
                    if tempRm == tempC:
                        break
                    else:
                        del bufferDict[tempRm]
                        if len(bufferArray) > 0:
                            tempRm = bufferArray.pop(0)
                        else:
                            break
            bufferDict[tempC] = index
            bufferArray.append(tempC)
            maxCount = max(maxCount, len(bufferArray))
            index += 1
        # print(bufferDict)
        # print(maxCount)
        return maxCount


print(Solution().lengthOfLongestSubstring("aab"))  # 2
print(Solution().lengthOfLongestSubstring("dvdf"))  # 3
print(Solution().lengthOfLongestSubstring("abcabcbb"))  # 3
print(Solution().lengthOfLongestSubstring("pwwkew"))  # 3
print(Solution().lengthOfLongestSubstring("abba"))  # 2
print(Solution().lengthOfLongestSubstring("jlygy"))  # 4


