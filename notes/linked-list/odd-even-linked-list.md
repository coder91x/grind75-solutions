# Odd Even Linked List

[Open on LeetCode](https://leetcode.com/problems/odd-even-linked-list) · Medium · Linked List

Status: Solved with Help
Date solved: 2026-09-21
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

Start with odd = head and even = head.next. Save even_head = head.next because even will move, but we need to remember where the even chain begins. If head == None, return immediately.
Continue while even != None and even.next != None. even != None ensures the even pointer exists, and even.next != None tells us there is another odd node available after it.
Set odd.next = even.next, which connects the current odd node to the next odd node. Then odd = odd.next moves along the newly created odd chain.
Now that odd has moved to the next odd node, odd.next is the next even node. So set even.next = odd.next, then even = even.next.
Repeat until there are no more nodes to separate. Finally, connect the tail of the odd chain to the saved beginning of the even chain with odd.next = even_head, and return the original head.
