class Solution {
    func insert(_ intervals: [[Int]], _ newInterval: [Int]) -> [[Int]] {
        var result = [[Int]]()
        var bufferInter: [Int]? = newInterval
        intervals.forEach { (tempInter) in
            if bufferInter == nil {
                result.append(tempInter)
            } else {
                if tempInter[0] > bufferInter![1] {
                    result.append(bufferInter!)
                    bufferInter = nil
                    result.append(tempInter)
                } else {
                    if tempInter[1] >= bufferInter![0] {
                       bufferInter = [min(tempInter[0], bufferInter![0]), max(tempInter[1], bufferInter![1])]
                    } else {
                        result.append(tempInter)
                    }
                }
            }
        }
        if bufferInter != nil {
            result.append(bufferInter!)
        }
        return result
    }
}