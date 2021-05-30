class Solution {
    func subarraysWithKDistinct(_ A: [Int], _ K: Int) -> Int {
        return countSubArraysK(A, K) - countSubArraysK(A, K-1)
    }
    // 计算 A 里连续，最大元素个数为K 的数组个数
    func countSubArraysK(_ A:[Int], _ K: Int) -> Int {
        let len = A.count
        var left = 0
        var right = 0
        var tempArr = [Int](repeating: 0, count: len+1)
        var count = 0
        var result = 0
        // [left, right) 左闭右开区间
        while right < len {
            if tempArr[A[right]] == 0 {
                count += 1
            }
            tempArr[A[right]] += 1
            right += 1
            while count > K {
                tempArr[A[left]] -= 1
                if tempArr[A[left]] == 0 {
                    count -= 1
                }
                left += 1
            }
            result += right-left
        }
        return result
    }
}