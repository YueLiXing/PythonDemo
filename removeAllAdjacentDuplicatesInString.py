class Solution:
    def removeDuplicates(self, S: str) -> str:
        temp = []
        for c in S:
            if len(temp) > 0 and c == temp[-1]:
                temp.pop()
                continue
            else:
                temp.append(c)
        return "".join(temp)
"""
输入："abbaca"
输出："ca"
"""

print(Solution().removeDuplicates("abbaca"))
