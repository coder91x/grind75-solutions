# Subarray Sum Equals K

[Open on LeetCode](https://leetcode.com/problems/subarray-sum-equals-k) · Medium · Array

Status: Solved with Help
Date solved: 2026-09-16
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

We create a hashmap where each key is a prefix sum we've previously encountered, and its value is how many times we've encountered that prefix sum. We initialize it with {0: 1} because before the array begins, prefix sum 0 has occurred once.
As we traverse the array, we maintain a running curr_prefix. Since the sum of a subarray is current_prefix - previous_prefix, and we want that sum to equal k, the previous prefix we need is curr_prefix - k.
If that required previous prefix exists in the hashmap, its frequency tells us how many valid subarrays ending at the current index exist, so we add that frequency to count.
Then, regardless of whether we found one, we record the current prefix in the hashmap by increasing its frequency. Finally, return count.
