class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        # cache = []
        target = ""
        for word in words:
            temp = ""
            for c in word:
                temp = c+temp
            target += temp+" "
        #     cache.append(temp)
        # return " ".join(cache)
        return target[:-1]


print(Solution().reverseWords("Let's take LeetCode contest"))
