class Solution:
    def simplifyPath(self, path: str) -> str:
        array = path.split("/")
        target = []
        count = 0
        # print(array)
        for temp in array:
            if len(temp) > 0:
                if temp == ".":
                    continue
                elif temp == "..":
                    if count > 0:
                        target.pop()
                        count -= 1
                    continue
                else:
                    target.append(temp)
                    count += 1
        return "/"+"/".join(target)


# print(Solution().simplifyPath("/home//foo/"))
print(Solution().simplifyPath("/../"))
