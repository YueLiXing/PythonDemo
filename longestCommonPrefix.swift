class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        guard strs.count > 0 else {
            return ""
        }
        if strs.count == 1 {
            return strs[0]
        }
        let arr = strs.sorted { (s0, s1) -> Bool in
            return s0.count < s1.count
        }
        var left = 0
        var right = arr[0].count-1
        while left < right {
            let mid = (left+right+1)/2
            var cacheS: Substring? = nil
            for index in 0..<arr.count {
                let tempS = arr[index]
                let startIndex = tempS.startIndex
                let endIndex = tempS.index(startIndex, offsetBy: mid)
                
                if index == 0 {
                    cacheS = tempS[startIndex...endIndex]
                } else {
                    let subS = tempS[startIndex...endIndex]
                    if cacheS == subS {
                        left = mid
                    } else {
                        right = mid-1
                    }
                }
            }
        }
        let tempS = arr[0]
        let startIndex = tempS.startIndex
        let endIndex = tempS.index(startIndex, offsetBy: (left+right)/2)
//        print(left, right)
        return String(tempS[startIndex...endIndex])
    }
}