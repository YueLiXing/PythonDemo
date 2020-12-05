class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: [str]) -> [[str]]:
        if endWord not in wordList:
            return []
        target = []
        self.realFindLadder(beginWord, endWord, set(wordList), [], target)
        return target
    
    def realFindLadder(self, currentWord: str, endWord: str, wordSet: set, cacheArr: [str], target: [[str]]):
        cacheArr.append(currentWord)
        if len(target) > 0 and len(cacheArr) > len(target[0]):
            return
        if currentWord == endWord:
            if len(target) > 0:
                len0 = len(target[0])
                len1 = len(cacheArr)
                if len0 < len1:
                    return
                elif len0 == len1:
                    target.append(cacheArr)
                else:
                    target.clear()
                    target.append(cacheArr)
            else:
                target.append(cacheArr)
            return
        for tempWord in wordSet:
            if self.cmpWords(tempWord, currentWord) == 1:
                tempWordList = wordSet.copy()
                tempWordList.remove(tempWord)
                self.realFindLadder(tempWord, endWord, tempWordList, cacheArr.copy(), target)

    def cmpWords(self, word0: str, word1: str):
        count = 0
        for index in range(len(word0)):
            if word0[index] != word1[index]:
                count += 1
        return count


print(Solution().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
