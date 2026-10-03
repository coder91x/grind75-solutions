# Daily Temperatures

[Open on LeetCode](https://leetcode.com/problems/daily-temperatures) · Medium · Stack

Status: Solved with Help
Date solved: 2026-10-03
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

For Daily Temperatures, go from left to right and keep a stack of days whose next warmer temperature has not been found yet. Store both (temperature, index) because when a warmer temperature is found, we need the index difference to calculate how many days we waited. For every current temperature, compare it with the temperature at the top of the stack. While the stack is not empty and the current temperature is greater than the top temperature, pop that day because the current day has now answered its question, and set answer[popped_index] = current_index - popped_index. Keep popping because one current temperature can solve multiple previous days, like 72 solving both 69 and 71. Once the current temperature can no longer solve the top, push (current_temperature, current_index) because the current day itself is now waiting for a warmer future day. The temperatures remaining in the stack naturally stay in decreasing order from bottom to top, which is why this is called a monotonic decreasing stack, but the important intuition is not “maintain a decreasing stack”; it is “the stack contains unresolved days, and when the current temperature is warmer, their question has been answered.” Any days left in the stack at the end never get a warmer future day, so their answer stays 0. Each day is pushed once and popped at most once, so time is O(n) and space is O(n).
