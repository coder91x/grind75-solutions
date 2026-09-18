# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        fast = slow = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        if fast != None:
            sp = slow.next
        else:
            sp = slow
        
        prev = None
        while sp != None:
            next_node = sp.next
            sp.next = prev
            prev = sp
            sp = next_node
        
        while prev != None:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True
