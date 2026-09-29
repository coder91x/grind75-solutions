# Non-overlapping Intervals

[Open on LeetCode](https://leetcode.com/problems/non-overlapping-intervals) · Medium · Array

Status: Solved with Help
Date solved: 2026-09-28
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

For Non-overlapping Intervals, the goal is to remove the minimum number of intervals, which is the same as trying to keep as many non-overlapping intervals as possible. First, sort the intervals by their ending value. We sort by the end because when two intervals overlap, we want to keep the one that ends earlier. The interval that ends earlier gives us more space for the intervals that come later. For example, if we have [1,10] and [2,3], keeping [2,3] is better because after 3 we are free to take more intervals, while [1,10] could block many of them. After sorting, keep the first interval and store its end in prev_end. Then go through the remaining intervals starting from index 1. If current_start < prev_end, there is an overlap, so increase removed and keep prev_end unchanged because the interval we already kept ends earlier. If current_start >= prev_end, there is no overlap, so keep the current interval and update prev_end to its end. Remember that current_start == prev_end is allowed and is not an overlap. The main idea to remember is: keep the interval that ends earliest → it leaves more room for future intervals → we can keep more intervals → therefore we remove fewer intervals. Time is O(n log n) because of sorting.
