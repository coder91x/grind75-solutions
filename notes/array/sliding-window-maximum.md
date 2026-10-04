# Sliding Window Maximum

[Open on LeetCode](https://leetcode.com/problems/sliding-window-maximum) · Hard · Array

Status: Solved with Help
Date solved: 2026-10-04
Attempts: 2
Confidence: 2/5

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

For Sliding Window Maximum, the idea is that we have to maintain a deque because we need to remove elements from both the front and the back. At every given point, the deque contains the candidates that are still potential maximums for the current window or a future window. We iterate through the array, and before that we declare an answer array and a deque dq. For every i, first we check the front to see if the candidate there has become too old and has passed outside the current window. We check this using dq[0] <= i - k, and if that is true, we remove it using dq.popleft(). Then we check the current number nums[i] against the back of the deque. While the deque is not empty and nums[i] > nums[dq[-1]], the candidate at the back is smaller than the current number and is therefore no longer a useful maximum candidate, so we remove it using dq.pop(). We keep doing this until the back is no longer smaller, and then we insert the current index i at the back using dq.append(i). Finally, we check whether we have a complete window using i >= k - 1. If we do, the maximum of that window is always at the front of the deque, so we add nums[dq[0]] to answer. The important thing is that the deque stores indices, not values: the front is used to remove candidates that are too old, while the back is used to remove candidates that have become useless because a newer, larger value has arrived.
