class Solution:
    def countOfAtoms(self, formula: str) -> str:
        targetDict = {}
        targetDict.update({'a': 1})
        print(targetDict)
        self.mergeDict(targetDict, {'a': 2})
        # targetDict.update({'a': 2})
        print(targetDict)
        return ""

    def mergeDict(self, target: dict, soue: dict):
        for k, v in soue.items():
            if k in target:
                target[k] = target[k] + v
            else:
                target[k] = v


Solution().countOfAtoms("K4(ON(SO3)2)2")
###
# formula = "K4(ON(SO3)2)2"
# 输出: "K4N2O14S4"
###
