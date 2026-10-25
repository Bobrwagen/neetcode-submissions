# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = l1
        carry = 0
        while l1 and l2:
            new_carry = 0
            if l1.val + l2.val + carry > 9:
                new_carry = (l1.val + l2.val + carry) // 10
            l1.val = (l1.val + l2.val + carry) % 10
            carry = new_carry
            dummy.next = l1
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            new_carry = 0
            if l1.val + carry > 9:
                new_carry = 1
            l1.val = (l1.val + carry) % 10
            carry = new_carry
            dummy.next = l1
            dummy = dummy.next
            l1 = l1.next
        while l2:
            new_carry = 0
            if l2.val + carry > 9:
                new_carry = 1
            l2.val = (l2.val + carry) % 10
            carry = new_carry
            dummy.next = l2
            dummy = dummy.next
            l2 = l2.next
        if carry:
            dummy.next = ListNode(1)
        return head

        