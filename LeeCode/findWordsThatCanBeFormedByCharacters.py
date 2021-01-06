import collections


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        charsDict = collections.defaultdict(int)
        for c in chars:
            charsDict[c] += 1
        for tempW in words:
            cache = collections.defaultdict(int)
            flag = True
            for c in tempW:
                cache[c] += 1
                if cache[c] > charsDict[c]:
                    flag = False
                    break
            if flag:
                count += len(tempW)
        return count
