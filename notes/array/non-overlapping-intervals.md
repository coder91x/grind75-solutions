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

For **Non-overlapping Intervals**, think of the problem as **minimum intervals removed = maximum non-overlapping intervals kept**. Sort the intervals by their **ending value**, because when two intervals overlap and we are forced to remove one, we want to keep the one that **ends earlier**; an earlier ending frees up the timeline sooner and leaves more room for future intervals, while keeping an interval with a larger end could unnecessarily block more future intervals. After sorting, keep the first interval and store its end as `prev_end`. For every remaining interval, compare its `current_start` with `prev_end`. If `current_start < prev_end`, they overlap, so remove the current interval by increasing `removed`; we don't change `prev_end` because, since we sorted by end, the interval we already kept ends earlier or at the same time and is therefore the better one to keep. If `current_start >= prev_end`, there is no overlap (touching is allowed), so keep the current interval and update `prev_end = current_end`. We only need `prev_end` because to decide whether the next interval can be kept, all that matters is when the **last kept interval finishes**. Remember to start the loop from index `1` because interval `0` has already been kept. The main intuition is: **keep the interval that ends earliest → leave maximum room for future intervals → keep maximum intervals → remove minimum intervals.** Time is **O(n log n)** because of sorting, and the scan itself is **O(n)**.
