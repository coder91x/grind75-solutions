# Sort Colors

[Open on LeetCode](https://leetcode.com/problems/sort-colors) · Medium · Array

Status: Solved with Help
Date solved: 2026-09-15
Attempts: 3
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

Dutch National Flag: Since the array contains only 0, 1, and 2, maintain three boundaries: left, mid, and right. Everything before left is confirmed 0, left to mid-1 is confirmed 1, mid to right is unknown, and everything after right is confirmed 2.
If nums[mid] == 0, swap it with left, then increment both left and mid. The value coming from left is already classified (or left == mid), so we don't need to inspect it again.
If nums[mid] == 1, just increment mid because the 1 is already where it belongs.
If nums[mid] == 2, swap it with right and decrement right, but don't increment mid, because the value coming from right was in the unknown region and still needs to be inspected.
Continue while mid <= right. The key invariant is: left swap brings a classified value into mid; right swap can bring an unclassified value into mid
