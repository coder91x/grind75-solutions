# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return head
        
        slow = head
        fast = head.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        prev = None

        while second != None:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        
        dummy = ListNode(-1)
        mergePointer = dummy

        first = head
        sec = prev
        while first and sec:
            mergePointer.next = first
            first = first.next
            mergePointer = mergePointer.next

            mergePointer.next = sec
            sec = sec.next
            mergePointer = mergePointer.next
        
        mergePointer.next = first







        
