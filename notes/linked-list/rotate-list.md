# Rotate List

[Open on LeetCode](https://leetcode.com/problems/rotate-list) · Medium · Linked List

Status: Solved with Help
Date solved: 2026-09-22
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

Here first we have to calculate total number of nodes by traversing through the list. Initially we start the node count as 1 and basically increment until head.next is not equal to None. Then once we have the number of nodes, we also can get the old tail, which will be the index at which the head will be currently at. Then we also previously captured old head as we have moved the head. Then we calculate k by k is equal to k percent n. If k is equal to zero, we just return the old head. If, yeah, then we calculate new tail by taking a variable i and iterating till it is less than n minus k minus 1. We will move the new tail equal to new tail.next. Initially we will can declare new tail as new tail head. Once we have all the info, we can do old tail.next is equal, we capture new head by taking the new tail.next, then our old tail.next will become equal to old head and our new tail.next will become None and we'll return new head.
