class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list = []
        for tempS in s:
            if tempS == "{" or tempS == "[" or tempS == "(":
                list.append(tempS)
            else:
                if len(list) == 0:
                    return False
                if tempS == "}":
                    last = list.pop()
                    if last == "{":
                        continue
                    else:
                        return False
                elif tempS == "]":
                    last = list.pop()
                    if last == "[":
                        continue
                    else:
                        return False
                elif tempS == ")":
                    last = list.pop()
                    if last == "(":
                        continue
                    else:
                        return False
        if len(list) > 0:
            return False
        else:
            return True

Solution().isValid("{([])}")
