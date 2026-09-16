# Gas Station

[Open on LeetCode](https://leetcode.com/problems/gas-station) · Medium · Array

Status: Solved with Help
Date solved: 2026-09-15
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

Gas Station — Greedy: First check global feasibility: if total gas < total cost, completing the circuit is impossible. While scanning, keep a running tank for the current candidate start: curr += gas[i] - cost[i]. If the running tank becomes negative at i, the current start fails, and every station from that start through i can also be discarded, so the next candidate is i + 1 and the running tank resets to 0. If total gas ≥ total cost, the final candidate start is valid.
