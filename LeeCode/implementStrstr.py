class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nLen = len(needle)
        if nLen == 0:
            return 0
        hLen = len(haystack)
        if nLen > hLen:
            return -1
        for index in range(hLen-nLen+1):
            i = 0
            while haystack[index+i] == needle[i]:
                i += 1
                if i == nLen:
                    return index

        return -1
