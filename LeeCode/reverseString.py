class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lenOfS = len(s)
        for index in range(lenOfS//2):
            t = s[index]
            s[index] = s[lenOfS-1-index]
            s[lenOfS-1-index] = t


