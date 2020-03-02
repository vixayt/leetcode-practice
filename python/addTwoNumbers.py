class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        carry = 0
        head = current = ListNode(0)
        while p1 or p2:
            p1_val = 0 if p1 is None else p1.val
            p2_val = 0 if p2 is None else p2.val

            sum = p1_val + p2_val + carry
            if sum >= 10:
                carry = 1
                sum -= 10
            else: 
                carry = 0
            current.next = ListNode(sum)
            current = current.next
            if p1 is not None:
                p1 = p1.next
            if p2 is not None:
                p2 = p2.next
            if carry > 0:
                current.next = ListNode(carry)
 
        return head.next
