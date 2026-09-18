# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                ptr1 = head
                ptr2 = fast
                while ptr1 != ptr2:
                    ptr1 = ptr1.next
                    ptr2 = ptr2.next
                
                if ptr1 == ptr2:
                    return ptr1
            
        return None
