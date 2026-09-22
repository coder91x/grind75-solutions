# Sort List

[Open on LeetCode](https://leetcode.com/problems/sort-list) · Medium · Linked List

Status: Solved with Help
Date solved: 2026-09-22
Attempts: 1
Confidence: 3/5

## First Instinct

_No notes yet._

## Key Observation

_No notes yet._

## Pattern/Invariant

_No notes yet._

## Mistake

_No notes yet._

## Complexity

_No notes yet._

## Disguised Version clues

_No notes yet._

## Review Notes

Here, the idea is we have to keep on dividing the list until we get individual nodes. How we divide is that basically we create a recursive case, like the base case is that if the head is equal to none, or head.next is equal to none, then return head. So either head will be returned as none, or head will be returned as the only element remaining. Then we find the midpoint by using slow and fast pointer. But as we know that we have to cut the list before the midpoint, so we store the slow before incrementing it. So basically previous is equal to slow, slow is equal to slow.next, fast is equal to fast.next.next. And then, after that is done, we cut the link. So previous.next is equal to none. After that we create a dummy node, and also we create a merge pointer starting at that dummy node. And while left and right, we, if the left.val is less than right.val, we basically add the left value by doing merge.next is equal to left, and then left is equal to left.next, else we do with the right. And then at the end, if both, if left is remaining, we just left merge the remaining left, and if right is remaining, we merge the remaining right. And in the end, we return dummy.next.
