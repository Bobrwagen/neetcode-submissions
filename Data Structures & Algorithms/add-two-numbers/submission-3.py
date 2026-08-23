# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l = l1
        r = l2
        prev = None
        while l or r:
            if l and r:
                update = l.val + r.val + carry
                carry = 0
                if update >= 10:
                    carry = 1
                    update -= 10
                l.val = update
                prev = l
                l = l.next
                r = r.next
            elif l:
                update = l.val + carry
                carry = 0
                if update >= 10:
                    carry = 1
                    update -= 10
                l.val = update
                prev = l
                l = l.next
            elif r:
                if carry:
                    update = r.val + carry
                    carry = 0
                    if update >= 10:
                        carry = 1
                        update -= 10
                    r.val = update
                    prev.next = r
                    prev = prev.next
                    r = r.next
                else:
                    prev.next = r
                    prev = prev.next
                    break
        if carry:
            prev.next = ListNode(1)
        return l1
                
