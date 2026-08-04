from exercise import Solution

if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        ("MMXXIV", 2024),
    ]
    
    for s, expected in test_cases:
        result = sol.romanToInt(s)
        print(f"Input: s = \"{s}\"")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}")
        print()