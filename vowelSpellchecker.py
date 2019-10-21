class Solution:
    def spellchecker(self, wordlist: [str], queries: [str]) -> [str]:
        ret = []
        orginCacheDict = {}
        cachaDict = {}
        retCacheDict = {}
        vowelList = set(['a', 'e', 'i', 'o', 'u'])
        for word in wordlist:
            if word not in orginCacheDict:
                orginCacheDict[word] = word
            temp = word.lower()
            if temp not in cachaDict:
                cachaDict[temp] = word
            newWord = temp
            for i in range(len(newWord)):
                if newWord[i] in vowelList:
                    newWord = newWord.replace(newWord[i], '*')
            
            if newWord not in cachaDict:
                # print(newWord,word)
                cachaDict[newWord] = word
        # print(cachaDict)
        for querWord in queries:
            if querWord in retCacheDict:
                ret.append(retCacheDict[querWord])
            else:
                if querWord in orginCacheDict:
                    s = orginCacheDict[querWord]
                    ret.append(s)
                    retCacheDict[querWord] = s
                else:
                    lQWord = querWord.lower()
                    if lQWord in cachaDict:
                        s = cachaDict[lQWord]
                        ret.append(s)
                        retCacheDict[querWord] = s
                    else:
                        newWord = lQWord
                        for i in range(len(newWord)):
                            if newWord[i] in vowelList:
                                newWord = newWord.replace(newWord[i], '*')
                        if newWord in cachaDict:
                            s = cachaDict[newWord]
                            ret.append(s)
                            retCacheDict[querWord] = s
                        else:
                            s = ""
                            ret.append(s)
                            retCacheDict[lQWord] = s
                    
        return ret

            

# 当查询完全匹配单词列表中的某个单词（区分大小写）时，应返回相同的单词。
# 当查询匹配到大小写问题的单词时，您应该返回单词列表中的第一个这样的匹配项。
# 当查询匹配到元音错误的单词时，您应该返回单词列表中的第一个这样的匹配项。
# 如果该查询在单词列表中没有匹配项，则应返回空字符串。

# 来源：力扣（LeetCode）
# 链接：https: // leetcode-cn.com/problems/vowel-spellchecker
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# ret = Solution().spellchecker(["KiTe", "kite", "hare", "Hare"], ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"])
ret = Solution().spellchecker(["KiTe", "kite", "hare", "Hare"], ["Kite"])
ret = Solution().spellchecker(["YellOw"], ["yeellow"])

print(ret)



