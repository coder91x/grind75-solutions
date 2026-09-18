# Palindrome Linked List

[Open on LeetCode](https://leetcode.com/problems/palindrome-linked-list) · Easy · Linked List

Status: Solved with Help
Date solved: 2026-09-18
Attempts: 2
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

We first use slow and fast pointers to find the midpoint. When the loop finishes, if fast != None, the list has an odd number of nodes, so slow is the middle node and we skip it by starting the second half at slow.next. If fast == None, the list is even, and slow is already the first node of the second half.
Then we reverse the second half of the linked list. After reversal, prev points to the head of that reversed half.
Finally, we compare nodes starting from head and prev. While prev != None, if head.val != prev.val, we immediately return False. Otherwise, we advance both pointers. If we exhaust prev without finding a mismatch, we return True.
