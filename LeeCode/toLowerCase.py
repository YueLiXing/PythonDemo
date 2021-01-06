class Solution:
    def toLowerCase(self, str: str) -> str:
        newS = ""
        for c in str:
            if "A" <= c <= "Z":
                newS += chr(ord(c)+32)
            else:
                newS += c
        return newS


print(Solution().toLowerCase("AsdasdSD"))
