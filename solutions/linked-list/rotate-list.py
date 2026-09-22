# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None:
            return None
        n = 1
        old_head = head
        new_tail = head
        while head.next != None:
            n += 1
            head = head.next
        old_tail = head
        k = k % n
        if k == 0:
            return old_head
        i = 0
        while i < n-k-1:
            new_tail = new_tail.next
            i += 1
        new_head = new_tail.next
        old_tail.next = old_head
        new_tail.next = None

        return new_head
