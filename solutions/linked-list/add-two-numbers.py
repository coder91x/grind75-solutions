# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1)
        total = 0
        carry = 0
        head = dummy
        while l1 != None or l2 != None:
            val1 = l1.val if l1 != None else 0
            val2 = l2.val if l2 != None else 0
            total = val1 + val2 + carry
            l3 = ListNode(total%10)
            carry = total // 10
            dummy.next = l3
            dummy = dummy.next
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        
        if carry:
            car = ListNode(carry)
            l3.next = car
        
        return head.next
