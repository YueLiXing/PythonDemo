class Solution {
    func backspaceCompare(_ S: String, _ T: String) -> Bool {
        var s0 = ""
        var s1 = ""
        S.forEach { (tempC) in
            if tempC == "#" {
                let _ = s0.popLast()
            } else {
                s0.append(tempC)
            }
        }
        T.forEach { (tempC) in
            if tempC == "#" {
                let _ = s1.popLast()
            } else {
                s1.append(tempC)
            }
        }
        return s0 == s1
    }
}