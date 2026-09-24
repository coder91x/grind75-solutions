# Reorder List

[Open on LeetCode](https://leetcode.com/problems/reorder-list) · Medium · Linked List

Status: Solved with Help
Date solved: 2026-09-23
Attempts: 2
Confidence: 0/5

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

Find the end of the first half using slow/fast pointers. Split the list, reverse the second half, then alternate one node from the first half and one from the reversed second half.
mportant details: slow = head, fast = head.next makes slow stop at the end of the first half, which is useful for both odd and even lengths. For reversal, remember SAVE → REVERSE → MOVE PREV → MOVE CURR; prev is always the head of the already-reversed portion, so it becomes the new head when reversal finishes. While weaving, advance each pointer before its old .next gets overwritten.
My key mistake / lesson:
Changing pointer only moves my reference; changing pointer.next actually changes the linked-list structure. Also, after reversing, the traversal pointer becomes None; prev is the head of the reversed list.
Complexity: O(n) time, O(1) extra space.
Pattern to recognize later:
When a linked-list problem needs nodes from the front and back alternately, consider: find middle → reverse second half → merge/weave.
