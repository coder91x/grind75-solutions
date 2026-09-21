# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        dumy = ListNode(-1)
        head = dumy

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                dumy.next = l1
                l1 = l1.next
            else:
                dumy.next = l2
                l2 = l2.next
            dumy = dumy.next
        
        if l1 != None:
            dumy.next = l1
        else:
            dumy.next = l2
        
        return head.next
