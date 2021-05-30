class Solution {
    func findMin(_ nums: [Int]) -> Int {
        for index in 0..<nums.count-1 {
            if nums[index] > nums[index+1] {
                return nums[index+1]
            }
        }
        return nums[0]
    }
}