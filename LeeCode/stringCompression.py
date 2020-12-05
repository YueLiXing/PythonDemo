class Solution:
    def replaceChars(self, chars: [str], char: str, count: int, index: int):
        if count == 1:
            return
        targetArray = []
        temp = count
        while temp > 0:
            targetArray.insert(0, temp % 10)
            temp //= 10
        targetArray.insert(0, char)
        lenOfTarget = len(targetArray)
        for i in range(index, index+count):
            if i - index < lenOfTarget:
                chars[i] = str(targetArray[i-index])
            else:
                chars.pop(index+lenOfTarget)

    def compress(self, chars: [str]) -> int:
        lChars = len(chars)
        if lChars > 1:
            result = 0
            count = 0
            lastChar = ""
            for i in range(lChars-1, -1, -1):
                if i == 0:
                    if lastChar == chars[i]:
                        count += 1
                        self.replaceChars(chars, lastChar, count, 0)
                    else:
                        if count >= 2:
                            self.replaceChars(chars, lastChar, count, 1)

                        lastChar = chars[i]
                        count = 1
                if i == lChars-1:
                    count += 1
                    lastChar = chars[i]
                else:
                    if lastChar == chars[i]:
                        count += 1
                    else:
                        self.replaceChars(chars, lastChar, count, i+1)

                        lastChar = chars[i]
                        count = 1
            return len(chars)
        else:
            return lChars


t = [
    "a", "b", "b", "b", "b",
    "b", "b", "b", "b", "b",
    "b", "b", "b"
]
print(Solution().compress(t))
print(t)
