class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        target = ""
        index = 0
        while True:
            cache = ""
            temp = s[index:index+k]
            for c in temp:
                cache = c+cache
            temp = s[index+k:index+2*k]
            cache += temp
            target += cache
            index += 2*k
            # print(target)
            if index >= len(s):
                break
        # target += s[k:]
        return target


print(Solution().reverseStr("abcdefg", 1))
