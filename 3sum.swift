
class Solution {
    func threeSum(_ nums: [Int]) -> [[Int]] {
        if nums.count < 3 {
            return []
        }
        let tempN = nums.sorted(by: <)
        var result = [[Int]]()
        for index in 0..<tempN.count-2 {
            if tempN[index] > 0 {
                break
            }
            if index > 0 && tempN[index] == tempN[index-1] {
                continue
            }
            var left = index+1
            var right = tempN.count-1
            while left < right {
                let s = tempN[index]+tempN[left]+tempN[right]
                if s == 0 {
                    result.append([tempN[index], tempN[left], tempN[right]])
                    while left < right && tempN[left] == tempN[left+1] {
                        left += 1
                    }
                    left += 1
                    while left < right && tempN[right] == tempN[right-1] {
                        right -= 1
                    }
                    right -= 1
                } else if s > 0 {
                    right -= 1
                } else {
                    left += 1
                }
            }
        }
        return result
    }
}