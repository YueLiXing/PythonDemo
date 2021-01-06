/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */
class Solution {
    func reverseBetween(_ head: ListNode?, _ m: Int, _ n: Int) -> ListNode? {
        var current:ListNode? = head
        var pre:ListNode? = nil
        var index = 1
        while index < m {
            pre = current
            current = current?.next
            index += 1
        }
        
        let con = pre
        let tail = current
        while index <= n {
            let tempN = current?.next
            current?.next = pre
            pre = current
            current = tempN
            index += 1
        }
        tail?.next = current
        if con == nil {
            return pre
        } else {
            con?.next = pre
            return head
        }
    }
}