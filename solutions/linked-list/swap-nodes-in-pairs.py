# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while prev.next != None and prev.next.next != None:
            first = prev.next #first = -1.next = 1
            second = first.next #second = 1.next = 2
            after_pair = second.next # after_pair = 3 onwards
            prev.next = second # -1.next = 2   -1 ---> 2
            second.next = first # 2.next = 1 2 ---> 1
            first.next = after_pair # 1.next = 3 1 ---> 3
            prev = first # prev = 1
            # after first iteration -1 ---> 2 ----> 1 ----> 3 and prev will become 1
        
        return dummy.next
