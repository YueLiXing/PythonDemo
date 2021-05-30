class Solution {
    func pivotIndex(_ nums: [Int]) -> Int {
        var allSum = 0
        nums.forEach { (temp) in
            allSum += temp
        }
        var leftSum = 0
        var rightSum = allSum
        if nums.count > 0 {
            for index in 0..<nums.count {
                let temp = nums[index]
                rightSum = rightSum-temp
                if leftSum == rightSum {
                    return index
                }
                leftSum += temp
            }
        }
        return -1
    }
}