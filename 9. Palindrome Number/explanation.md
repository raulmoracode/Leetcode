# 9. Palindrome Number

## Problem
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

## Approach
Convert to string and check if it reads the same forwards and backwards.
- Handles negative numbers automatically (not palindromes)
- Simple and readable

## Alternative (No String Conversion)
Reverse half the number mathematically and compare.

## Complexity
- **Time**: O(n) where n = number of digits
- **Space**: O(n) for string conversion (O(1) if done mathematically)

## Edge Cases
- Negative numbers → false
- Single digit → true
- Numbers ending in 0 (except 0) → false