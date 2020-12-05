class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        cacheArray = []
        countDict = {
            "a": 0,
            "e": 0,
            "i": 0,
            "o": 0,
            "u": 0
            }
        for c in s:
            if c in countDict:
                countDict[c] += 1
        self.travel(countDict.copy(), s, cacheArray)

        ret = 0
        for tempS in cacheArray:
            ls = len(tempS)
            if ls > ret:
                ret = ls
        return ret
    
    def judge(self, countDict):
        return countDict["a"] % 2 == 0 and countDict["e"] % 2 == 0 and countDict["i"] % 2 == 0 and countDict["o"] % 2 == 0 and countDict["u"] % 2 == 0

    def travel(self, countDict: dict, s: str, tempArr: [str]):
        # print(s)
        flag = True
        for v in countDict.values():
            if v % 2 != 0:
                flag = False
                break
        if flag:
            tempArr.append(s)
            return
        # print("deal", s, countDict)
        lenS = len(s)
        index = 0
        cpcd0 = countDict.copy()
        while index < lenS:
            c = s[index]
            if c in cpcd0:
                cpcd0[c] -= 1
                if cpcd0[c] % 2 == 0:
                    self.travel(cpcd0, s[index+1:lenS], tempArr)
                    break

            index += 1
        index = 0
        end = lenS-1
        cpcd1 = countDict.copy()
        while index < end:
            c = s[end]
            if c in cpcd1:
                cpcd1[c] -= 1
                if cpcd1[c] % 2 == 0:
                    self.travel(cpcd1, s[index:end], tempArr)
                    break
            end -= 1


print(Solution().findTheLongestSubstring("bcbcbc"))
print(Solution().findTheLongestSubstring("eleetminicoworoep"))
print(Solution().findTheLongestSubstring("qnplnlarrtztkotazhufrsfczrzibvccaoayyihidztfljcffiqfviuwjowkppdajmknzgidixqgtnahamebxfowqvnrhuzwqohquamvszkvunbxjegbjccjjxfnsiearbsgsofywtqbmgldgsvnsgpdvmjqpaktmjafgkzszekngivdmrlvrpyrhcxbceffrgiyktqilkkdjhtywpesrydkbncmzeekdtszmcsrhsciljsrdoidzbjatvacndzbghzsnfdofvhfxdnmzrjriwpkdgukbaazjxtkomkmccktodig"))

