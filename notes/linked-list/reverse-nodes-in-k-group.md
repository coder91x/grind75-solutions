# Reverse Nodes in k-Group

[Open on LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group) · Hard · Linked List

Status: Solved with Help
Date solved: 2026-09-24
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

Use a dummy node and keep group_prev pointing to the node immediately before the next group to reverse. Starting from group_prev, move kth forward k times; if it becomes None, there are fewer than k nodes left, so leave them unchanged and stop. Save group_start = group_prev.next and after_group = kth.next. Reverse only the current group using the normal save → reverse → move prev → move curr process, but instead of starting reverse_prev = None, start with reverse_prev = after_group; this automatically makes the old first node point to the beginning of the next group. Stop reversing when curr == after_group. After reversal, reverse_prev is the new head of the group, so connect it with group_prev.next = reverse_prev, then set group_prev = group_start because the old group start is now the tail and sits immediately before the next group. Repeat this whole process with an outer loop. Remember that after changing curr.next, move forward using the saved next_node, not curr.next. Time is O(n) and extra space is O(1).
