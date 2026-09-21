# Remove Nth Node From End of List

[Open on LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list) · Medium · Linked List

Status: Solved with Help
Date solved: 2026-09-21
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

We have to take two pointers fast and slow make fast first reach End nodes from the start And then while fast is not equal to none Increments low and fast by one Eventually slow will be at the Node Just before the node that needs to be removed and We delete that node which has to be deleted by doing slow dot next is equal to slow dot next dot next And then we return the dummy dot next we create a dummy variable here because We also consider that head can Also be removed
