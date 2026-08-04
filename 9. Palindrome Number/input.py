from exercise import Solution

if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (12321, True),
        (123, False),
    ]
    
    for x, expected in test_cases:
        result = sol.isPalindrome(x)
        print(f"Input: x = {x}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}")
        print()