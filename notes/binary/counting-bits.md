# Counting Bits

[Open on LeetCode](https://leetcode.com/problems/counting-bits) · Easy · Binary

Status: Solved with Help
Date solved: 2026-09-17
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

Brute force: Count every number's bits from scratch using % 2 and // 2 → O(n log n).
DP: Ask what work is being repeated. i // 2 removes the last bit and is a smaller number whose answer is already stored. i % 2 tells whether the removed bit was 1. Therefore ans[i] = ans[i // 2] + i % 2 → O(n).
DP mental model: solve smaller → store → reuse.
