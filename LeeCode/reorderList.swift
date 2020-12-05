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
    func reverseListNode(_ head: ListNode?) -> ListNode? {
        var current = head
        var pre:ListNode? = nil
        while current != nil {
            let tempN = current?.next
            current?.next = pre
            pre = current
            current = tempN
        }
        return pre
    }
    func printList(_ head: ListNode?) {
        var cacheArr = [Int]()
        var temp = head
        while temp != nil {
            cacheArr.append(temp!.val)
            temp = temp?.next
        }
        print(cacheArr)
    }
    func getMidNode(_ head: ListNode?) -> ListNode? {
        var slow = head
        var fast = head
        while fast != nil {
            if fast?.next == nil || fast?.next?.next == nil {
                return slow
            }
            slow = slow?.next
            fast = fast?.next?.next
        }
        return slow
    }
    func reorderList(_ head: ListNode?) {
        var mid = self.getMidNode(head)
        // print("mid: \(mid?.val)")
        var last = self.reverseListNode(mid?.next)
        mid?.next = nil
        var temp = head
        var temp1 = last
        while temp != nil {
            let tempN = temp?.next
            let tempN1 = temp1?.next
            temp?.next = temp1
            temp1?.next = tempN
            temp = tempN
            temp1 = tempN1
        }
        // self.printList(head)
        // self.printList(last)
    }
}