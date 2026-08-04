# 13. Roman to Integer

## Problem
Given a roman numeral, convert it to an integer.

## Approach
Single pass left-to-right:
- If current value < next value → subtract current
- Else → add current
- Handle last character separately (always add)

## Roman Values
| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

## Subtraction Cases
- IV = 4, IX = 9
- XL = 40, XC = 90
- CD = 400, CM = 900

## Complexity
- **Time**: O(n) where n = length of string
- **Space**: O(1) — only hash map of fixed size (7 entries)

## Notes
Input guaranteed valid Roman numeral in range [1, 3999].