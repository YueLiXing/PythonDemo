# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 因为自己写的老是超时，所以看了官方解析。采用中心扩散法
# 一个长度为 n 的字符串，有可能出现回文子串的中心个数为 2*n-1 个
# 遍历这些中心数，向两边扩散。


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        tempChar = s[0:1]
        maxLongS = tempChar
        bufferArr = [maxLongS]
        unBufferArr = []
        flag = True
        for index in range(1,len(s)):
            tempS = s[index:index+1]
            if tempChar != tempS:
                flag = False
                break
            else:
                maxLongS += tempS
                bufferArr.append(maxLongS)
        if flag:
            return s
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
        index = 0
        for index in range(2*len(s)-1):
            tempS = ""
            start = 0
            end = 0
            if index % 2 == 0:  # 当前中心为某一个字符
                start = index//2
                end = index//2+1
            else:  # 当前中心在字符中间位置
                start = index//2
                end = index//2+2
            # print("index:%d start:%d end:%d " % (index, start, end))
            while start >= 0 and end <= len(s):
                tempS = s[start:end]
                # print(tempS, start, end)
                if tempS in unBufferArr:
                    break
                if tempS in bufferArr:
                    start -= 1
                    end += 1
                    continue
                flag = judgeIsPal(tempS)
                if flag:
                    bufferArr.append(tempS)
                    maxLongS = tempS if len(tempS) >= len(maxLongS) else maxLongS
                    start -= 1
                    end += 1
                    if len(maxLongS) == len(s):
                        return maxLongS
                else:
                    unBufferArr.append(tempS)
                    break
        return maxLongS
                    
import time
startTime = time.time()
# print(Solution().longestPalindrome("cbbd"))
# print(Solution().longestPalindrome("bb"))
print(Solution().longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))
# print(Solution().longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))
print(time.time()-startTime)
startTime = time.time()
Solution().longestPalindrome("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
print(time.time()-startTime)
startTime = time.time()
Solution().longestPalindrome("1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
print(time.time()-startTime)
