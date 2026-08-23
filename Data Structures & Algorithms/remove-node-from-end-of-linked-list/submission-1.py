# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        if length == 1:
            return None
        if length == n:
            return head.next
        tmp = head
        prev = None
        counter = 0
        while tmp:
            if length - counter == n:
                prev.next = prev.next.next
                break
            else:
                prev = tmp
                tmp = tmp.next
                counter += 1
        return head

        