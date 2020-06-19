class Solution {
    func isPalindrome(_ s: String) -> Bool {
        let tempS = s.lowercased()
        var cacheArr = [Character]()
        tempS.forEach { (c) in
            if ("a" <= c && c <= "z") || ("0" <= c && c <= "9") {
                cacheArr.append(c)
            }
        }
        let count = cacheArr.count
        var front = 0
        var end = count-1
        while front < end {
            let fc = cacheArr[front]
            let lc = cacheArr[end]
            if fc == lc {
                front += 1
                end -= 1
            } else {
                return false
            }
        }
        return true
    }
}