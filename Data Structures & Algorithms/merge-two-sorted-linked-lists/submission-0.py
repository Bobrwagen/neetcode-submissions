# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        head = list1 if list1.val < list2.val else list2
        if list1.val < list2.val:
            list1 = list1.next
        else:
            list2 = list2.next
        res = head
        while list1 is not None or list2 is not None:
            if list1 is None:
                res.next = list2
                list2 = list2.next
                res = res.next

            elif list2 is None:
                res.next = list1
                list1 = list1.next
                res = res.next
            else:
                if list1.val < list2.val:
                    res.next = list1
                    list1 = list1.next
                    res = res.next
                else:
                    res.next = list2
                    list2 = list2.next
                    res = res.next
        
        return head

        