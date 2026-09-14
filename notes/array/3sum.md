# 3Sum

[Open on LeetCode](https://leetcode.com/problems/3sum) · Medium · Array

Status: Solved with Help
Date solved: 2026-09-14
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

Here basically we take a for loop and fix I Before that we sort the array because we are going to apply two pointers Then once we do that We Start By fixing one value the ith value and we also run the for loop Till the second last index as the last 10 As the second last and the last index will be J K and K After that Cheque that if the I Position is greater than zero Diet value is equal to equal to I minus 1 th value We increment I till then And then while J is less than K we calculate the current sum if the current sum Is equal to zero we append it into the result And we just increment J then Cheque whether while the J is less than K and The value at J is equal to equal to value at J - 1 we keep on incrementing To just to make sure that we are not repeating the values And if the current sum is greater than 0 Then we decrement the K by one else we increment the J by one in the end we return the result
