class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # lows = s.lower()
        cacheArr = []
        for c in s:
            cacheArr.append(c)
        front = 0
        last = len(cacheArr)-1
        while front < last:
            if cacheArr[front] == cacheArr[last]:
                front += 1
                last -= 1
            else:
                return False
        return True

    def palindromePairs(self, words: [str]) -> [[int]]:
        target = []
        lenOfWords = len(words)
        for indexI in range(lenOfWords):
            s1 = words[indexI]
            len1 = len(s1)
            for indexJ in range(indexI+1, lenOfWords):
                s2 = words[indexJ]
                len2 = len(s2)
                # print(s1, s2)
                # if -1 <= len(s1)-len(s2) <= 1:
                if len1 == len2:
                    pass
                if self.isPalindrome(s1+s2):
                    target.append([indexI, indexJ])
                if self.isPalindrome(s2+s1):
                    target.append([indexJ, indexI])

        return target


print(Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))

# 输出: [[0, 1], [1, 0], [3, 2], [2, 4]]
