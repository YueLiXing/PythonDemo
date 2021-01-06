/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func swapPairs(_ head: ListNode?) -> ListNode? {
        var temp = head
        var h: ListNode? = head
        var pre: ListNode? = nil
        while temp != nil && temp?.next != nil {
            let tempN = temp?.next?.next
            if pre != nil {
                pre?.next = temp?.next
                temp?.next?.next = temp
                pre = temp
                temp?.next = tempN
                temp = tempN
            } else {
                h = temp?.next
                pre = temp
                h?.next = temp
                temp?.next = tempN
                temp = tempN
            }
        }
        return h
    }
}