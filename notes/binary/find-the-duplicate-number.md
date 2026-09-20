# Find the Duplicate Number

[Open on LeetCode](https://leetcode.com/problems/find-the-duplicate-number) · Medium · Binary

Status: Solved with Help
Date solved: 2026-09-19
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

This is basically the variant or, like, detection cycle in linked list. So here we create a slow pointer, a fast pointer. We run a for loop on the nums array, and basically the value at the value in the array represents the next position it is going. So for example, if the array is 1 3 4 2 2, 1 represents tf you're currently at index 1, nums[1] = 3, so you go to index 3. Then nums[3] = 2, so you go to index 2. So we basically use the same algorithm called the Floyd's algorithm as we use in linked list cycle detection. So here basically the slow will become nums of slow, fast will become nums of nums of fast. Why nums of slow? Because initially we'll be starting at 0. So we are creating 0 is telling us to go to 1. So basically nums of slow is telling us where slow should go, same with the fast, but two steps. So we are doing that. Then if slow is equal to equal to fast, which means there is a cycle, we start, we create a new pointer P1 and P2, where P1 will become 0 and P2 will basically remain where the fast pointer ends. And then while P1 is not equal to P2, we'll run that loop, and eventually when P1 and P2 will become equal, and we return P1.
