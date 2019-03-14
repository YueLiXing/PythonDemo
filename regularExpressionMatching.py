class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lenP = len(p)
        lenS = len(s)
        if lenP == 0:
            return lenS == 0
        elif lenP == 1:
            return lenS == 1 and (s[0] == p[0] or p[0] == '.')
        
        if p[1] != '*':
            if lenS == 0:
                return False
            return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        
        while lenS > 0 and (s[0] == p[0] or p[0] == '.'):
            if self.isMatch(s, p[2:]):
                return True
            s = s[1:]
            lenS -= 1

        return self.isMatch(s, p[2:])

Solution().isMatch("aa","a*")