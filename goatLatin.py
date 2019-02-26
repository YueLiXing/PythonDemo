class Solution:
    def toGoatLatin(self, S: 'str') -> 'str':
        arr = S.split(" ")
        ret = ""
        count = 1
        l = len(arr)
        cacheAEIOU = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        for index in range(l):
            tempS = arr[index]
            firstC = tempS[0]
            if firstC not in cacheAEIOU:
                tempS = tempS[1:]+firstC
            tempS += "ma"
            for i in range(count):
                tempS += "a"
            count += 1
            ret+=tempS
            if index+1<l:
                ret+= " "
        return ret


Solution().toGoatLatin("I speak Goat Latin")
