class Solution {
    func longestValidParentheses(_ s: String) -> Int {
        var maxLength = 0
        let sArr = Array(s)
        var count0 = 0
        var count1 = 0
        sArr.forEach { (tempC) in
            if tempC == "(" {
                count0 += 1
            } else {
                count1 += 1
            }
        }
        let possMaxCount = min(count0, count1)*2
        for index in 0..<sArr.count {
            if sArr[index] == "(" {
                var left = 0
                var right = 0
                var tempCount = 0
                for j in index..<min(possMaxCount+index, sArr.count) {
                    if sArr[j] == "(" {
                        left += 1
                    } else {
                        right += 1
                    }
                    if left == right {
                        tempCount = left*2
                    }
                    if right > left {
                        break
                    }
                }
                maxLength = max(maxLength, tempCount)
            }
            if index + maxLength == sArr.count {
                break
            }
        }
        return maxLength
    }
}