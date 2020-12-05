# 给定一个单词，你需要判断单词的大写使用是否正确。
# 我们定义，在以下情况时，单词的大写用法是正确的：
# 全部字母都是大写，比如"USA"。
# 单词中所有字母都不是大写，比如"leetcode"。
# 如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
# 否则，我们定义这个单词没有正确使用大写字母。
# 示例 1:
# 输入: "USA"
# 输出: True


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 1:
            return True
        firstLowIndex = -1
        bigCount = 0
        for index in range(len(word)):
            tempChar = word[index]
            if "a" <= tempChar and tempChar <= "z":
                firstLowIndex = index
                if bigCount > 1:
                    return False
            else:
                bigCount += 1
                if firstLowIndex >=0:
                    return False
        return True


print(Solution().detectCapitalUse("FFFFFFFFFFFFFFFFFFFFf"))
