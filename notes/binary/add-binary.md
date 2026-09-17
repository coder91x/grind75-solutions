# Add Binary

[Open on LeetCode](https://leetcode.com/problems/add-binary) · Easy · Binary

Status: Solved with Help
Date solved: 2026-09-17
Attempts: 3
Confidence: 1/5

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

Add Binary — Two Pointers + Carry
Start two pointers i and j at the end of strings a and b, because binary addition happens from right to left. Initialize carry = 0 and an empty result list.
While either string still has digits, get the current digit from each string. If that string has already run out of digits, treat its digit as 0.
Calculate:
total = digit_a + digit_b + carry
The binary digit for the current column is total % 2, and the carry for the next column is total // 2. Append the current digit to the result and decrement both pointers.
After the loop, if a carry remains, append it. Since we generated the answer from right to left, reverse the collected digits, join them into a string, and return it.
