class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s = {}
        for c in magazine:
            if c in s:
                s[c] = s[c]+1
            else:
                s[c] = 1
        for c in ransomNote:
            if c not in s:
                return False
            else:
                a = s[c]-1
                if a > 0:
                    s[c] = a
                else:
                    del s[c]
        return True


print(Solution().canConstruct("aa", "ab"))
