# 1. Two Sum

## Problem
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## Approach
Brute force: nested loop checking all pairs.
- Time: O(n²)
- Space: O(1)

## Optimization (Hash Map)
Single pass with a hash map storing `value -> index`.
- Time: O(n)
- Space: O(n)

## Complexity
- **Time**: O(n²) — current implementation
- **Space**: O(1)

## Notes
Current solution uses brute force. Can be optimized to O(n) using a dictionary.