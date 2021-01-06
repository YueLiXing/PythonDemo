class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        lastC = ""
        currentC = None
        indexN = 0
        indexT = 0
        while indexT < len(typed):
            indexN = min(indexN,len(name)-1)
            currentC = name[indexN]
            if typed[indexT] in [currentC,lastC]:
                if typed[indexT] == currentC:
                    lastC = currentC
                    indexT += 1
                    indexN += 1
                else:
                    indexT += 1
            else:
                return False
        if indexN < len(name):
            return False
        return True


print(Solution().isLongPressedName("pyplrz", "ppyypllr"))

