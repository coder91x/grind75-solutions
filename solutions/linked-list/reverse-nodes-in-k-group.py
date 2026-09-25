# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
       dummy = ListNode(-1)
       dummy.next = head
       group_prev = dummy

       while True:
        kth = group_prev
        group_start = group_prev.next
        
        i=0
        while i < k and kth != None:
            kth = kth.next
            i += 1
        
        if kth == None:
            break
        
        after_group = kth.next
        reverse_prev = after_group
        curr = group_start

        while curr != after_group:
            next_node = curr.next
            curr.next = reverse_prev
            reverse_prev = curr
            curr = next_node
        
        group_prev.next = reverse_prev
        group_prev = group_start

       return dummy.next
