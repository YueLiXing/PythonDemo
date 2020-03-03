class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        lenOfS = len(s)
        self.cache = set()
        for index in range(lenOfS):
            end = index+2
            count += 1
            while end <= lenOfS:
                if self.judgePalindrome(s[index:end]):
                    count += 1
                end += 1
        return count

    def judgePalindrome(self, s: str) -> bool:
        if s in self.cache:
            return True
        lenOfS = len(s)
        for index in range(lenOfS//2):
            if s[index] != s[lenOfS-1-index]:
                return False
        self.cache.add(s)
        return True


Solution().countSubstrings("abc")
