class Solution:
    def reverseWords(self, s: str) -> str:
        target = ""
        cache = ""
        flag = False
        for c in s:
            if c == " ":
                flag = True
                continue
            else:
                if flag:
                    if len(target) > 0:
                        target = cache+" "+target
                    else:
                        target = cache
                    cache = c
                    flag = False
                else:
                    cache += c
        if len(cache) > 0:
            if len(target) > 0:
                target = cache+" "+target
            else:
                target = cache
        return target