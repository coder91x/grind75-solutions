# LRU Cache

[Open on LeetCode](https://leetcode.com/problems/lru-cache) · Medium · Linked List

Status: Solved with Help
Date solved: 2026-09-25
Attempts: 3
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

Use a hashmap + doubly linked list because the hashmap gives O(1) lookup and the doubly linked list maintains the usage order in O(1). The hashmap stores key → Node, not just key → value, because after finding a key we need direct access to its linked-list node. Keep two permanent dummy nodes so the list is always LEFT ↔ LRU ↔ ... ↔ MRU ↔ RIGHT; therefore left.next is always the least recently used node and right.prev is always the most recently used node. A doubly linked list is needed because when a node is accessed we need to remove it from anywhere in O(1), which requires both neighbors: node.prev.next = node.next and node.next.prev = node.prev. To make a node MRU, insert it immediately before RIGHT by connecting the old right.prev to the node and the node to RIGHT. For get(key), if the key doesn't exist return -1; otherwise get the node from the hashmap, remove it from its current position, insert it at the MRU end because it was just accessed, and return its value. For put() on an existing key, update the existing node's value and move that same node to MRU; don't create another node. For a new key, create a node, store key → node in the hashmap, and insert it at MRU. If len(hmap) > capacity, evict left.next because that is the LRU, removing it from both the linked list and hashmap using del hmap[lru.key]; this is why each node stores its key as well as its value. The main mental model is: hashmap tells me WHERE the node is, doubly linked list tells me HOW RECENTLY it was used; every access moves the node to MRU, and when full we remove LRU. get and put are O(1).
