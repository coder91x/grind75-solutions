# Reverse Bits

[Open on LeetCode](https://leetcode.com/problems/reverse-bits) · Easy · Binary

Status: Solved with Help
Date solved: 2026-09-17
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

For this brute force solution I would think that I would create a digits array of 32 size Fill it with zeros And Basically I will Start feeling the digital area from behind By calculating the remainder divided by 2 and filling it in the IM position from behind And then keep on decrementing By a factor of two And this while loop will run Telenb Till N becomes zero After that I will Take Variable result is equal to zero runoff for loop for the length of the digit array calculate the power Which is basically Dg index I have the power will be Length of the digit array Current index one Then result is equal to result Plus the digit add current index Into 2 to that power calculated And then written the result But this is a brute force solution The best solution would Basically running a for P-30 inch of 32 Because Every we are already getting the digits in reversed order when we divide by two We just need one variable to Accumulate those digits And so we create a variable result is equal to zero And we run a forum for our Range of 32 and Basically result is equal to Result into two Plus The digit we are getting Add a reminder after dividing by two Yeah and then return the result
