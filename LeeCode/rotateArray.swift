class Solution {
    func resverse(_ nums: inout [Int], _ start: Int, _ end: Int) {
        for index in start..<(start+end)/2 {
            nums.swapAt(index, end-(index-start))
        }
    }
    func rotate(_ nums: inout [Int], _ k: Int) {
        if nums.count < 2 {
            return
        }
        let newK = k%nums.count
        if newK == 0 {
            return
        }
        resverse(&nums, 0, nums.count)
        resverse(&nums, 0, newK)
        resverse(&nums, newK+1, nums.count)
    }
    
//    func rotate(_ nums: inout [Int], _ k: Int) {
//        if nums.count < 2 {
//            return
//        }
//        let newK = k%nums.count
//        if newK == 0 {
//            return
//        }
//
//        var count = 0
//        var start = 0
//        while count != nums.count {
//            var current = start
//            let temp = nums[current]
//            while true {
//                var next = current-newK
//                if next < 0 {
//                    next = nums.count+next
//                }
//                nums[current] = nums[next]
//                count += 1
//                if next == start {
//                    nums[current] = temp
//                    break
//                }
//                current = next
//                if count == nums.count {
//                    return
//                }
//            }
//            start += 1
//        }
//    }
}
