# Product of Array Except Self

[Open on LeetCode](https://leetcode.com/problems/product-of-array-except-self) · Medium · Array

Status: Solved with Help
Date solved: 2026-09-15
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

Instinct: For every index i, the answer is the product of everything to the left of i × everything to the right of i. Instead of recalculating those products for every index, carry running products.
Left pass: Initialize left = 1. Move left → right. At each index, first store left in answer[i], then update left *= nums[i]. We store first because the current number must be excluded from its own answer.
Right pass: Initialize right = 1. Move right → left. At each index, multiply the stored left product by right, then update right *= nums[i]. Again, update afterward so the current number isn't included in its own answer.
Key invariant: When I'm standing at index i, left/right contains the product of the elements I've already passed, not the current element.
