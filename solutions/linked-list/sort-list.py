# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        #       4 ---> 2 ---> 1 ---> 3
                    #  find mid
                # 4---> 2 and 1 ---> 3
                # keep dividing until they become individual nodes as indivdual nodes are sorted and then merge them into new list by comparing their values    


        if head is None or head.next is None:
            return head
        
        slow = fast = head

        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        dummy = ListNode(-1)
        mergePointer = dummy

        while left and right:
            if left.val < right.val:
                mergePointer.next = left
                left = left.next
            else:
                mergePointer.next = right
                right = right.next

            mergePointer = mergePointer.next
        
        if left:
            mergePointer.next = left
        else:
            mergePointer.next = right
        
        return dummy.next
