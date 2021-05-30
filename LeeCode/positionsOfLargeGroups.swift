class Solution {
    func largeGroupPositions(_ s: String) -> [[Int]] {
        var result = [[Int]]()
        var lastC: Character? = nil
        var lastIndex:Int = 0
        var count = 0
        var currentIndex = 0
        
        s.forEach { (tempC) in
            if lastC == nil {
                lastC = tempC
                count = 1
                lastIndex = currentIndex
            } else {
                currentIndex += 1
                if lastC == tempC {
                    count += 1
                } else {
                    if count >= 3 {
                        result.append([lastIndex, currentIndex-1])
                    }
                    lastIndex = currentIndex
                    lastC = tempC
                    count = 1
                }
            }
        }
        if count >= 3 {
            result.append([lastIndex, currentIndex])
        }
        return result
    }
}
