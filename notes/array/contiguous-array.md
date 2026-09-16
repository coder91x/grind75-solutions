# Contiguous Array

[Open on LeetCode](https://leetcode.com/problems/contiguous-array) · Medium · Array

Status: Solved with Help
Date solved: 2026-09-16
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

We need the maximum-length contiguous subarray containing an equal number of 0s and 1s. Treat every 0 as -1 and every 1 as +1. Then any subarray containing equal 0s and 1s has a net sum of 0.
Maintain a running balance and a hashmap seen storing balance → earliest index where that balance occurred. Initialize it with {0: -1} because before processing any elements, the balance is 0 at the imaginary index -1. This allows a valid subarray starting at index 0 to be counted correctly.
As we traverse, update the running balance. If we've seen the same balance before, the elements between the previous occurrence and the current index must have a net sum of 0, so their 0s and 1s are equal. Calculate:
length = current_index - seen[balance]
and update max_length. If the balance hasn't been seen before, store its current index. Never overwrite an existing balance, because keeping its earliest occurrence gives us the longest possible subarray.
